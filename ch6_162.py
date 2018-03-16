from pandas import Series, DataFrame
import pandas as pd
import numpy as np

df=pd.read_csv('E:/study/python/pydata-book-master/ch06/ex1.csv')
pd.read_table('E:/study/python/pydata-book-master/ch06/ex1.csv',sep=',')
pd.read_csv('E:/study/python/pydata-book-master/ch06/ex2.csv',header=None)
pd.read_csv('E:/study/python/pydata-book-master/ch06/ex2.csv',names=['a','b','c','d','message'])
names=['a','b','c','d','message']
pd.read_csv('E:/study/python/pydata-book-master/ch06/csv_mindex.csv',names=names,index_col='message')
parsed=pd.read_csv('E:/study/python/pydata-book-master/ch06/csv_mindex.csv', index_col=['key1', 'key2'])
list(open('E:/study/python/pydata-book-master/ch06/ex3.txt'))
result=pd.read_table('E:/study/python/pydata-book-master/ch06/ex3.txt',sep='\s+')
pd.read_csv('E:/study/python/pydata-book-master/ch06/ex4.csv',skiprows=[0,2,3])
result=pd.read_csv('E:/study/python/pydata-book-master/ch06/ex5.csv')
pd.isnull(result)
result=pd.read_csv('E:/study/python/pydata-book-master/ch06/ex5.csv',na_values=['NA'])

result=pd.read_csv('E:/study/python/pydata-book-master/ch06/ex6.csv')
result=pd.read_csv('E:/study/python/pydata-book-master/ch06/ex6.csv',nrows=5)
chunker=pd.read_csv('E:/study/python/pydata-book-master/ch06/ex6.csv',chunksize=1000)
tot=Series([])
for piece in chunker:
    tot=tot.add(piece['key'].value_counts(),fill_value=0)
tot=tot.order(ascending=False)
pd.read_csv()

