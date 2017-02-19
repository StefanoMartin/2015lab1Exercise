import IPython #IPython is what you are using now to run the notebook
import numpy as np # Numpy is a library for working with Arrays
import scipy as sp # SciPy implements many different numerical algorithms
import pandas as pd # Pandas makes working with data tables easier
import matplotlib # Module for plotting
import sklearn # SciKit Learn implements several Machine Learning algorithms
import requests # Requests is a library for getting data from the Web
import bs4 #BeautifulSoup is a library to parse HTML and XML documents
import pyquery

print "IPython version:      %6.6s (need at least 3.0.0)" % IPython.__version__
print "Numpy version:        %6.6s (need at least 1.9.1)" % np.__version__
print "SciPy version:        %6.6s (need at least 0.15.1)" % sp.__version__
print "Pandas version:       %6.6s (need at least 0.16.2)" % pd.__version__
print "Mapltolib version:    %6.6s (need at least 1.4.1)" % matplotlib.__version__
print "Scikit-Learn version: %6.6s (need at least 0.16.1)" % sklearn.__version__
print "requests version:     %6.6s (need at least 2.0.0)" % requests.__version__
print "BeautifulSoup version:%6.6s (need at least 4.4)" % bs4.__version__
print "Loaded PyQuery"
