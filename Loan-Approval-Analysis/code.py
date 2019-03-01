# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 

bank=pd.read_csv(path)
categorical_var=bank.select_dtypes(include='object')
print(categorical_var)
numerical_var=bank.select_dtypes(include='number')
print(numerical_var)
# code starts here






# code ends here


# --------------
# code starts here
bank.drop(columns=['Loan_ID'],inplace=True)
banks=bank
print(banks.columns)
print(path)
#print(type(banks))
#print(banks)
bank_mode=banks.mode()
print(banks.isnull().sum())
for column in banks.columns:
    banks[column]=banks[column].fillna(banks[column].mode()[0])
#banks=banks.fillna(bank_mode,inplace=True)
#bank_mode=banks.mode(axis='columns', numeric_only=True)

#banks.apply(lambda x: banks[x].fillna(banks[x].mode(),inplace=True),banks.columns)
print(banks)
#code ends here#


# --------------
# Code starts here

avg_loan_amount=banks.pivot_table(values=['LoanAmount'],index=['Gender', 'Married', 'Self_Employed'],aggfunc='mean')
avg_loan_amount


# code ends here



# --------------
# code starts here


tpY=banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')]
tpN=banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')]
loan_approved_se=tpY.count()[0]
loan_approved_nse=tpN.count()[0]
print(loan_approved_se)
print(loan_approved_nse)
Loan_Status=614
percentage_se=(loan_approved_se/Loan_Status)*100
percentage_nse=(loan_approved_nse/Loan_Status)*100

# code ends here


# --------------
# code starts here

loan_term= banks['Loan_Amount_Term'].apply(lambda x : x/12 )
big_loan_term = loan_term[loan_term >= 25].size
print(big_loan_term)


# code ends here


# --------------
# code starts here


loan_groupby=banks.groupby(by='Loan_Status')
loan_groupby[['ApplicantIncome','Credit_History']]


mean_values = loan_groupby.mean()


# code ends here


