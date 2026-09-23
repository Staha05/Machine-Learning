import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.set_page_config(
    page_title="پیش‌بینی قیمت مسکن رودهن",
    page_icon="C:\\Users\\lenovo\\Downloads\\icon.png",  # مسیر عکس تو پروژه
    layout="centered"
)
st.markdown("""
<h2 style="color: green; text-align: center;">
 به نرم افزار پیش‌بینی قیمت مسکن رودهن خوش آمدید
</h2>
<p style="text-align: center; font-size: 18px;">
قیمت خونه‌ات رو قبل از خرید و فروش بدون
</p>
<hr>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    Property_type = st.selectbox("نوع ملک", ["آپارتمان", "ویلا"])
    Meterage = st.number_input("متراژ (متر مربع)", min_value=30, value=100)
    year_of_manufacture = st.number_input("سال ساخت", min_value=1380, max_value=1405, value=1400)
    Number_of_rooms = st.number_input("تعداد اتاق", min_value=1, value=2, max_value=5)

with col2:
    parking = st.selectbox("پارکینگ", ["داشته باشد", "نداشته باشد"])
    elevator = st.selectbox("آسانسور", ["داشته باشد", "نداشته باشد"])
    warehouse = st.selectbox("انباری", ["داشته باشد", "نداشته باشد"])
    
    if Property_type == "آپارتمان":
        floor = st.number_input("طبقه ملک", min_value=1, value=2, max_value=12)
    else:
        floor = 0

if Property_type == "آپارتمان":
    property_type_num = 0
else:
    property_type_num = 1

if parking == "داشته باشد":
    parking_num = 0
else:
    parking_num = 1

if elevator == "داشته باشد":
    elevator_num = 0
else:
    elevator_num = 1

if warehouse == "داشته باشد":
    warehouse_num = 0
else:
    warehouse_num = 1

df = pd.read_excel("divar_rudehen.xlsx", index_col=0)
df.drop(["تعداد طبقات ساختمان", "محدوده"], axis=1, inplace=True)
    
pd.set_option('future.no_silent_downcasting', True)
df.replace({
    "نوع ملک": {"آپارتمان": 0, "ویلا": 1},
    "پارکینگ": {"بله": 0, "خیر": 1},
    "آسانسور": {"بله": 0, "خیر": 1},
    "انباری": {"بله": 0, "خیر": 1},
    "استان": {"تهران": 0},
    "منطقه": {"رودهن": 0},
    "نوع معامله": {"فروش": 0},
}, inplace=True)

X = df.loc[:, (df.columns != 'قیمت کل') & (df.columns != 'قیمت هر متر')]
Y = df['قیمت کل']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.40, random_state=1)

model = LinearRegression()
model.fit(X_train, Y_train)

features_for_prediction = [
    property_type_num,  
    Meterage,           
    year_of_manufacture,
    Number_of_rooms,    
    floor,              
    parking_num,        
    elevator_num,       
    warehouse_num,      
    0,                  
    0,                  
    0                   
]

features_df = pd.DataFrame([features_for_prediction], columns=X_train.columns)

predicted_total_price = model.predict(features_df)
if st.button("پیش‌بینی قیمت", use_container_width=True, type="primary"):
    st.markdown("---")
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 30px; 
                border-radius: 20px; 
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                animation: fadeIn 0.5s ease-in;">
        <h2 style="color: white;"> قیمت پیش‌بینی شده</h2>
        <h1 style="color: #ffd700; font-size: 48px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            {predicted_total_price[0]:,.0f} 
        </h1>
        <h3 style="color: white;">تومان</h3>
        <p style="font-size: 14px; color: #ffd700;">⚠️  این یک پیش‌بینی بر اساس داده‌های موجود است و ۱۰۰% دقیق نمی‌باشد و حدودی می باشد</p>
    </div>
    <style>
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>
    """, unsafe_allow_html=True)
