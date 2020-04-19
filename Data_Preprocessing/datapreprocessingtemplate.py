##Importing Lib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import random

#dataset
data=pd.read_csv("Data.csv",encoding='utf-8')
X=data.iloc[:,0:-1].values
y=data.iloc[:, 3].values


###taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3]=imputer.transform(X[:, 1:3])

##Encoding categorical data Independent variable
##Dummy Data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder_X= LabelEncoder()
X[:,0] = labelEncoder_X.fit_transform(X[:,0])

onehotencoder = OneHotEncoder(categorical_features= [0])
X = onehotencoder.fit_transform(X).toarray()

##Encoding Dependent variable
## In Genral we will not do onehotencoder on Dependent variables

labelEncoder_y= LabelEncoder()
y= labelEncoder_y.fit_transform(y)


#### Splitting the data set into Training set and Test Set
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state = 0)

####Scaling##

from sklearn.preprocessing import StandardScaler 
sc_X= StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


#### Final data preprocessing###
