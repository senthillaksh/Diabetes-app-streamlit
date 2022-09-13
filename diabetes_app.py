
import pickle
import streamlit as st

# loading the saved models

diabetes_model = pickle.load(open('/content/drive/MyDrive/Diabetes Prediction /diabetes_prediction.pkl', 'rb'))

#creating function for prediction

def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age):

    preg = int(Pregnancies)
    glucose = float(Glucose)
    bp = float(BloodPressure)
    st = float(SkinThickness)
    insulin = float(Insulin)
    bmi = float(BMI)
    dpf = float(DPF)
    age = int(Age)

    x = [[preg, glucose, bp, st, insulin, bmi, dpf, age]]
    prediction =  diabetes_model.predict(x)

    if (prediction[0] == 1):
       return "Sorry! You have diabetes."
    else:
       return "Great! You don't have diabetes."
           
def main():
  
  # giving a title
  st.title("Diabetes Prediction")

  # getting the input data for the user
  Pregnancies = st.text_input("Number of Pregnancies")
  Glucose = st.text_input("Glucose Level(mg/dL) eg. 90")
  BloodPressure = st.text_input("Blood Pressure(mmHg) eg. 80")
  SkinThickness = st.text_input("Skin Thickness(mm) eg. 20")
  Insulin = st.text_input("Insulin Level(IU/mL) eg. 80")
  BMI = st.text_input("BMI value eg. 23.1")
  DPF = st.text_input("DiabetesPedigreeFunction eg. 0.52")
  Age = st.text_input("Age of the Person")

  # code for prediction
  diagnosis = ''

  #creating a button for prediction
  if st.button('Diabetes Test Result'):
    diagnosis = predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age)

  st.success(diagnosis)   

if __name__ == '__main__':
  main()
  
