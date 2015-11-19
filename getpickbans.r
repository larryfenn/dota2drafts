# expected in: [match_id, radiant_win, duration, 1is_pick, 1team_id, 1hero_id, ...]
parseRow <- function(x) {
    result <- matrix(0, nrow=20, ncol=113)
    radiantpicks <- 0
    radiantbans <- 0
    direpicks <- 0
    direbans <- 0
    for (i in 1:20) {
        ispick <- x[[3*i + 1]]
        side <- strtoi(x[[3*i + 2]])
        hero <- strtoi(x[[3*i + 3]])
        if (ispick == "True") {
            if (side == 0) {
                radiantpicks <- radiantpicks + 1
            } else {
                direpicks <- direpicks + 1
            }
            result[11 - (radiantpicks + direpicks), hero] <- result[11 - (radiantpicks + direpicks), hero] + 1
        } else {
            if (side == 0) {
                radiantbans <- radiantbans + 1
            } else {
                direbans <- direbans + 1
            }
            result[10 + (radiantbans + direbans), hero] <- result[10 + (radiantbans + direbans), hero] + 1
        }
    }
    data.frame(result)
}



reqPkgs <- c("snow", "parallel", "snowfall")
new.packages <- reqPkgs[!(reqPkgs %in% installed.packages()[,"Package"])]
if (length(new.packages)) {install.packages(new.packages)}

library(snow)
library(parallel)

coreCount <- detectCores()

raw <- read.csv("capmodedata.csv")
picksbans <- data.frame(matrix(0, nrow=20, ncol=113), row.names = c(sapply(10:1, function(x) paste(x, "pick", sep="")), sapply(1:10, function(x) paste(x, "ban", sep=""))))

timing <- proc.time()

parallel <- FALSE
if (parallel) {
    cl <- makeCluster(coreCount, type = "SOCK")
    picksbans <- Reduce('+', parRapply(cl, raw, parseRow))
    stopCluster(cl)
} else {
    for (i in 1:nrow(raw)) {
        picksbans <-  picksbans + parseRow(raw[i,])
    }
}
timing <- proc.time() - timing

picksbans <- data.frame(picksbans, row.names = c(sapply(10:1, function(x) paste(x, "pick", sep="")), sapply(1:10, function(x) paste(x, "ban", sep=""))))

print(timing)
