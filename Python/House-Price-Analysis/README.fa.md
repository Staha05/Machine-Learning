<div align="right">

[🇮🇷 فارسی](README.fa.md) | [🇬🇧 English](README.md)

</div>

<div align="center">

# 🏡 پیش‌بینی قیمت مسکن رودهن

### تخمین هوشمند قیمت ملک با استفاده از یادگیری ماشین

پروژه‌ای برای تخمین قیمت املاک مسکونی در منطقه رودهن با استفاده از الگوریتم‌های یادگیری ماشین.

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)

![وضعیت](https://img.shields.io/badge/Project-Machine%20Learning-success)
![زبان](https://img.shields.io/badge/Interface-Persian-blue)

</div>

---

## 📌 درباره پروژه

**پیش‌بینی قیمت مسکن رودهن** یک پروژه یادگیری ماشین برای تخمین قیمت املاک مسکونی در منطقه رودهن است.

این نرم‌افزار با دریافت مشخصات ملک و استفاده از داده‌های معاملات و آگهی‌های مسکن، قیمت تقریبی کل ملک را پیش‌بینی می‌کند.

مدل پیش‌بینی این پروژه بر اساس الگوریتم **رگرسیون خطی (Linear Regression)** ساخته شده و رابط کاربری آن با Streamlit توسعه یافته است.

## ✨ امکانات

- 🏢 انتخاب نوع ملک (آپارتمان یا ویلا)
- 📐 وارد کردن متراژ ملک
- 🗓️ تعیین سال ساخت
- 🛏️ تعیین تعداد اتاق
- 🚗 انتخاب وضعیت پارکینگ
- 🛗 انتخاب وضعیت آسانسور
- 📦 انتخاب وضعیت انباری
- 🏬 تعیین طبقه آپارتمان
- 💰 پیش‌بینی قیمت کل ملک
- 🇮🇷 رابط کاربری فارسی

## 🧠 یادگیری ماشین

### الگوریتم مورد استفاده

**Linear Regression | رگرسیون خطی**

### مراحل انجام پروژه

1. بارگذاری اطلاعات املاک از فایل Excel
2. آماده‌سازی و پاک‌سازی داده‌ها
3. تبدیل ویژگی‌های متنی به مقادیر عددی
4. جداسازی ویژگی‌ها و متغیر هدف
5. تقسیم داده‌ها به دو بخش آموزش و آزمایش
6. آموزش مدل رگرسیون خطی
7. پیش‌بینی قیمت ملک بر اساس اطلاعات ورودی

### تنظیمات مدل

| پارامتر | مقدار |
|---|---|
| الگوریتم | Linear Regression |
| اندازه داده آزمایش | ۴۰٪ |
| Random State | ۱ |
| متغیر هدف | قیمت کل ملک |

## 🛠️ تکنولوژی‌های استفاده شده

| تکنولوژی | کاربرد |
|---|---|
| Python | زبان برنامه‌نویسی |
| Pandas | پردازش داده‌ها |
| Scikit-learn | یادگیری ماشین |
| Streamlit | ساخت رابط کاربری |
| Excel | ذخیره‌سازی دیتاست |

## 📂 ساختار پروژه

```text
House-Price-Analysis/
│
├── README.md
├── README.fa.md
├── home_price_rudhen_st.py
├── divar_rudehen.xlsx
└── rudehen_home_price.ipynb
```

## 🚀 نصب و راه‌اندازی

### ۱. دریافت مخزن

```bash
git clone https://github.com/Staha05/Machine-Learning.git
```

### ۲. ورود به پوشه پروژه

```bash
cd Machine-Learning/Python/House-Price-Analysis
```

### ۳. نصب کتابخانه‌ها

```bash
pip install streamlit pandas scikit-learn openpyxl
```

### ۴. اجرای نرم‌افزار

```bash
streamlit run home_price_rudhen_st.py
```

توجه داشته باشید فایل `divar_rudehen.xlsx` باید در کنار فایل پایتون قرار داشته باشد.

## 📊 فایل‌های پروژه

| فایل | توضیحات |
|---|---|
| `home_price_rudhen_st.py` | نرم‌افزار پیش‌بینی قیمت |
| `divar_rudehen.xlsx` | دیتاست املاک |
| `rudehen_home_price.ipynb` | دفترچه تحلیل داده |
| `README.md` | مستندات انگلیسی |
| `README.fa.md` | مستندات فارسی |

## ⚠️ سلب مسئولیت

قیمت‌های ارائه‌شده توسط این نرم‌افزار تخمینی هستند و بر اساس داده‌های موجود و مدل آموزش‌دیده محاسبه می‌شوند.

قیمت واقعی ملک ممکن است تحت تأثیر شرایط بازار، موقعیت مکانی، وضعیت ساختمان و عوامل دیگر متفاوت باشد.

این پروژه با اهداف آموزشی و آزمایشی توسعه داده شده است.

---

<div align="center">

### 👨‍💻 توسعه‌دهنده

**Staha05**

Python | Machine Learning | Data Science

[مشاهده پروفایل GitHub](https://github.com/Staha05)

⭐ اگر این پروژه برایتان جالب بود، با دادن Star از آن حمایت کنید.

</div>
