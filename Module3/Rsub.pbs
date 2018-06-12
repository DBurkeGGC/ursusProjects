#PBS -l nodes=1:ppn=1
#PBS -l walltime=1:00:00
### Merge stderr with stdout
#PBS -j oe
### Queue names (low, medium, default, and high)
#PBS -q batch
### Job name
#PBS -N R_pbs_job
### Declare job-non-rerunable
#PBS -r n
#PBS -M myemail@ggc.edu

# This job's working directory
echo Job ID: $PBS_JOBID
echo Working directory is $PBS_O_WORKDIR
cd $PBS_O_WORKDIR
echo Running on host `hostname`
echo Time is `date`
echo Directory is `pwd`
echo This job runs on the following processors:
echo `cat $PBS_NODEFILE`

#Define number of processors
NPROCS=`wc -l < $PBS_NODEFILE`
echo This job has allocated $NPROCS nodes/processors.

module load  R-3.4.0

# Command line:
/usr/bin/time R CMD BATCH MCPi_0b.R > MCPi_0b_R.out 2>&1
