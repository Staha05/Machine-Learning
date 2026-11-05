# 🏡 House Price Prediction | Rudehen

<div align="center">

# 🏠 Rudehen House Price Predictor

### Predict House Prices Using Machine Learning

A Persian-language machine learning application for estimating residential property prices in Rudehen, Iran.

**Built with Python · Streamlit · Scikit-learn**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikitlearn)
![Status](https://img.shields.io/badge/Status-Completed-success)

</div>

---

## 📌 About The Project

**House Price Prediction – Rudehen** is a machine learning project designed to estimate the total price of residential properties in Rudehen, Iran.

The application uses property information such as area, construction year, number of rooms, parking, elevator, and storage to generate an estimated property price.

The project uses a Linear Regression model trained on real estate listing data.

## ✨ Features

- 🏢 Apartment and Villa Selection
- 📐 Property Area Input
- 🗓️ Construction Year
- 🛏️ Number of Rooms
- 🚗 Parking Availability
- 🛗 Elevator Availability
- 📦 Storage Availability
- 🏬 Apartment Floor Selection
- 💰 Estimated Total Property Price
- 🇮🇷 Persian User Interface

## 🧠 Machine Learning

The prediction model is based on **Linear Regression**.

### Workflow

1. Load real estate data from Excel.
2. Clean and prepare the dataset.
3. Convert categorical features into numerical values.
4. Split the dataset into training and testing sets.
5. Train the Linear Regression model.
6. Predict the total property price based on user inputs.

### Model Configuration

| Parameter | Value |
|---|---|
| Algorithm | Linear Regression |
| Test Size | 40% |
| Random State | 1 |
| Target | Total Property Price |

## 🛠️ Technologies

- Python
- Pandas
- Scikit-learn
- Streamlit
- Excel Dataset

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Staha05/Machine-Learning.git
```

Go to the project directory:

```bash
cd Machine-Learning/Python/House-Price-Analysis
```

Install dependencies:

```bash
pip install streamlit pandas scikit-learn openpyxl
```

Make sure the dataset `divar_rudehen.xlsx` is available in the project directory.

Run the application:

```bash
streamlit run app.py
```

## 📂 Project Structure

```text
House-Price-Analysis/
│
├── app.py
├── divar_rudehen.xlsx
├── icon.png
└── README.md
```

## ⚠️ Disclaimer

The predicted prices are estimates generated from historical dataset information.

Actual property prices may vary depending on market conditions, location, property condition, and other factors.

This application is intended for educational and experimental purposes.

---

<div align="center">

### 👨‍💻 Developed by Staha05

**Machine Learning | Python | Data Science**

[GitHub Profile](https://github.com/Staha05)

⭐ If you find this project interesting, consider giving it a star!

</div>
