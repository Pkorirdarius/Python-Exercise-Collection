#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score


# In[2]:


# specify the file_path
file_path = './Electric_cars_dataset.csv'

cars_df = pd.read_csv(file_path)
cars_df.head()


# In[3]:


# general info about the dataSet
cars_df.info()


# In[4]:


cars_df.describe()


# In[5]:


# Genrating a pandas profiling report
profile_report = ProfileReport(cars_df,title="Electic_cars profiling report",explorative=True)
profile_path = 'Electric_cars.html'
profile_report.to_file(profile_path)
print(f"\n Profile report saved to {profile_path}")


# In[6]:


# According to the profile report there are missing values,skewedness in specific 2 columns
cars_df.isnull().sum()


# In[7]:


# checking for duplicated values there are no duplicates according to the report
cars_df.duplicated().sum()


# In[8]:


# Dropping rows with missing essential values: Model Year, Make, Model
df_cleaned = cars_df.dropna(subset=["Model Year", "Make", "Model","Vehicle Location"])

# Filling missing ZIP Code and Legislative District with mode
df_cleaned["ZIP Code"].fillna(df_cleaned["ZIP Code"].mode()[0], inplace=True)
df_cleaned["Legislative District"].fillna(df_cleaned["Legislative District"].mode()[0], inplace=True)

# Filling categorical columns with "Unknown"
categorical_cols = ["County", "City", "State", "Electric Utility"]
df_cleaned[categorical_cols] = df_cleaned[categorical_cols].fillna("Unknown")

# Converting Expected Price ($1k) to numeric
df_cleaned["Expected Price ($1k)"] = pd.to_numeric(df_cleaned["Expected Price ($1k)"], errors="coerce")

# Converting ZIP Code and Model Year to integers
df_cleaned["ZIP Code"] = df_cleaned["ZIP Code"].astype(int)
df_cleaned["Model Year"] = df_cleaned["Model Year"].astype(int)
df_cleaned.info(), df_cleaned.isnull().sum()


# In[9]:


# Dropping unnecessary columns
df_cleaned.drop(columns=["ID", "VIN (1-10)", "DOL Vehicle ID", "Vehicle Location"], inplace=True)

# Handling outliers using IQR method for Base MSRP and Electric Range
Q1 = df_cleaned[["Base MSRP", "Electric Range"]].quantile(0.25)
Q3 = df_cleaned[["Base MSRP", "Electric Range"]].quantile(0.75)
IQR = Q3 - Q1

# Define acceptable range for values
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter dataset to remove extreme outliers
df_cleaned = df_cleaned[
    (df_cleaned["Base MSRP"] >= lower_bound["Base MSRP"]) & (df_cleaned["Base MSRP"] <= upper_bound["Base MSRP"]) &
    (df_cleaned["Electric Range"] >= lower_bound["Electric Range"]) & (df_cleaned["Electric Range"] <= upper_bound["Electric Range"])
]


# In[10]:


# Encoding categorical values
encoder = LabelEncoder()
categorical_features = ["County", "City", "State", "Make", "Model", "Electric Vehicle Type",
                        "Clean Alternative Fuel Vehicle (CAFV) Eligibility", "Electric Utility"]
for col in categorical_features:
    df_cleaned[col] = encoder.fit_transform(df_cleaned[col])
df_cleaned


# In[21]:


# Identifying the targets and features
X = df_cleaned.drop(columns=["Expected Price ($1k)"])
y = df_cleaned["Expected Price ($1k)"]
# splitting our data into training and testing 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
# Standardizing features for SVM
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# Training the model using rbf
svm_model = SVR(kernel="rbf") 
svm_model.fit(X_train_scaled, y_train)


# In[23]:


# testing our model
y_pred =svm_model.predict(X_test_scaled)
y_pred
y_pred.shape


# In[29]:


mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
mae,rmse,mse,r2


# In[ ]:


# Model evaliuation using mean absolute error,mean squared error and r2 score
# since the model  R² is close to 1, the model explains most of the variance in price.
# MAE is low, the model makes small average errors.
# The RMSE is slightly higher than the MAE hence the model makes some errors
# since mse is squared, it magnifies the effect of larger errors.


# In[ ]:


# How to improve the model
# Check if important predictors are missing (e.g., mileage).
# Instead of Label Encoding, try One-Hot Encoding or Target Encoding for better representation.
#Using Hyperparameter tuning for SVR: C,Gamma

