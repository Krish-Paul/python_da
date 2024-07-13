

import pandas as pd

ser1=pd.Series(data=[1,2,3,4,5],
               index=['a','b','c','d','e'])
ser1

ser2=pd.Series(dic1)
ser2

ser1['a']

ser1[0:3]

ser1+ser2

np.mean(ser1)

dic3 = {"name" : ["Joe","Bob","Frans"],
           "age" : np.array([10,15,20]),
           "weight" : (75,123,239),
           "height" : pd.Series([4.5, 5, 6.1],
                                index=["Joe","Bob","Frans"]),
           "siblings" : 1,
           "gender" : "M"}
df = pd.DataFrame(dic3)
df

df["weight"]

df.weight

del df["weight"]

df["iq"]=[130,100,123]
df

df["married"]=False
df

df.loc["Joe"]

df.loc["Joe","iq"]

df["college"]=pd.Series(["IIT"],index=["Joe"])
df

df.loc["Joe":"Bob","iq":"college"]

df.iloc[0]

df.iloc[0,3]

bool_index=[True,False,True]
df[bool_index]

bool_index=df["age"]>=15
df[bool_index]

df[df["age"]>12]
