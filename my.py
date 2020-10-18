

import pandas as pd
import warnings
import pickle
warnings.filterwarnings("ignore")

df=pd.read_csv(r'sample1.csv')
import numpy
OTT=numpy.array(df.OTT)
hours=numpy.array(df.hours)
OTT=OTT.reshape(-1,1)
from sklearn.linear_model import LinearRegression
mind=LinearRegression()
mind.fit(OTT,hours)
a=int(input('Enter OTT'))
example=mind.predict([[a]])
print(example)


pickle.dump(mind,open('mode2.pkl','wb'))
model=pickle.load(open('mode2.pkl','rb'))
