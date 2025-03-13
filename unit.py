import streamlit as st
st.markdown(
    """ 
    <style>
    body{
    background-color:rgb(108, 21, 167);
    color: white;
    }
    .stApp{
    background: linear gradient(135deg, #bcbcbc, #cfe2f3);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 10px 30px rgba(0,0,0,03);
    }
    h1{
    text-aling: center ;
    font-size: 36px;
    color: white;
    }
    .stButton>button{
    background: rgb(96, 6, 104);
    width: 50%;
    margin-left: 20%;
    color: white;
    font-size: 28px;
    padding: 10px 20px;
    border-radius : 10px;
    transition: 0.3s;
    box-shadow: 0px 5px 15px rgba(0,201, 255, 0.4);
   
    }
    .stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(45deg,rgb(176, 8, 182),rgb(140, 9, 180));
    color: black;
    
    }
    .result-box {
    font-size: 20px;
    font-weight: bold;
    text-align: center;
    background: rgba(255,255,255,0.1);
    padding: 15px;
    border-radius: 10px;
    margin-top: 20px;
    box-shadow: 0px 5px 15px rgba(0,201,255,0.4);}
    .footor{
    text-align: center;
    margin-top: 50px;
    font-size: 14px;
    color: black;}
    .stSidebar{
    background: rgba(65, 29, 68, 0.64);}
    </style>
    """,
    unsafe_allow_html= True
)

#hedding
st.markdown("<h1>Unit convertor using python and streamlit </h1>", unsafe_allow_html=True)
st.write("conversion between unit of lengths, temperature , weight")


##unit convertions
unit_conversion = st.sidebar.selectbox("Select the unit convertion", ["Length", "Temperature", "Weight"])
value = st.number_input("Enter the value to convert", value= 0.0 , min_value=0.0 , step=0.1)
col1, col2 = st.columns(2)

if unit_conversion == "Length":
    with col1:
      from_unit = st.selectbox("From unit", ["meters", "kilometers", "foot", "inches", "centimeters", "millimeters"])
    with col2: 
        to_unit = st.selectbox("To unit", ["meters", "kilometers", "foot", "inches", "centimeters", "millimeters"])
        
elif unit_conversion == "Temperature":
    with col1:
     from_unit = st.selectbox("From unit",["celcius", "farhenheit", "kelvin"])
    with col2:
        to_unit = st.selectbox("To unit", ["celcius", "farhenheit", "kelvin"])

elif unit_conversion == "Weight":
    with col1:
     from_unit = st.selectbox("From unit",["kilogram", "gram", "milligram", "pound"])
    with col2:
        to_unit = st.selectbox("To unit", ["kilogram", "gram", "milligram", "pound"])

def length_converter(value, from_unit, to_unit): 
    length_units = {
        'meters': 1, 'kilometers': 0.001 , 'centimeters': 100, 'millimeters': 1000,
        'miles': 0.000621371 , 'yards': 1.09361 ,'foot': 3.28084 , 'inches': 39.3701,
    } 

    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
        weight_units = {
            'kilogram': 1, 'gram': 1000, 'milligram': 1000000, 'pound': 2.20462
        }
        return (value / weight_units[from_unit]) * weight_units[to_unit]
        
def temperature_converter(value, from_unit, to_unit):
    if from_unit == "celcius":
        return (value * 9/5 + 32) if to_unit == "farhenheit" else value + 273.15 if to_unit == "kelvin" else value
    elif from_unit == "farhenheit":
        return (value - 32) * 5/9 if to_unit == "celcius" else (value - 32) * 5/9 + 273.15 if to_unit == "kelvin" else value
    elif from_unit == "kelvin":
        return value - 273.15 if to_unit == "celcius" else (value - 273.15) * 9/5 + 32 if to_unit == "farhenheit" else value
    return value   

if st.button("Convert"):
    if unit_conversion == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif unit_conversion == "Weight":
       result = weight_converter(value, from_unit, to_unit)
    elif unit_conversion == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit} </div>", unsafe_allow_html=True)

    st.markdown("<div class='footor'> Made with ❤️ by Ansharah </div>", unsafe_allow_html=True)


