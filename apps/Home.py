import streamlit as st
import pickle
import numpy as np

def app():
	st.markdown("#       ArgHealthMini")
	st.write(" ")
	st.write(" ")
	st.write(" ")
	st.write(" ")

	Precaution=pickle.load(open("Precaution.pkl","rb"))
	Description=pickle.load(open("Description.pkl","rb"))
	Severity=pickle.load(open("Severity_degree.pkl","rb"))
	Model=pickle.load(open("Model.pkl","rb"))

	Symptom=[]

	text1=st.text_input("Enter problem",key=1)
	text2=st.text_input("Enter problem",key=2)
	text3=st.text_input("Enter problem",key=3)
	text4=st.text_input("Enter problem",key=4)
	st.write("## Any other problem")
	select1 = st.selectbox("Select to continue", ("No", "Yes"), key=0)
	if text1 != "":
		try:
			input1=Severity[text1]
		except:
			input1=140
		Symptom.append(input1)
	if text2 != "":
		try:
			input2=Severity[text2]
		except:
			input2=140
		Symptom.append(input2)
	if text3 != "":
		try:
			input3=Severity[text3]
		except:
			input3=140
		Symptom.append(input3)
	if text4 != "":
		try:
			input4=Severity[text4]
		except:
			input4=140
		Symptom.append(input4)
	if select1=="Yes":
		text5=st.text_input("Enter problem",key=5)
		if text5 != "":
			try:
				input5=Severity[text5]
			except:
				input5=140
			Symptom.append(input5)
			for i in range(12):
				Symptom.append(140)
		# underscores to be removed
	for i in range(17-len(Symptom)):
		Symptom.append(140)
	Symptom_main=np.asarray([Symptom])
	if len(Symptom) !=0:
		y_pred=Model.predict(Symptom_main)
		st.session_state["value"]=y_pred

