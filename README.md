# 🛍️ Black Friday Purchase Prediction

> An end‑to‑end Machine Learning web application that predicts a customer’s **purchase amount** using demographic and product information — built with Python, XGBoost, and Streamlit, and deployed to the cloud for real‑time inference.
> Customer Behavior Analysis
The project focuses on understanding the "how" and "why" behind customer spending.

Spending Patterns: It analyzes how much different groups of people spend on specific product categories.

Demographic Influence: The project examines how factors like Age, Gender, and Occupation directly correlate with total purchase amounts.

Product Preferences: It identifies which product categories (Product_Category_1, 2, or 3) drive the most volume during high-traffic events like Black Friday.
Customer Behavior Analysis
The project focuses on understanding the "how" and "why" behind customer spending.

Spending Patterns: It analyzes how much different groups of people spend on specific product categories.

Demographic Influence: The project examines how factors like Age, Gender, and Occupation directly correlate with total purchase amounts.

Product Preferences: It identifies which product categories (Product_Category_1, 2, or 3) drive the most volume during high-traffic events like Black Friday.
🔗 **Live App:** [https://ashutoshrana434-black-friday-sales-prediction-app-zif3ay.streamlit.app/](https://ashutoshrana434-black-friday-sales-prediction-app-zif3ay.streamlit.app/)

---<img width="1880" height="1050" alt="image" src="https://github.com/user-attachments/assets/2a43be5a-fed7-4512-b5ec-cec2bc0c0741" />


## ✨ Highlights

* End‑to‑end ML pipeline (EDA → Feature Engineering → Model → Deployment)
* Real‑time predictions via an interactive web UI
* Cross‑platform safe model loading (XGBoost JSON booster)
* Handles categorical encodings consistently between training & inference
* Publicly deployed and accessible from any device

---

## 🧠 Problem Statement

Retailers want to estimate how much a customer will spend during promotional events like **Black Friday**. Accurate predictions help with:

* Demand forecasting
* Inventory planning
* Targeted marketing campaigns
* Personalized offers

This project builds a regression model to estimate the **Purchase Amount (₹)** using customer demographics and product categories.

---

## 📊 Dataset

The dataset contains anonymized customer shopping data including:

* Gender
* Age group
* City category
* Years in current city
* Occupation
* Product category information
* Marital status
* Purchase amount (target)

Target Variable: **Purchase**

---

## ⚙️ Tech Stack

* **Python** – Core language
* **Pandas & NumPy** – Data processing
* **Scikit‑learn** – Preprocessing utilities
* **XGBoost** – Regression model
* **Streamlit** – Web application
* **Git & GitHub** – Version control
* **Streamlit Community Cloud** – Deployment

---

## 🏗️ Project Architecture

```
User Input (Web Form)
        ↓
Input Validation & Encoding
        ↓
Feature Alignment
        ↓
XGBoost Model (JSON Booster)
        ↓
Predicted Purchase Amount (₹)
```

---

## 📁 Project Structure

```
black-friday-sales-prediction/
│
├── app.py                     # Streamlit web app
├── black_friday_model.json    # Trained XGBoost model (portable format)
├── encoders.pkl               # Saved label encoders
├── model_columns.pkl          # Training feature columns
├── requirements.txt           # Dependencies
├── EDA and Feature Engineering_Model.ipynb
└── README.md
```

---

## 🚀 Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/Ashutoshrana434/Black-Friday-Sales-Prediction.git
cd Black-Friday-Sales-Prediction
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
streamlit run app.py
```

The app will open at:

```
http://localhost:8501
```

---

## 🧪 Example Input

| Feature              | Example |
| -------------------- | ------- |
| Gender               | F       |
| Age                  | 26‑35   |
| City Category        | B       |
| Stay in Current City | 2       |
| Occupation           | 7       |
| Product Category 1   | 5       |
| Product Category 2   | 8       |
| Product Category 3   | 0       |

Output:

> Predicted Purchase Amount in ₹

---

## 🧩 Model Details

* Model: **XGBoost Regressor**
* Objective: Regression (predict purchase amount)
* Saved using: `model.save_model()` (JSON booster format)

Why JSON instead of pickle?

> Pickled XGBoost models can fail across operating systems. The JSON booster format ensures reliable loading in cloud environments.

---

## 🛠️ Key Challenges Solved

* Feature mismatch between training and inference
* Windows vs Linux deployment issues
* Model serialization errors
* Handling categorical encodings consistently
* Git & deployment debugging

---

## 📈 Future Improvements

* Add model performance metrics (RMSE, R²)
* Add visual analytics dashboard
* Add user history & recommendations
* Containerize using Docker
* Add CI/CD pipeline

---

## 🤝 Contributing

Contributions and suggestions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is for educational and portfolio purposes.

---

## 👤 Author

**Ashutosh Rana**

* GitHub: [https://github.com/Ashutoshrana434](https://github.com/Ashutoshrana434)

