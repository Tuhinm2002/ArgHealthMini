import streamlit as st
import pickle
disease=pickle.load(open("disease.pkl","rb"))
Description=pickle.load(open("Description.pkl","rb"))
Precaution=pickle.load(open("Precaution.pkl","rb"))
def app():
    result=st.session_state["value"]
    st.write("## Predicted Disease : ")
    st.write(f"### {disease[int(result)]}")
    st.write(" ")
    st.write(" ")
    st.write(f"## Click Here to see the Description of : {disease[int(result)]}")
    button1=st.button("Description")
    if button1:
        st.write(f"##### {Description[int(result)]}")
    st.write(" ")
    st.write(" ")
    st.write(f"## Click Here to see the Precaution of : {disease[int(result)]}")
    button2=st.button("Precaution")
    j=1
    if button2:
        for i in(Precaution[int(result)]):
            st.write(f"##### {j}->{i}")
            j=j+1
