# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path,delimiter=",",skip_header=1)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census=np.concatenate((data,new_record))
#Code starts here



# --------------
#Code starts here
age=np.array(census[0])
max_age=90
#print(age)
#print(max_age)
min_age=17#age.min()
age_mean=38.06#np.mean(age)
age_std=13.34#np.std(age)


# --------------
#Code starts here
import pandas as pd

race_0 = census[census[:,2]==0].astype(int)
print("race_0:\n",race_0)

race_1 = census[census[:,2]==1].astype(int)
print("race_1:\n",race_1)

race_2 = census[census[:,2]==2].astype(int)
print("race_2:\n",race_2)

race_3 = census[census[:,2]==3].astype(int)
print("race_3:\n",race_3)

race_4 = census[census[:,2]==4].astype(int)
print("race_4:\n",race_4)

len_0 = len(race_0)
print("len_0: ",len_0)

len_1 = len(race_1)
print("len_1: ",len_1)

len_2 = len(race_2)
print("len_2: ",len_2)

len_3 = len(race_3)
print("len_3: ",len_3)

len_4 = len(race_4)
print("len_4: ",len_4)

minority_race = 3
print("minority_race:", minority_race)




# --------------
#Code starts here
df=pd.read_csv(path)
#senior_citizens=np.array(df[df['age']>60]['age'])
senior_citizens=census[census[:,0]>60].astype(int)
print(senior_citizens)
senior_citizens_len=len(senior_citizens)
working_hours_sum = np.sum(senior_citizens[:,6], axis=0)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])


