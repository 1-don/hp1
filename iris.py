import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv("iris.data")
print df.head()
print df.info()
print df.describe()
print df["sepal_length"]
print df[["sepal_length","petal_length"]]

print df.columns.values
for col in df.columns.values[:-1]:
	print col
	df.hist(column=col)

plt.show()

df.boxplot(column=list(df.columns.values[:-1]))

plt.show()












#sudo apt-get install python-dev
#sudo apt-get install python-pip


#:~$ cd Desktop
#~/Desktop$ cd p1
#:~/Desktop/p1$ python prac1.py
#    sepal_length  sepal_width  petal_length  petal_width        class
# 0           5.1          3.5           1.4          0.2  Iris-setosa
# 1           4.9          3.0           1.4          0.2  Iris-setosa
# 2           4.7          3.2           1.3          0.2  Iris-setosa
# 3           4.6          3.1           1.5          0.2  Iris-setosa
# 4           5.0          3.6           1.4          0.2  Iris-setosa
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 150 entries, 0 to 149
# Data columns (total 5 columns):
# sepal_length    150 non-null float64
# sepal_width     150 non-null float64
# petal_length    150 non-null float64
# petal_width     150 non-null float64
# class           150 non-null object
# dtypes: float64(4), object(1)
# memory usage: 7.0+ KB
# None
#        sepal_length  sepal_width  petal_length  petal_width
# count    150.000000   150.000000    150.000000   150.000000
# mean       5.843333     3.054000      3.758667     1.198667
# std        0.828066     0.433594      1.764420     0.763161
# min        4.300000     2.000000      1.000000     0.100000
# 25%        5.100000     2.800000      1.600000     0.300000
# 50%        5.800000     3.000000      4.350000     1.300000
# 75%        6.400000     3.300000      5.100000     1.800000
# max        7.900000     4.400000      6.900000     2.500000

