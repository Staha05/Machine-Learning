<p align="right">
  <img src="https://img.shields.io/badge/🇮🇷_فارسی-198754?style=for-the-badge" />
  <a href="README.md">
    <img src="https://img.shields.io/badge/🇬🇧_English-333333?style=for-the-badge" />
  </a>
</p>

# طبیب‌یار | پیش‌بینی بیماری با یادگیری ماشین

طبیب‌یار یک پروژه مبتنی بر یادگیری ماشین است که با استفاده از Streamlit توسعه داده شده و امکان آزمایش مدل‌های پیش‌بینی بیماری را فراهم می‌کند.

این پروژه شامل سه بخش پیش‌بینی و یک بخش آموزش مدل‌های شخصی است.

### تکنولوژی‌ها

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)

### امکانات

- پیش‌بینی دیابت
- پیش‌بینی سرطان سینه
- پیش‌بینی آلزایمر
- انتخاب الگوریتم یادگیری ماشین
- آپلود دیتاست با فرمت CSV و Excel
- آموزش مدل با داده‌های دلخواه
- پیش‌بینی با مدل آموزش‌دیده
- رابط کاربری تعاملی با Streamlit

### الگوریتم‌های یادگیری ماشین

الگوریتم‌های استفاده‌شده در پروژه:

- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Decision Tree
- Naive Bayes

در بخش مدل‌سازی شخصی، الگوریتم‌های رگرسیون نیز پشتیبانی می‌شوند.

### دیتاست‌ها

این پروژه از داده‌های زیر استفاده می‌کند:

- `Diabetes.csv`
- `alzheimers_disease_data.csv`
- دیتاست سرطان سینه کتابخانه Scikit-learn

فایل‌های CSV موردنیاز باید در پوشه پروژه قرار داشته باشند.

### نصب و اجرا

دریافت مخزن:

```bash
git clone https://github.com/Staha05/Machine-Learning.git
```

ورود به پوشه پروژه:

```bash
cd Machine-Learning/Python/Medical-Disease-Prediction
```

نصب کتابخانه‌ها:

```bash
pip install streamlit pandas numpy scikit-learn openpyxl
```

اجرای برنامه:

```bash
streamlit run YOUR_FILE_NAME.py
```

### سلب مسئولیت

این پروژه با اهداف آموزشی و آزمایش الگوریتم‌های یادگیری ماشین توسعه داده شده است.

نتایج پیش‌بینی، تشخیص پزشکی محسوب نمی‌شوند و نباید جایگزین نظر پزشک یا مشاوره تخصصی شوند.

### توسعه‌دهنده

**[Staha05](https://github.com/Staha05)**
