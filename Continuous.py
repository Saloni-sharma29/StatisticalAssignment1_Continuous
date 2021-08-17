from numpy.random import normal
from scipy.stats import norm
import scipy.stats
from matplotlib import pyplot
import statistics
import matplotlib.pyplot as plt
import random
import math
import numpy as np
#creating a population
print('Normal distribution')
population= [random.randint(0,100) for x in range(100)]
populationMean= statistics.mean(population)
print(population)
print(' Population Mean {}'.format(populationMean) )
mu=populationMean #creating samples
sigma=5
size=20
sample= normal(mu, sigma, size).tolist() #generate many sample
#testsample=normal(mu, sigma, size).tolist()
meanlist=[]
varlist=[]
for i in range(5):
    temp=normal(mu, sigma,size)
    sample.extend(temp)
    #print('\nSamples {} '.format(i+1),sample)
    mean=statistics.mean(sample)
    meanlist.append(mean)
    var= statistics.variance(sample)
    varlist.append(var)
print('All mean values')
for i in meanlist:
    print(i)
print('\nAll variance values')
for i in varlist:
    print(i)
print ('\nExpectation E[x] {}'.format(statistics.mean(meanlist)))

print("\n********Checking for Biased/ Unbiased estimator*******")
if ( round(populationMean)==round(statistics.mean(meanlist))):
    print("\t\tUnbiased Estimator")
else:
    print("\t\tBiased Estimator")

print("\n\n**************Tailed  t-Test**************")
#tailed t test(checking whether the drawn samples are from the same population or not )
alpha=0.05 #levelof significance
#both samples are from same population
testsample1=[32.673454310450005, 49.940601777171075, 48.78716691724057, 46.45682307748068, 52.84772653411166, 41.95897462564672, 44.621892530101015, 49.4356582294638, 44.05151827515441, 53.532007128948024, 39.041434500793294, 47.036092972845275, 47.11117728132795, 52.979126465294975, 55.990020754568306, 54.10146325872839, 49.12567345045704, 38.4437509793944, 49.987488191767625, 43.32102394241081, 45.5682041362608, 48.891195091621725, 30.51159426685728, 26.443020124045823, 33.854955328030755, 34.33157829796744, 37.59630311162043, 40.64714587841358, 38.015110884187266, 40.33272515239269]
#testsample2=[44.28760085877977, 52.19368669397271, 46.01565274409231, 45.743823849984565, 34.829798985733035, 44.793022182516374, 43.337086098265864, 53.06904974469225, 52.519964523499354, 36.08502916467928, 49.57384526192511, 42.336648546214555, 54.27877437045529, 56.687322228025636, 40.23862654101876, 43.53596049554759, 43.33960285810991, 42.2572784930678, 54.49766493692633, 25.4231329017662, 46.47104857452629, 43.905843094668434, 37.30768018045746, 44.40503471312516, 44.03013651870655, 50.97271542384164, 23.709251331749776, 40.39024533475154, 47.505329918046996, 41.51224291688304]
print('I took sample from different population')
print('Null Hypothesis H0: means are equal')
print('Alternate Hypothesis H1: means are not equal')
population2= [random.randint(0,300) for x in range(300)]
populationMean2= statistics.mean(population2)
testsample2= normal(populationMean2, 15, size).tolist()
for i in range(0):
    temp=normal(mu, sigma,size)
    testsample2.extend(temp)
#print('\nTest Samples 1 {} '.format(testsample1))
#print('\nTest Samples 2 {} '.format(testsample2))
testmean1=statistics.mean(testsample1)
testmean2=statistics.mean(testsample2)

print('\nTest sample 1--- Mean {}'.format(testmean1))
print('Test sample 2--- Mean {}'.format(testmean2))
t_value =scipy.stats.ttest_ind(testsample2,testsample1) #t test
#print('t value = {} \np value = {}'.format(t_value.statistic,t_value.pvalue))

#Interpret via p_value
if(t_value.pvalue>alpha):
    print("\nResult:  Accept the null hypothesis that the means are equal")
else:
    print("\nResult:  Reject the  null hypothesis that the means are equal")

#plotting mean
values=[value for value in range (1,100,20)]
plotmean=[meanlist for value in values]
plt.plot(values, plotmean,label='mean')
#plotting variance
values=[value for value in range (1,100,20)]
plotvar=[varlist for value in values]
plt.plot(values, plotvar,label='variance')
dist=norm(mu, sigma)
plt.legend()
plt.show()
#plotting pdf
values=[value for value in range (20 ,80)]
probabilities= [dist.pdf(value) for value in values]
plt.text(30,55, 'Normal Distribution')
#print(probabilities)
pyplot.plot(values, probabilities,label='pdf')
#pyplot.show()

#plotting cdf
values=[value for value in range (20 ,80)]
cprob=[dist.cdf(value) for value in values]
plt.text(50,1, 'Normal Distribution')
#print(cprob)
pyplot.plot(values,cprob,label='cdf')
plt.legend()
pyplot.show()

