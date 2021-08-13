import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title(" Water Potability **Estimation**")

st.markdown("""
	Access to safe drinking-water is essential to health, a basic human right and a component of effective policy for health protection.
	This is important as a health and development issue at a national, regional and local level. In some regions, it has been shown that investments in water supply and sanitation can yield a net economic benefit,
	since the reductions in adverse health effects and health care costs outweigh the costs of undertaking the interventions.
	""")

st.subheader("sample values for the input")
df=pd.read_csv("example.csv")
df
#df_example=df.iloc[df['ph']==6.007427,['Organic_carbon','Conductivity','Hardness']]
#df_example=df.iloc[0,1:]
#df_example

if st.checkbox("Show orignal dataframe"):
	dataframe=pd.read_csv("water_potability.csv")
	dataframe

##Sidebar

st.sidebar.title("Select your Input  Values")

uploaded_file=st.sidebar.file_uploader("Upload your csv file in the same input as the example csv file",type=["csv"])

if uploaded_file is not None:
	input_params=pd.read_csv(uploaded_file)

else:
	Carbon=st.sidebar.slider("Organic Carbon value",2.1,28.3,12.5)
	Conductivity=st.sidebar.slider("Conductivity value",181.4,753.2,442.85)
	Hardness=st.sidebar.slider("Hardness value",47.432,323.3,158.2)
	dict_values={"Carbon":Carbon,"Conductivity":Conductivity,"Hardness":Hardness}
	features=pd.DataFrame(dict_values,index=[0])
	input_params=features
	




st.subheader("user input fields")

if uploaded_file is not None:
	st.write(input_params)
else:
	st.write(input_params)

load_clf=pickle.load(open('water.pkl','rb'))

prediction=load_clf.predict(input_params)
st.subheader("The Prediction is")
st.write(prediction[0])

if(prediction[0]==1):
	st.subheader("The water is safe to drink")
else:
	st.subheader("The water is not safe to drink")
