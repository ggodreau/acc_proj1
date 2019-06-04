#DO NOT MODIFY THE CODE IN THIS FILE
#File: Proj01.py

from Proj01Runner import Runner
import sys
import math
from statistics import mean
from statistics import median
from statistics import stdev
from statistics import pstdev

import random

def normalRandomGenerator(seed=1,dataLength=10000,numberSamples=50,\
                          lowLim=0,highLim=100):
    '''
    Create a new dataset of dataLength values consisting of the 
    average of numberSamples samples taken from a population of 
    uniformly distributed values between lowLim and highLim 
    generated with a seed of seed.

    Input keyword parameters and their default values:

    seed = 1 seed used to generate the uniformly distributed values
    dataLength = 10000 number of samples in the returned list of values
    numberSamples = 50 number of samples taken from the uniformly 
                    distributed population and averaged into the output
    lowLim = 0 lower limit value of the uniformly distributed population
    highLim = 100 high limit value of the uniformly distributed population

    returns: a list containing the dataset
    '''
    data = []
    random.seed(seed)

    for cnt in range(dataLength):
        theSum = 0
        for cnt1 in range(numberSamples):
            theSum += random.uniform(lowLim,highLim)
        data.append(theSum/numberSamples)
        
    return data
    #=========================================================================#

print("The command-line arguments are: " , str(sys.argv))

args = sys.argv[1].split(",")

xSeed = int(args[0])
xDataLength = int(args[1])
xNumberSamples = int(args[2])
xLowLim = int(args[3])
xHighLim = int(args[4])
print("xSeed =",xSeed)
print("xDataLength =",xDataLength)
print('xNumberSamples =',xNumberSamples)
print('xLowLim =',xLowLim)
print('xHighLim =',xHighLim)
print()


print("The code that you write may not \n \
import anything other than math.\n\
")

#Create a dataset using command-line parameters
data = normalRandomGenerator(seed=xSeed,dataLength=xDataLength,\
       numberSamples=xNumberSamples,\
       lowLim=xLowLim,\
       highLim=xHighLim\
       )
       
print("Output from student code begins here.")
#Call the run method in the student's file

print('DATA be poppin', data)
xMean,xMedian,xStdev,xpStdev = Runner.run(data)
print()

#Print student output values and compare with the standard values
# produced by calling built-in Python functions.
print("xMean =",xMean)
print("mean = ",round((mean(data)*100))/100)
print("xMedian =",xMedian,)
print("median = ",round((median(data)*100))/100)
print("Sample xStdev =",xStdev)
print("Sample stdev = ",round((stdev(data)*100))/100)
print("Population xpStdev =",xpStdev)
print("Population pstdev = ",round((pstdev(data)*100))/100)



