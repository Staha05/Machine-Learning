 <div align="right">

[🇮🇷 فارسی](README.fa.md) | [🇬🇧 English](README.md)

</div>

<div align="center">

# 🏡 Rudehen House Price Prediction

### Smart Property Price Estimation Using Machine Learning

Predict residential property prices in Rudehen, Iran, using Machine Learning.

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)

![Status](https://img.shields.io/badge/Project-Machine%20Learning-success)
![Language](https://img.shields.io/badge/Interface-Persian-blue)

</div>

---

## 📌 About The Project

**Rudehen House Price Prediction** is a Machine Learning project designed to estimate residential property prices in Rudehen, Iran.

The application uses property characteristics and historical real estate data to predict the approximate total price of a property.

The prediction model is built using **Linear Regression**, with an interactive interface developed using Streamlit.

## ✨ Features

- 🏢 Apartment and Villa Selection
- 📐 Property Area Input
- 🗓️ Construction Year
- 🛏️ Number of Rooms
- 🚗 Parking Availability
- 🛗 Elevator Availability
- 📦 Storage Availability
- 🏬 Apartment Floor Selection
- 💰 Total Property Price Prediction
- 🇮🇷 Persian User Interface

## 🧠 Machine Learning

### Algorithm

**Linear Regression**

### Workflow

1. Load real estate data from Excel.
2. Prepare and clean the dataset.
3. Encode categorical features.
4. Separate features and target variable.
5. Split data into training and testing sets.
6. Train the Linear Regression model.
7. Predict property prices using user inputs.

### Model Configuration

| Parameter | Value |
|---|---|
| Algorithm | Linear Regression |
| Test Size | 40% |
| Random State | 1 |
| Target Variable | Total Property Price |

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Pandas | Data Processing |
| Scikit-learn | Machine Learning |
| Streamlit | Web Interface |
| Excel | Dataset Storage |

## 📂 Project Structure

```text
House-Price-Analysis/
│
├── README.md
├── README.fa.md
├── home_price_rudhen_st.py
├── divar_rudehen.xlsx
└── rudehen_home_price.ipynb
```

## 🚀 Installation & Usage

### 1. Clone Repository

```bash
git clone https://github.com/Staha05/Machine-Learning.git
```

### 2. Navigate to Project

```bash
cd Machine-Learning/Python/House-Price-Analysis
```

### 3. Install Dependencies

```bash
pip install streamlit pandas scikit-learn openpyxl
```

### 4. Run Application

```bash
streamlit run home_price_rudhen_st.py
```

Make sure `divar_rudehen.xlsx` is located in the same directory as the Python application.

## 📊 Project Files

| File | Description |
|---|---|
| `home_price_rudhen_st.py` | Streamlit Application |
| `divar_rudehen.xlsx` | Real Estate Dataset |
| `rudehen_home_price.ipynb` | Data Analysis Notebook |
| `README.md` | English Documentation |
| `README.fa.md` | Persian Documentation |

## ⚠️ Disclaimer

The predicted prices are approximate estimates based on the available dataset and trained model.

Actual property prices may vary depending on market conditions, location, property condition, and other factors.

This project is intended for educational and experimental purposes.

---

<div align="center">

### 👨‍💻 Developed by Staha05

**Python | Machine Learning | Data Science**

[GitHub Profile](https://github.com/Staha05)

⭐ If you find this project interesting, consider giving it a star!

</div>
