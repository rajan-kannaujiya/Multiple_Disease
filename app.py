import os 
import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

# set page configurations
st.set_page_config(page_title="Health Guard",layout="wide")

# Getting the working directory of the .py file 
working_dir = os.path.dirname(os.path.abspath(__file__))

#Loading of the saved models

diabetes_model  = pickle.load(open('diabetes.pkl','rb'))
heart_model 	= pickle.load(open('heart.pkl','rb'))

# sidebar for navigation 
with st.sidebar:
	selected=option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],menu_icon= 'hospital-fill',icons = ['activity','heart','person'], default_index= 0)

if selected== 'Diabetes Prediction':
	st.title('Welcome to the Diabetes Prediction Model')
	col1,col2,col3= st.columns(3)
	glucose= col1.slider('Glucose Level',0,500,120)
	bp = col2.slider('Blood Pressure Level',0,200,120)
	skthic= col3.slider('Skin Thickness Value',0,100,20)
	insuline = col1.slider('Insulin Level',0,900,30)
	bmi=col2.slider('BMI Value',0.0,70.0,25.0)
	dpf = col3.slider('Diabetes Pedigree Function Value',0.0,2.5,0.5)
	age = col1.slider('Age of the Person',0,100,25)
	if st.button('Diabetes Test Result'):
		user_input = [glucose,bp,skthic,insuline,bmi,dpf,age]
		pred= diabetes_model.predict([user_input])[0]
		diab_diagnosis = 'The Person is Diabetic' if pred==1 else 'The Person is not Diabetic'
		st.success(diab_diagnosis)

# for Heart Disease Prediction
if selected == 'Heart Disease Prediction':
	st.title('Heart Disease Prediction using ML')
	col1,col2,col3= st.columns(3)
	

	age		= col1.slider('Age',0,100,50)
	gender 		= col2.radio('Gender',['Male','Female'])
	cp		= col3.selectbox('Chest Pain Types',['Type1','Type2','Type3','Type4'])
	trestbps 	= col1.slider('Resting Blood Pressure',0,200,120)
	chol 		= col2.slider('Serum Cholestrol in mg/dl',50,600,200)
	fbs 		= col3.radio('Fasting Blood Sugar >120 ',['Yes','No'])
	restecg 	= col1.radio('Resting Electrocardiograph Results',['Normal','Abnormal'])
	mhra		= col2.slider('Maximum Heart Rate Achieved',50,200,80)
	ang		= col3.radio('Exercise Induced Angine',['Yes','No'])
	oldpeak		= col1.slider('ST depression induced by exercise',0.0,10.0,1.0)
	slope		= col2.selectbox('Slope of the peakexercise ST segment',['Unsloping','Flat','Downsloping'])
	cf 		= col3.slider('Major vessels colored by flourosopy',0,4,0)
	thal		= col1.selectbox('Thalassemia',['Normal','Fixed Defect','Reversable Defect'])
	

	#mapping for categorical data
	cp_mapping	={'Type1':0,'Type2':1,'Type3':2,'Type4':3,}
	slope_mapping 	={'Unsloping':0,'Flat':1,'Downsloping':2}
	thal_mapping	={'Normal':0,'Fixed Defect':1,'Reversable Defect':2}


	if st.button('Heart Disease Test Result '):
		user_input = [age, 1 if gender=='Male' else 0,cp_mapping[cp],trestbps,chol,1 if fbs=='Yes' else 0, 1 if restecg=='Normal' else 0,mhra,1 if ang == 'Yes' else 0,oldpeak, 		slope_mapping[slope],cf,thal_mapping[thal] ]
		pred= heart_model.predict([user_input])[0]
		heart_diagnosis = 'The Person is Having Heart Disease' if pred==1 else 'The Person is does not have Heart Disease'
		st.success(heart_diagnosis)
# Add a footer using Markdown
st.markdown(""" --- © 2024 RajanKannaujiya. All rights reserved.""")
	


	
