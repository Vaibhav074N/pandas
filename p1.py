"""
Pandas:
       it contains data structures and data manipulation tools designed to make
       data cleaning and data analysis, fast and easy in python.

It has two D-S:
        1. Series - it is a 1-D array like object containing a sequence and values.
        2. Dataframe - it represents a rectangular table of data and contains an ordered
                       collection of columns,each of which can be different value type
                       (numeric,string,boolean,etc).
"""

# import pandas as pd

# obj = pd.Series([4,7,-5,3])
# print(obj)

# obj1=pd.Series([4,7,-5,3],index=['a','b','c','d'])
# print(obj1)
# print(obj1.values)
# print(obj1.index)

# print(obj1['a'])             # Accessing values with obj

# print(obj1[obj1>0])
# print('a' in obj1)

""" if you have data contained in a python dict,you can create
    a series from it by passing the dict. 
    Ex:
"""
# data = {'c':300,'d':200,'a':100}
# obj2=pd.Series(data)
# print(obj2)
# data1=['a','b',"c"]              # b is not present in data therefore it show NaN
# obj3=pd.Series(data,index=data1)
# print(obj3)

"""
The isnull and notnull functions in pandas should be used to detect missing data.
Ex: pd.isnull() , pd.notnull()
"""
# print(pd.isnull(obj3))
# print(pd.notnull(obj3))

"""
Both the series object itself and its index have a name attribute, which
integrates with other key areas of pandas.
"""
# obj2.name="Alpha"
# obj2.index.name="Salary"
# print(obj2)

#----------------------------------------------------------------------------------#

""" There are many ways to construct a dataframe, though one of the most common is 
    from a dict of equal length lists."""
import pandas as pd

# data = {"state":['nanded','ohio','ohio','ohio','nevada'],
#         "year":[2004,2003,2002,2001,2000],
#         "pop":[1.5,1.7,3.6,2.4,2.9]}
# frame = pd.DataFrame(data)
# print(frame)
# f=pd.DataFrame(data,columns=['year','state','pop'])
# print(f)

""" for large dataframe,the head method selects only the first five rows. Ex:f.head()
    or we can pass parameter to it. Ex: f.head(2)"""
# print(frame.head(2))

# frame1=pd.DataFrame(data,columns=['year','state','pop','debt'],index=['1','2','3','4','5'])
# print(frame1)
""" If you pass a column that isn't contained in the dict ,it will appear with
    missing values in result. Ex: NaN"""

"""Column in dataframe can be retrive as a series.
   Rows can also br retrieved by position or name with special loc attribute."""
# print(frame1['year'])
# print(frame1.state)

# print(frame1.loc['4'])

""" Another common from of data is a nested dict if dicts.
    if the nested dict is passed to the dataframe, pandas will interpret the outer
    dict-keys as a column and inner-keys as a row indices."""
# d={'nev':{2001:2.4,2001:2.9},
#    'ohio':{2000:1.5,2001:1.7,2002:3.6}}
# f=pd.DataFrame(d)
# print(f)
# print(f.T)          # T will transpose the data