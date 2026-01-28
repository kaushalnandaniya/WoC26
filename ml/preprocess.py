import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

def add_salary_column(df):
    np.random.seed(42)
    
    df['Salary'] = (df['CGPA'] * 50000) + (df['IQ'] * 2000) + np.random.normal(0, 10000, len(df))
    
    df['Salary'] = df.apply(lambda x: max(0, x['Salary']), axis=1)
    
    if df['Placement'].dtype == 'object':
         df.loc[df['Placement'] == "No", 'Salary'] = 0
    else:
         df.loc[df['Placement'] == 0, 'Salary'] = 0
    
    return df

def preprocess_data(df, train=True, label_encoders=None):
    
    df = df.copy()
    
    if "College_ID" in df.columns:
        df = df.drop(columns="College_ID")
    
    encoders = {} if label_encoders is None else label_encoders
    
    cat_cols = ["Internship_Experience"]
    
    if "Placement" in df.columns:
        if df["Placement"].dtype == 'object':
             df["Placement"] = df["Placement"].map({"Yes": 1, "No": 0})
    
    for col in cat_cols:
        if col in df.columns:
            if train:
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col])
                encoders[col] = le
            else:
                le = encoders.get(col)
                if le:
                    try:
                        df[col] = le.transform(df[col])
                    except:
                        pass
    
    return df, encoders
