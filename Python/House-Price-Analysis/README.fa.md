<div align="right">
[🇮🇷 فارسی](README.fa.md) | [🇬🇧 English](README.md)
</div>

# پیش‌بینی قیمت مسکن رودهن

پروژه‌ای مبتنی بر یادگیری ماشین برای تخمین قیمت کل املاک مسکونی در منطقه رودهن.

در این پروژه از الگوریتم **رگرسیون خطی (Linear Regression)** برای تخمین قیمت ملک بر اساس ویژگی‌های آن استفاده شده است.

### تکنولوژی‌ها

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)

### امکانات

- انتخاب نوع ملک (آپارتمان یا ویلا)
- تعیین متراژ و سال ساخت
- تعیین تعداد اتاق و طبقه
- انتخاب وضعیت پارکینگ، آسانسور و انباری
- تخمین قیمت کل ملک

### مدل یادگیری ماشین

- **الگوریتم:** رگرسیون خطی (Linear Regression)
- **متغیر هدف:** قیمت کل ملک
- **اندازه داده آزمایش:** ۴۰ درصد
- **Random State:** 1

### ساختار پروژه

```text
House-Price-Analysis/
├── README.md
├── README.fa.md
├── divar_rudehen.xlsx
├── home_price_rudhen_st.py
└── rudehen_home_price.ipynb
```

### نصب و اجرا

دریافت مخزن:

```bash
git clone https://github.com/Staha05/Machine-Learning.git
```

ورود به پوشه پروژه:

```bash
cd Machine-Learning/Python/House-Price-Analysis
```

نصب کتابخانه‌ها:

```bash
pip install streamlit pandas scikit-learn openpyxl
```

اجرای برنامه:

```bash
streamlit run home_price_rudhen_st.py
```

### دیتاست

اطلاعات املاک در فایل `divar_rudehen.xlsx` ذخیره شده است. این فایل باید در کنار فایل پایتون برنامه قرار داشته باشد.

### سلب مسئولیت

قیمت‌های پیش‌بینی‌شده تخمینی هستند و بر اساس داده‌های موجود محاسبه می‌شوند. این پروژه با اهداف آموزشی توسعه داده شده است.

### توسعه‌دهنده

**[Staha05](https://github.com/Staha05)**
