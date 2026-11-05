<p align="right">
  <a href="README.fa.md">
    <img src="https://img.shields.io/badge/🇮🇷_فارسی-198754?style=for-the-badge" />
  </a>
  <img src="https://img.shields.io/badge/🇬🇧_English-333333?style=for-the-badge" />
</p>
# House Price Prediction — Rudehen

A machine learning project for estimating residential property prices in Rudehen, Iran.

The application uses **Linear Regression** to predict the estimated total price of a property based on its features.

### Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)

### Features

- Property type selection (Apartment / Villa)
- Property area and construction year
- Number of rooms and floor
- Parking, elevator, and storage options
- Estimated total property price

### Model

- **Algorithm:** Linear Regression
- **Target:** Total property price
- **Test size:** 40%
- **Random state:** 1

### Project Structure

```text
House-Price-Analysis/
├── README.md
├── README.fa.md
├── divar_rudehen.xlsx
├── home_price_rudhen_st.py
└── rudehen_home_price.ipynb
```

### Installation

Clone the repository:

```bash
git clone https://github.com/Staha05/Machine-Learning.git
```

Navigate to the project directory:

```bash
cd Machine-Learning/Python/House-Price-Analysis
```

Install dependencies:

```bash
pip install streamlit pandas scikit-learn openpyxl
```

Run the application:

```bash
streamlit run home_price_rudhen_st.py
```

### Dataset

The project uses `divar_rudehen.xlsx` as its property dataset. Keep this file in the same directory as the Python application.

### Disclaimer

Predictions are estimates based on the available dataset and should not be considered guaranteed market prices. This project is developed for educational purposes.

### Author

**[Staha05](https://github.com/Staha05)**
