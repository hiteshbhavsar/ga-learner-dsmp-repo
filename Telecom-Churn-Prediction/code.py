# --------------
import pandas as pd
from sklearn.model_selection import train_test_split
#path - Path of file 

# Code starts here


df=pd.read_csv(path)
X=df.drop(columns=['customerID','Churn'],axis='columns')
y=df['Churn']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)


# --------------
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Code starts here
X_train['TotalCharges']=X_train['TotalCharges'].replace(' ',np.NaN).astype(float)
X_test['TotalCharges']=X_test['TotalCharges'].replace(' ',np.NaN).astype(float)

X_train['TotalCharges'].fillna(X_train['TotalCharges'].mean(), inplace = True)
X_test['TotalCharges'].fillna(X_train['TotalCharges'].mean(), inplace = True)

le = LabelEncoder()
for col in X_train.select_dtypes(exclude = 'number').columns.tolist():
    X_train[col] = le.fit_transform(X_train[col])
    X_test[col] = le.fit_transform(X_test[col])

y_train = y_train.replace({'No':0, 'Yes':1})
y_test = y_test.replace({'No':0, 'Yes':1})



# --------------
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

# Code starts here
print(X_train)
print(X_test)
print(y_train)
print(y_test)

ada_model=AdaBoostClassifier(random_state=0)
ada_model.fit(X_train,y_train)
y_pred=ada_model.predict(X_test)
ada_score=accuracy_score(y_test,y_pred)
ada_cm=confusion_matrix(y_test,y_pred)
ada_cr=classification_report(y_test,y_pred)


# --------------
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV

#Parameter list
parameters={'learning_rate':[0.1,0.15,0.2,0.25,0.3],
            'max_depth':range(1,3)}

# Code starts here
xgb_model=XGBClassifier(random_state=0)
xgb_model.fit(X_train,y_train)
y_pred=xgb_model.predict(X_test)
xgb_score=accuracy_score(y_test,y_pred)
xgb_cm=confusion_matrix(y_test,y_pred)
xgb_cr=classification_report(y_test,y_pred)

clf_model=GridSearchCV(estimator=xgb_model,param_grid=parameters)
clf_model.fit(X_train,y_train)
y_pred=clf_model.predict(X_test)
clf_score=accuracy_score(y_pred,y_test)
clf_cm=confusion_matrix(y_test,y_pred)
clf_cr=classification_report(y_test,y_pred)
print(xgb_cr)
print(clf_cr)



