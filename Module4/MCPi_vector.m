% MonteCarlo Pi
clear;

rand("seed",5757);

NTrials = [10; 10^2; 10^3; 10^4; 10^5; 10^6];
Ncases = numel(NTrials);
PiEst = zeros(Ncases,1);

for i =1:Ncases 
  x=rand(NTrials(i),1);
  y=rand(NTrials(i),1);
  Rcount=sum(x.^2+y.^2<=1);
  PiEst(i) = 4*Rcount/NTrials(i); 
end

dlmwrite("MCPi_octave_vector.txt",[NTrials,PiEst]);

hf = figure();
plot(NTrials',PiEst')
title("Monte Carlo Estimation of Pi (Octave, Vectorized)");
xlabel("Number of Trials");
ylabel("Estimation of Pi");
print(hf,"MCPi_octave_vector.pdf");
