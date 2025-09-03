#import libraries
import numpy as np 
import joblib
import streamlit as st 

#loading the model
model=joblib.load('kmeans.pkl')

st.title('Customer Category Predictor')

income=st.number_input("Enter Annual Income (k$)",min_value=0, max_value=100000)
spending_score=st.number_input("Enter Spending Score(1-100)",min_value=0,max_value=100)

if st.button("Predict Category"):
   cluster= model.predict(np.array([[income,spending_score]]))[0]
   st.success(f"Customer belongs to **Category {cluster}** ")
