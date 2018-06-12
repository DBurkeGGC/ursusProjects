# MonteCarlo Pi 
rm(list=ls())

set.seed(5757)

NTrials <- c(10,10^2,10^3,10^4,10^5,10^6)
Ncases <- length(NTrials)
PiEst <- numeric(Ncases)

for( i in 1:Ncases) {
  Rcount <- 0
  for (j in 1:NTrials[i]) {
    x <- runif(1)
    y <- runif(1)
    if( x^2 + y^2 <= 1) {
      Rcount <- Rcount + 1
    }
  }
  PiEst[i] <- 4*Rcount/NTrials[i]
}

sink("MCPi_R_novector.txt")
print(cbind(NTrials,PiEst))
sink()

pdf("MCPi_R_novector.pdf")
plot(NTrials,PiEst,
	main="Monte Carlo Estimation of Pi (R, Basic)",
	xlab="Number of Trials",
	ylab="Estimation of Pi")
dev.off()
