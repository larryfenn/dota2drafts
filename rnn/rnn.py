"""
Many thanks to Andrej Karpathy (@karpathy)
https://gist.github.com/karpathy/d4dee566867f8291f086
"""

import numpy as np
np.random.seed(1)

# data I/O
data = open('test.txt', 'r').read().rstrip() # should be simple plain text file
trials = data.split('\n')
data_size, hero_count = len(trials), 112 # number of heroes in dota 2

def parseTrial(line):
	"""
	line: 'string:with:colon:seps'
	first four components are pick and ban sets
	last component is time to win (negative if a loss)
	returns the four hero lists, and the time to win, in a list
	"""
	output = list()
	for l in line.split(':'):
		output.append(list(map(int, l.split(',')))) # may need to change this for python 2.7
	return output

def scoring(x):
	if x > 0:
		return np.exp(-x/6000)
	else:
		return -np.exp(x/6000)

def invscoring(x):
	if (x >= 0):
		winner = "radiant"
	else:
		winner = "dire"
	return -6000*np.log(abs(x)), winner

hidden_size = 100 # layers
seq_length = 1 # grab the next BLA units of whatever
learning_rate = 1e-1

Wxh = np.random.randn(hidden_size, 4*hero_count + 1)*0.01
Whh = np.random.randn(hidden_size, hidden_size)*0.01
Why = np.random.randn(1, hidden_size)*0.01
bh = np.zeros((hidden_size, 1))
by = np.zeros((1, 1))

def lossFun(inputs, hprev):
	"""
	inputs: list of separate games to compute over.
	hprev is previous hidden state
	return loss, gradients on model parameters, and last hidden state
	"""
	targets = list()
	xs, hs, ys, ps = {}, {}, {}, {}
	hs[-1] = np.copy(hprev)
	loss = 0
	# forward pass
	for t in range(len(inputs)): # iterate over 'len(inputs)' many separate games
		xs[t] = np.zeros((4*hero_count + 1, 1))
		# inputs[t] is a 'trial'; a list of lists.
		for i in range(len(inputs[t])): # in a game, iterate over the ban/pick lists
			if i == 4: # special case: the last number is the game time, fed through the objective function
				targets.append(scoring(inputs[t][i][0]))
			else: # general case: fill in the hero list
				for j in inputs[t][i]:
					xs[t][i*hero_count + j] = 1

		hs[t] = np.tanh(np.dot(Wxh, xs[t]) + np.dot(Whh, hs[t-1]) + bh) #hidden state
		ys[t] = np.dot(Why, hs[t]) + by #unnormalized log probabilities for next chars
		ps[t] = np.exp(ys[t]) / np.sum(np.exp(ys[t])) #probabilities for next chars
		loss += -np.log(ps[t][targets[t],0]) #softmax (cross-entropy loss)

	# backward pass: compute gradients going backwards
	dWxh, dWhh, dWhy = np.zeros_like(Wxh), np.zeros_like(Whh), np.zeros_like(Why)
	dbh, dby = np.zeros_like(bh), np.zeros_like(by)
	dhnext = np.zeros_like(hs[0])
	for t in reversed(range(len(inputs))):
		dy = np.copy(ps[t])
		dy[targets[t]] -= 1 #backprop into y
		dWhy += np.dot(dy, hs[t].T)
		dby += dy
		dh = np.dot(Why.T, dy) + dhnext #backprop into h
		dhraw = (1 - hs[t] * hs[t]) * dh #backprop through tanh nonlinearity
		dbh += dhraw
		dWxh += np.dot(dhraw, xs[t].T)
		dWhh += np.dot(dhraw, hs[t-1].T)
		dhnext = np.dot(Whh.T, dhraw)
	for dparam in [dWxh, dWhh, dWhy, dbh, dby]:
		np.clip(dparam, -5, 5, out=dparam) #clip to mitigate exploding gradients
	return loss, dWxh, dWhh, dWhy, dbh, dby, hs[len(inputs)-1]

def sample(h, seed):
	"""
	attempt to predict the outcome based on "seed", the input vector
	"""
	x = np.zeros((4*hero_count + 1, 1))
	for i in range(len(seed) - 1):
		for j in seed[i]:
			x[i*hero_count + j] = 1
	goal = scoring(seed[4][0])
	ixes = []
	h = np.tanh(np.dot(Wxh, x) + np.dot(Whh, h) + bh)
	y = np.dot(Why, h) + by
	return y

n, p = 0, 0
mWxh, mWhh, mWhy = np.zeros_like(Wxh), np.zeros_like(Whh), np.zeros_like(Why)
mbh, mby = np.zeros_like(bh), np.zeros_like(by) # memory variables for Adagrad
smooth_loss = -np.log(1.0/hero_count)*seq_length # loss at iteration 0

while True:
	# prepare inputs (sweeping left to right in steps seq_length long)
	if p >= len(trials) or n ==0:
		hprev = np.zeros((hidden_size, 1)) # reset RNN memory
		p = 0 # go from start of data
		break # instead this should be an exit
	# inputs should be a list, seq_length long, of game vectors
	inputs = list()
	for i in range(seq_length):
		inputs.append(parseTrial(trials[p + i]))

	# sample from model now and then
	if n % 100 == 0:
		game = [[28,29,93,94,89],[23,14,56,48,82],[72,68,51,87,25],[100,39,3,61,8],[6262]]
		txt = invscoring(sample(hprev, game)[0][0])
		print('----\n %s \n----' % (txt, ))

	# forward seq_length characters through the net and fetch gradient
	loss, dWxh, dWhh, dWhy, dbh, dby, hprev = lossFun(inputs, hprev)
	smooth_loss = smooth_loss * 0.999 + loss * 0.001
	if n % 100 == 0 : print('iter %d, loss %f' % (n, smooth_loss)) # print progress

	# perform parameter update with Adagrad
	for param, dparam, mem in zip([Wxh, Whh, Why, bh, by],
	                              [dWxh, dWhh, dWhy, dbh, dby],
	                              [mWxh, mWhh, mWhy, mbh, mby]):
		mem += dparam * dparam
		param += -learning_rate * dparam / np.sqrt(mem + 1e-8) # adagrad update

	p += seq_length # move data pointer
	n += 1 # iteration counter
