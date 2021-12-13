import pandas
import numpy

from factor_analyzer import FactorAnalyzer

import matplotlib.pyplot as pyplot



dataset  = pandas.read_csv("dataset_final.csv")


dataset.drop(['country'], axis=1, inplace=True)
dataset.drop(['Unnamed: 0'], axis=1, inplace=True)

dataset.dropna(inplace=True)

#print(dataset)

machine = FactorAnalyzer(n_factors=40, rotation=None)
machine.fit(dataset)
ev, v = machine.get_eigenvalues()
print(ev)

pyplot.scatter(range(1,dataset.shape[1]+1), ev)
pyplot.savefig("plot.png")
pyplot.close()

machine = FactorAnalyzer(n_factors=4, rotation='varimax')
machine.fit(dataset)
output = machine.loadings_
numpy.set_printoptions(suppress=True)
print(output)

dataset = dataset.values
result = numpy.dot(dataset, output)

print(result)
print(result.shape)

from numpy import savetxt

from numpy import asarray
savetxt('final.csv', result, delimiter=',')