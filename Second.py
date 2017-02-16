import pandas
from pandas.tools.plotting import scatter_matrix

import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# READ DATA FROM ONLINE
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names) # Note that we load it with pandas

# INTERPRETATE DATA
print()
print("TABLE\n")
print(dataset.shape) # Check shape of our table
print("\n")
print(dataset.head(20)) # Print only the first 20 rows of data3
print("\n STATISTICS \n")
print(dataset.describe()) # Return some statistics of a dataset
print("\n SIZE GROUPS \n")
print(dataset.groupby('class').size()) # Return the size of different groups

# CREATE PLOT
# Univariate plots
dataset.plot(kind="box", subplots=True, layout=(2,2), sharex=False, sharey=False) # Box plot
plt.show()

dataset.hist() # histogram
plt.show()

# Multivariate plots
scatter_matrix(dataset)
plt.show()
