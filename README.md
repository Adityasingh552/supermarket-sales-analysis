# 🛒 Supermarket Sales Analysis & Prediction Dashboard

This project is a **hybrid of Data Analytics and Machine Learning**.  
It explores supermarket sales data through **visual insights** and builds a **predictive model** for real-time sales forecasting — all wrapped in an interactive **Streamlit dashboard**.

---

## 📌 Objective

- 📈 Perform **exploratory data analysis (EDA)** to uncover sales trends
- 🤖 Build a **Random Forest model** to predict total sales
- 💻 Create a **Streamlit dashboard** for user-friendly interaction

---

## 💡 Key Highlights

✔️ Combination of **descriptive analytics** and **predictive modeling**  
✔️ Real-time sales forecasting via user input  
✔️ Visualizations: trends, category performance, customer types  
✔️ Business-ready app with accurate results

---

## 🔍 What You'll See in the App

- Count plots for **payment types**, **customer types**, and **cities**
- Correlation **heatmap** for numerical insights
- Boxplots and line charts for **sales distribution**
- A **Random Forest** model to predict `Total` based on key features
- A dashboard for anyone to try predictions interactively

---

## 🧱 Project Structure

```
📁 supermarket-sales-dashboard
├── app.py                # Streamlit app
├── sales_model.pkl       # Trained model
├── features.pkl          # Top features used
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```


---

## 🚀 Step-by-Step Instructions

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/Adityasingh552/supermarket-sales-dashboard.git
cd supermarket-sales-dashboard
  ```

🔹 Step 2: Install Required Packages
    pip install -r requirements.txt
Or manually:
    pip install streamlit pandas numpy scikit-learn matplotlib seaborn


🔹 Step 3: Run the Dashboard
    streamlit run app.py

Your app will open at http://localhost:8501.


🔹 Step 4: Use the App
   .Input values for features like quantity, unit price, product line, etc.
   .View predicted sales instantly
   .Explore various visual analytics for better understanding.


📊 Tools Used:

| Tool                | Role                           |
| ------------------- | ------------------------------ |
| Python              | Programming base               |
| pandas, numpy       | Data cleaning & transformation |
| seaborn, matplotlib | Visualization                  |
| scikit-learn        | Model training and evaluation  |
| Streamlit           | Dashboard frontend             |
| pickle              | Model serialization            |


📈 Model Performance:

| Metric   | Score  |
| -------- | ------ |
| R² Score | \~0.92 |
| RMSE     | ₹45.67 |


👨‍💻 Author
Aditya Singh
B.Tech CSE (AI & ML) – K.R. Mangalam University
Data Science Intern at Unified Mentors
GitHub: @Adityasingh552



---

### ✅ Next Step
Would you like the **`requirements.txt` file** as well? I can generate it based on your final working setup.

