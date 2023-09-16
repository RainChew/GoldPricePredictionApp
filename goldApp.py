import streamlit as st
import pandas as pd
import joblib

# Load the trained regression model (replace 'regression_model.pkl' with your model file)
model = joblib.load('svr.pkl')

loaded_selected_features = joblib.load('feature_selected.pkl')
# Streamlit web app
st.title('Gold Price Prediction App')

st.sidebar.header('Input Features')

# Create input widgets for relevant features
features = ['Open','High','Low','SP_low','OF_Open','OF_High','GDX_Close','GDX_Adj Close','SMA','Upper_band','Lower_band','DIF','MACD','RSI','Open_Close']

input_features = {}
for feature in features:
    input_features[feature] = st.sidebar.slider(feature, min_value=loaded_selected_features[feature].min(), max_value=loaded_selected_features[feature].max(), value=loaded_selected_features[feature].mean())

# Create a button to make predictions
if st.sidebar.button('Predict'):
    # Prepare input features as a DataFrame
    input_data = pd.DataFrame([input_features])
    
    # Make a prediction using the loaded model
    prediction = model.predict(input_data)
    st.write(f'Predicted MY Adj Close: {prediction[0]:.2f}')
