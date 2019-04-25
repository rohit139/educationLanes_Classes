# Last amended: 18th April, 2019
# Myfolder: D:\data\OneDrive\Documents\black_friday

# 1.0 Clear memory and all variables
%reset -f

# 1.1 Import numpy As np
import numpy as np

# 1.2 Import pandas As pd
import pandas as pd

# 1.3 Import pyplot module of matplotlib as plt
import matplotlib.pyplot as plt
%matplotlib inline

# 1.4 Import seaborn As sns
import seaborn as sns

# 1.5 Import os for Operating System related work
import os

# 1.6 Use 'os' to change your working dir to where your
#     black friday csv file is placed
os.chdir("C:\\Users\\tgyk\\Downloads\\Python\\EdLanes_Homework")
  #to check the current working directory
os.getcwd()


# 1.7 List all files in your current working folder
os.listdir(os.curdir)


# 1.8 Count the number of files in your current working folder
print (len(os.listdir(os.getcwd())))
 # Ans:6


# 1.9  Read the dataset file 'BlackFriday.csv' or
#      black-friday.zip into a variable 'df'

df = pd.read_csv("blackfriday.csv")
    #confirming the correct load
df.head(5) #Succes



### Exploration of data

# 2.0 Check the data type of 'df'. Is it
#     a pandas DataFrame or a Pandas Series?
print(type(df))
  # Ans: pandas.core.frame.DataFrame


# 2.1 How much memory does the dataframe 'df' uses?
#     Hint: Use: .memory_usage()
print (df.memory_usage())
# =============================================================================
# #Ans:
# Index                              80
# User_ID                       4300616
# Product_ID                    4300616
# Gender                        4300616
# Age                           4300616
# Occupation                    4300616
# City_Category                 4300616
# Stay_In_Current_City_Years    4300616
# Marital_Status                4300616
# Product_Category_1            4300616
# Product_Category_2            4300616
# Product_Category_3            4300616
# Purchase                      4300616
# dtype: int64
# 
# =============================================================================

# 2.2 What is the shape of df
#     How many rows and columns does it have?
df.shape
print ("Rows :",df.shape[0])  #Ans: Rows : 537577
print ("Columns :",df.shape[1])  #Ans: Columns : 12


# 2.3 What are the column names of df?
df.columns
#    Ans: Index(['User_ID', 'Product_ID', 'Gender', 'Age', 'Occupation', 'City_Category',
#       'Stay_In_Current_City_Years', 'Marital_Status', 'Product_Category_1',
#       'Product_Category_2', 'Product_Category_3', 'Purchase'],
#      dtype='object')


# 2.4 Get columns names as an array object
#     Hint: Use attribute: .values

dataColumns=df.columns.values
print(dataColumns)
#    ans: ['User_ID' 'Product_ID' 'Gender' 'Age' 'Occupation' 'City_Category'
# 'Stay_In_Current_City_Years' 'Marital_Status' 'Product_Category_1'
# 'Product_Category_2' 'Product_Category_3' 'Purchase']


# 2.5 Print few five rows of DataFrame
df.head(5)


# 2.6 Print last five rows of DataFrame
df.tail(5)


# 2.7 Check data types of each column of df
df.dtypes
# =============================================================================
# User_ID                         int64
# Product_ID                     object
# Gender                         object
# Age                            object
# Occupation                      int64
# City_Category                  object
# Stay_In_Current_City_Years     object
# Marital_Status                  int64
# Product_Category_1              int64
# Product_Category_2            float64
# Product_Category_3            float64
# Purchase                        int64
# dtype: object
# =============================================================================



# 2.8 User_ID should be 'object' and not int64
#     Make dtype of User_ID to 'object'
df[['User_ID']]=df[['User_ID']].astype(object)
df['User_ID'].dtype.kind



# 2.9 Summarise datatypes by counts of dtypes
#     ie how many are 'object', 'int64' etc
#     Hint: Use method value_counts()
df.dtypes.value_counts()
# =============================================================================
# object     6
# int64      4
# float64    2
# dtype: int64
# =============================================================================



# 3.0 Give a statistical summary of dataframe df
#     In the summary include numeric and categorical (object)
#     datatypes also:
df.describe(include = 'all')
# =============================================================================
# User_ID Product_ID  Gender     Age    Occupation City_Category  \
# count    537577.0     537577  537577  537577  537577.00000        537577   
# unique     5891.0       3623       2       7           NaN             3   
# top     1001680.0  P00265242       M   26-35           NaN             B   
# freq       1025.0       1858  405380  214690           NaN        226493   
# mean          NaN        NaN     NaN     NaN       8.08271           NaN   
# std           NaN        NaN     NaN     NaN       6.52412           NaN   
# min           NaN        NaN     NaN     NaN       0.00000           NaN   
# 25%           NaN        NaN     NaN     NaN       2.00000           NaN   
# 50%           NaN        NaN     NaN     NaN       7.00000           NaN   
# 75%           NaN        NaN     NaN     NaN      14.00000           NaN   
# max           NaN        NaN     NaN     NaN      20.00000           NaN   
# 
#        Stay_In_Current_City_Years  Marital_Status  Product_Category_1  \
# count                      537577   537577.000000       537577.000000   
# unique                          5             NaN                 NaN   
# top                             1             NaN                 NaN   
# freq                       189192             NaN                 NaN   
# mean                          NaN        0.408797            5.295546   
# std                           NaN        0.491612            3.750701   
# min                           NaN        0.000000            1.000000   
# 25%                           NaN        0.000000            1.000000   
# 50%                           NaN        0.000000            5.000000   
# 75%                           NaN        1.000000            8.000000   
# max                           NaN        1.000000           18.000000   
# 
#         Product_Category_2  Product_Category_3       Purchase  
# count        370591.000000       164278.000000  537577.000000  
# unique                 NaN                 NaN            NaN  
# top                    NaN                 NaN            NaN  
# freq                   NaN                 NaN            NaN  
# mean              9.842144           12.669840    9333.859853  
# std               5.087259            4.124341    4981.022133  
# min               2.000000            3.000000     185.000000  
# 25%               5.000000            9.000000    5866.000000  
# 50%               9.000000           14.000000    8062.000000  
# 75%              15.000000           16.000000   12073.000000  
# max              18.000000           18.000000   23961.000000 
# 
# =============================================================================


# 3.1 Extract just two columns from the dataset:
#     User_ID and Product_ID and also access its
#     rwos from row 10 to 20
df.iloc[9:20,0:2]


# 3.2 Which columns in the dataset have null values
df.isnull().sum(axis = 0)
# =============================================================================
# Product_Category_2            166986
# Product_Category_3            373299
# 
# =============================================================================


# 3.3 How many and which all Age (ie age-groups) exist?
#     Hint: Use value_counts()
df.Age.value_counts()
# =============================================================================
# 26-35    214690
# 36-45    107499
# 18-25     97634
# 46-50     44526
# 51-55     37618
# 55+       20903
# 0-17      14707
# =============================================================================

# 3.4  How many and which all kinds of Occupation exist?
df.Occupation.value_counts()
# =============================================================================
# 4     70862
# 0     68120
# 7     57806
# 1     45971
# 17    39090
# 20    32910
# 12    30423
# 14    26712
# 2     25845
# 16    24790
# 6     19822
# 3     17366
# 10    12623
# 5     11985
# 15    11812
# 11    11338
# 19     8352
# 13     7548
# 18     6525
# 9      6153
# 8      1524
# =============================================================================


# 3.5 How many kinds of City_Category exist?
df.City_Category.unique()
#array(['A', 'C', 'B'], dtype=object)


# 3.6 How many types of Products (ie Product_ID) exist?
len(df["Product_ID"].unique())
#Ans: 3623


# 3.7 How many types of Product_Category_1,
#     Product_Category_2 and Product_Category_3 exist?
print(len(df["Product_Category_1"].unique()))
#Ans: 18
print(len(df["Product_Category_2"].unique()))
#Ans: 18
print(len(df["Product_Category_3"].unique()))
#Ans: 16



#3.8  Which top-10 User_ID occur most frequently
#     Hint: Use: value_counts(), sort_values()
#                and head()
df.User_ID.value_counts().sort_values(ascending=False).head(10)
# =============================================================================
# 1001680    1025
# 1004277     978
# 1001941     898
# 1001181     861
# 1000889     822
# 1003618     766
# 1001150     752
# 1001015     739
# 1002909     717
# 1001449     714
# Name: User_ID, dtype: int64
# =============================================================================


# 3.9 Make a barplot of frequency of top-10 User_IDs
#     that occur most frequently on Black Friday
#     Can you order the graph either in
#     decreasing/increasing order of frequency
uids=df.User_ID.value_counts().sort_values(ascending=False).head(10).index.values
frequency=df.User_ID.value_counts().sort_values(ascending=False).head(10).values
cnt=1,2,3,4,5,6,7,8,9,10

plt.bar(cnt,frequency,align='center', alpha=0.5)
plt.xlabel("User")
plt.ylabel("frequecy of shoping")
plt.xticks(cnt,uids)

plt.show()



#### Group and summarise data

# 4.0 Find average purchases ('Purchase') per User_ID
#     Hint: Use groupby(), sort_values() and head()

df.head()
df.groupby('User_ID').Purchase.mean().sort_values(ascending=False).head(20).index.values


# 4.1 Refer answer to 4.0
#     Plot a barchart of User_IDs average purchases wise

purchase=df.groupby('User_ID').Purchase.mean().sort_values(ascending=False).head(20)
uids=df.groupby('User_ID').Purchase.mean().sort_values(ascending=False).head(20).index.values

unit=range(20)

#len(uids)

plt.figure(figsize=(10,6))
plt.bar(unit,purchase)
plt.xlabel("Unser IDs")
plt.ylabel("average purchase")

plt.xticks(unit,uids)

plt.show()




# 4.2 Product_ID wise average 'Purchase'?
df.head()
df.groupby('Product_ID').Purchase.mean().sort_values(ascending=False)




# 4.3 Plot top-10 Product_IDs most purchased on an average
purchase=df.groupby('Product_ID').Purchase.mean().sort_values(ascending=False).head(10)
pids=df.groupby('Product_ID').Purchase.mean().sort_values(ascending=False).head(10).index.values

unit=range(10)

#len(uids)

plt.figure(figsize=(10,6))
plt.bar(unit,purchase)
plt.xlabel("Product IDs")
plt.ylabel("average purchase")

plt.xticks(unit,pids)

plt.show()




# 4.4 Product_Category_1 wise mean 'Purchase'?
df.groupby('Product_Category_1').Purchase.mean().sort_values(ascending=False)


# 4.5 Plot top-10 Product_Category_1 most purchased on an average
purchase=df.groupby('Product_Category_1').Purchase.mean().sort_values(ascending=False).head(10)
pids=df.groupby('Product_Category_1').Purchase.mean().sort_values(ascending=False).head(10).index.values

unit=range(10)

#len(uids)

plt.figure(figsize=(10,6))
plt.bar(unit,purchase)
plt.xlabel("Product_Category_1")
plt.ylabel("average purchase")

plt.xticks(unit,pids)

plt.show()



# 4.6 Product_Category_2 wise mean 'Purchase'?
df.groupby('Product_Category_2').Purchase.mean().sort_values(ascending=False)



# 4.7 Plot top-10 Product_Category_2 most purchased on an average
purchase=df.groupby('Product_Category_2').Purchase.mean().sort_values(ascending=False).head(10)
pids=df.groupby('Product_Category_2').Purchase.mean().sort_values(ascending=False).head(10).index.values

unit=range(10)

#len(uids)

plt.figure(figsize=(10,6))
plt.bar(unit,purchase)
plt.xlabel("Product_Category_2")
plt.ylabel("average purchase")

plt.xticks(unit,pids)

plt.show()



# 4.8 Product_Category_3 wise mean 'Purchase'?
df.groupby('Product_Category_3').Purchase.mean().sort_values(ascending=False)


# 4.9 Plot top-10 Product_Category_3s most purchased on an average

purchase=df.groupby('Product_Category_3').Purchase.mean().sort_values(ascending=False).head(10)
pids=df.groupby('Product_Category_3').Purchase.mean().sort_values(ascending=False).head(10).index.values

unit=range(10)

#len(uids)

plt.figure(figsize=(10,6))
plt.bar(unit,purchase)
plt.xlabel("Product_Category_3")
plt.ylabel("average purchase")

plt.xticks(unit,pids)

plt.show()


# 5.0 Which Product_Category_1 is more popular in which City_Category?
df.groupby('City_Category').Product_Category_1.max()
# =============================================================================
# #ANS:
# City_Category
# A    18
# B    18
# C    18
# Name: Product_Category_1, dtype: int64
# =============================================================================


# 5.1 Get City_Category wise average 'Purchase'
df.groupby('City_Category').Purchase.mean()

# =============================================================================
# City_Category
# A    8958.011014
# B    9198.657848
# C    9844.441855
# Name: Purchase, dtype: float64
# =============================================================================


# 5.2 Get Age wise average 'Purchase'?
df.groupby('Age').Purchase.mean()
# =============================================================================
# Age
# 0-17     9020.126878
# 18-25    9235.197575
# 26-35    9314.588970
# 36-45    9401.478758
# 46-50    9284.872277
# 51-55    9620.616620
# 55+      9453.898579
# Name: Purchase, dtype: float64
# =============================================================================


# 5.3 Get City_Category wise and Age wise average 'Purchase'
df.groupby(['City_Category','Age']).Purchase.mean()
# =============================================================================
# City_Category  Age  
# A              0-17      8673.295555
#                18-25     8886.956078
#                26-35     8990.238064
#                36-45     9041.641611
#                46-50     8386.424936
#                51-55     9575.454012
#                55+       8587.106877
# B              0-17      8985.208396
#                18-25     9069.532164
#                26-35     9199.148351
#                36-45     9150.322154
#                46-50     9297.089648
#                51-55     9393.971724
#                55+       9886.257757
# C              0-17      9171.916354
#                18-25     9819.690145
#                26-35     9952.538704
#                36-45    10008.983828
#                46-50     9661.676321
#                51-55     9917.586464
#                55+       9522.626968
# Name: Purchase, dtype: float64
# 
# =============================================================================


#### Relationships between two categories

# 6.0 Is there any relationship between City_Category and Age?
#     Ref: https://machinelearningmastery.com/chi-squared-test-for-machine-learning/
from scipy.stats import chi2_contingency
test_df=pd.crosstab(df.City_Category,df.Age)
chi2_contingency(test_df)
# =============================================================================
# (21658.51596036734,
#  0.0,
#  12,
#  array([[ 3956.997911  , 26268.95587423, 57763.50591636, 28923.18749128,
#          11979.96117393, 10121.32640347,  5624.06522973],
#         [ 6196.38219455, 41135.3490979 , 90453.61347305, 45291.69031971,
#          18759.781981  , 15849.28982081,  8806.89311299],
#         [ 4553.61989445, 30229.69502788, 66472.88061059, 33284.12218901,
#          13786.25684507, 11647.38377572,  6472.04165729]]))
# 
# =============================================================================



# 6.1  How confident would you want to be about the existence of any relationship?
#      95% or 90% or 99%......
confidence_level = 0.95         # 95% confident
level_of_significance = 1- confidence_level

# 6.2 Create a cross-table between two categorical variables
table = pd.crosstab(df.City_Category,df.Age)
table
# =============================================================================
# Age            0-17  18-25  26-35  36-45  46-50  51-55    55+
# City_Category                                                
# A              2497  27025  72048  26142   7467   5969   3490
# B              5288  42470  89767  46605  19900  17435   5028
# C              6922  28139  52875  34752  17159  14214  12385
# =============================================================================


# 6.3 Apply chi-square test of independence and get p_value
#_, p_value, _, _ = chi2_contingency(table)

chi2,p,dof,expected=chi2_contingency(table)
print("P value: ", p)
print("Chi2 score: ", chi2)
print("dof value: ", dof)
print("expected values: ", expected)
# =============================================================================
# P value:  0.0
# Chi2 score:  21658.51596036734
# dof value:  12
# expected values:  [[ 3956.997911   26268.95587423 57763.50591636 28923.18749128
#   11979.96117393 10121.32640347  5624.06522973]
#  [ 6196.38219455 41135.3490979  90453.61347305 45291.69031971
#   18759.781981   15849.28982081  8806.89311299]
#  [ 4553.61989445 30229.69502788 66472.88061059 33284.12218901
#   13786.25684507 11647.38377572  6472.04165729]]
# =============================================================================



# 6.4 Now examine p_value
if p <= level_of_significance:
	print("Categorical variables have relationships")
else:
	print("Categorical variables have no relationships")


# 7.0 Similarly examine if there is any relationship between Age and Occupation?
table = pd.crosstab(df.Occupation,df.Age)
table
chi2,p,dof,expected=chi2_contingency(table)
print("P value: ", p)
print("Chi2 score: ", chi2)
print("dof value: ", dof)
#print("expected values: ", expected)
# =============================================================================
# P value:  0.0
# Chi2 score:  581712.9936323236
# dof value:  120
# =============================================================================



# 7.1 And also examine if there is any Gender  and Marital_Status?
table = pd.crosstab(df.Marital_Status,df.Gender)
table
chi2,p,dof,expected=chi2_contingency(table)
print("P value: ", p)
print("Chi2 score: ", chi2)
print("dof value: ", dof)
#print("expected values: ", expected)
# =============================================================================
# P value:  2.8078724890395355e-14
# Chi2 score:  57.86465518457894
# dof value:  1
# =============================================================================



######################
