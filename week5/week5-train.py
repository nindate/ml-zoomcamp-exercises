#!/usr/bin/env python
# coding: utf-8

# #### Cleaned up code for training model for churn prediction

#Import libraries

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import KFold
import pickle


#Parameters
n_splits = 5
C=1.0
output_file = f'model_C={C}.bin'


#Load and prepare data
print("Loading data")
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Preparing data")
df.columns = df.columns.str.lower().str.replace(' ','_')

categorical_cols = list(df.dtypes[df.dtypes == 'object'].index)
for c in categorical_cols:
    df[c] = df[c].str.lower().str.replace(' ','_')

df['totalcharges'] = pd.to_numeric(df['totalcharges'],errors='coerce')
df['totalcharges'] = df['totalcharges'].fillna(0)

df['churn'] = (df['churn'] == 'yes').astype(int)


numerical_cols = [ 'tenure', 'monthlycharges', 'totalcharges']

categorical_cols = [
    'gender',
    'seniorcitizen',
    'partner',
    'dependents',
    'phoneservice',
    'multiplelines',
    'internetservice',
    'onlinesecurity',
    'onlinebackup',
    'deviceprotection',
    'techsupport',
    'streamingtv',
    'streamingmovies',
    'contract',
    'paperlessbilling',
    'paymentmethod'
]


df_full_train,df_test = train_test_split(df,test_size=0.2,random_state=1)


def train(df_train, y_train, C=1.0):
    dicts = df_train[categorical_cols + numerical_cols].to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)

    model = LogisticRegression(C=C, max_iter=1000)
    model.fit(X_train, y_train)
    
    return dv, model


def predict(df, dv, model):
    dicts = df[categorical_cols + numerical_cols].to_dict(orient='records')

    X = dv.transform(dicts)
    
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred


kfold = KFold(n_splits=n_splits, shuffle=True, random_state=1)

scores = []
fold = 0

print("Training model")
for train_idx, val_idx in kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]

    y_train = df_train.churn.values
    y_val = df_val.churn.values

    dv, model = train(df_train, y_train, C=C)
    
    y_pred = predict(df_val, dv, model)

    auc = roc_auc_score(y_val, y_pred)
    scores.append(auc)
    print(f"AUC for fold-{fold} is {auc}")
    fold = fold + 1

print(f'C={C}, mean_auc={np.mean(scores)}, std={np.std(scores)}')


print("Training final model")
dv, model = train(df_full_train, df_full_train['churn'].values, C=C)

y_test = df_test['churn'].values
y_pred = predict(df_test, dv, model)

auc = roc_auc_score(y_test, y_pred)
print(f"AUC on final model is {auc}")


# Save model
print(f"Saving model to {output_file}")
with open(output_file,'wb') as f_out:
    pickle.dump((dv,model),f_out)
