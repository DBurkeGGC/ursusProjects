# MonteCarlo Pi 
rm(list=ls())

set.seed(5757)

NTrials <- c(10,10^2,10^3,10^4,10^5,10^6)
Ncases <- length(NTrials)
PiEst <- numeric(Ncases)

for( i in 1:Ncases) {
    x <- runif(NTrials[i])
    y <- runif(NTrials[i])
    Rcount <- sum( x^2 + y^2 <= 1)
    PiEst[i] <- 4*Rcount/NTrials[i]
}

sink("MCPi_R_vector.txt")
print(cbind(NTrials,PiEst))
sink()

pdf("MCPi_R_vector.pdf")
plot(NTrials,PiEst, 
	main="Monte Carlo Estimation of Pi (R, Vectorized)",
	xlab="Number of Trials",
	ylab="Estimation of Pi")
dev.off()
