"""
This Module runs the streamlit Web App.
"""
import streamlit as st
import json
import requests

st.title(" Basic Calculator App")


# Taking User Inputs
option = st.selectbox(" Select your OPERATION",
                      (
                          'Addition', 'Subtraction',
                          'Multiplication', 'Division'
                          )
                      )

st.write(" Choose the Values for Operation")
x = st.slider("X", 0, 100, 10)
y = st.slider("Y", 0, 200, 20)

inputs = {"operation": option, "x": x, "y": y}

st.json(inputs)

if st.button('Calculate'):
    res = requests.post(url="http://127.0.0.1:8000/calculate", data=json.dumps(inputs))
    response_dict = json.loads(res.text)
    st.json(response_dict)
    st.subheader(f" Response from FastAPI is {res}")

