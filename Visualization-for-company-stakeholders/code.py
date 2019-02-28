# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=pd.read_csv(path)
loan_status=data['Loan_Status'].value_counts()

plt.plot(loan_status)


# --------------
#Code starts here




property_and_loan=data.groupby(by=['Property_Area','Loan_Status']).size().unstack()

property_and_loan.plot(kind='bar',stacked=False,rot=45)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.show()


# --------------
#Code starts here




education_and_loan=data.groupby(by=['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=False,rot=45)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.show()


# --------------
#Code starts here



graduate=data[data['Education']=='Graduate']
not_graduate=data[data['Education']=='Not Graduate']

graduate.plot(kind='density',label='Graduate')
not_graduate.plot(kind='density',label='Not Graduate')









#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3) = plt.subplots(nrows=3,ncols=1)

plt.plot(x=data['ApplicantIncome'],y=data['LoanAmount'],kind='scatter')
ax_1.set_title('Applicant Income')
plt.plot(x=data['CoapplicantIncome'],y=data['LoanAmount'],kind='scatter')
ax_2.set_title('Coapplicant Income')
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
plt.plot(x=data['TotalIncome'],y=data['LoanAmount'],kind='scatter')
ax_2.set_title('Coapplicant Income')
plt.show()


