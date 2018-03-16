from pandas import Series, DataFrame
import pandas as pd
import numpy as np

data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
      'year':[2000,2001,2002,2001,2002],
      'pop':[1.5,1.7,3.6,2.4,2.9]}
frame=DataFrame(data)
DataFrame(data,columns=['year','state'])
frame2=DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five'])
frame2.columns
frame2.index
frame2['state']
frame2.year
frame2.ix['three']
frame2.debt=16.5
frame2['debt']=np.arange(5)

val=Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt']=val
frame2['eastern']=frame2.state=='Ohio'
del frame2['eastern']
pop={'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame3=DataFrame(pop)
frame3.T
DataFrame(pop,index=[2001,2002,2003])
pdata={'Ohio':frame3['Ohio'][:-1],'Nevada':frame3['Nevada'][:2]}
DataFrame(pdata)

