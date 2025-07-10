import streamlit as st
from prediction_helper import predict

# ---------------------- App Configuration -----------------------
st.set_page_config(
    page_title="Health Insurance Predictor BY ANMOL JAIN",
    layout="wide",
    page_icon="🩺"
)

# ---------------------- Theme Toggle ----------------------------
theme = st.selectbox("🌓 Select Theme", ["Light", "Dark"], index=1)

# CSS Styling
def apply_theme(mode):
    if mode == "Dark":
        st.markdown("""
        <style>
        .stApp {
            background-color: #121212;
            color: #f5f5f5;
        }
        .stButton>button {
            background-color: #1E88E5;
            color: white;
            border-radius: 8px;
            font-weight: 600;
        }
        .stSelectbox label, .stNumberInput label, .stRadio label {
            font-weight: bold;
        }
        .css-10trblm, .css-1v0mbdj {
            font-weight: 700 !important;
            color: #90CAF9 !important;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        .stApp {
            background-color: #ffffff;
            color: black;
        }
        .stButton>button {
            background-color: #0D47A1;
            color: white;
            border-radius: 8px;
            font-weight: 600;
        }
        .stSelectbox label, .stNumberInput label, .stRadio label {
            font-weight: bold;
        }
        .css-10trblm, .css-1v0mbdj {
            font-weight: 700 !important;
            color: #0D47A1 !important;
        }
        </style>
        """, unsafe_allow_html=True)

apply_theme(theme)

# ---------------------- Title & Branding ------------------------
st.markdown("<h1 style='text-align: center; color:#29B6F6;'>🩺 Health Insurance Cost Predictor</h1>", unsafe_allow_html=True)
st.markdown("<hr style='margin-top:-10px;'>", unsafe_allow_html=True)

# ---------------------- Input Options ---------------------------
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease',
        'Diabetes & Thyroid', 'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# ---------------------- Section: Personal Info ------------------
st.markdown("### 👤 Personal & Demographic Information")
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age', 18, 100, step=1, help="Enter your current age")
        gender = st.selectbox('Gender', categorical_options['Gender'])
    with col2:
        marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
        employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])
    with col3:
        number_of_dependants = st.number_input('Number of Dependants', 0, 20, help="How many people depend on you")
        region = st.selectbox('Region', categorical_options['Region'])

# ---------------------- Section: Medical -------------------------
st.markdown("### 🧬 Lifestyle & Medical Details")
with st.container():
    col4, col5, col6 = st.columns(3)
    with col4:
        bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])
        smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
    with col5:
        medical_history = st.selectbox('Medical History', categorical_options['Medical History'])
    with col6:
        income_lakhs = st.number_input('Annual Income (in Lakhs)', 0, 200)
        genetical_risk = st.slider('Genetical Risk (0 = Low, 5 = High)', 0, 5)

# ---------------------- Section: Plan ----------------------------
st.markdown("### 📄 Insurance Plan")
insurance_plan = st.radio("Select Plan Type", categorical_options['Insurance Plan'], horizontal=True)

# ---------------------- Input Dictionary -------------------------
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# ---------------------- Prediction Button ------------------------
st.markdown("----")
with st.container():
    center_col = st.columns(3)[1]
    with center_col:
        if st.button("🔍 Predict Insurance Cost"):
            prediction = predict(input_dict)
            st.success(f"💰 Estimated Insurance Cost: ₹{prediction:,.2f}")

