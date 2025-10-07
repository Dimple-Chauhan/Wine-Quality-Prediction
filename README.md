## ** 🍷 Wine Quality Prediction using Machine Learning **

## **🧠 Project Overview**

The Wine Quality Prediction project aims to predict the quality of wine based on its chemical characteristics such as acidity, density, alcohol content, and more.
This project demonstrates the application of machine learning in viticulture, showcasing how data-driven approaches can help in assessing wine quality efficiently.

## ** 📊 Dataset Description **

The dataset contains several physicochemical variables (inputs) and a sensory quality score (output variable).

 Fixed Acidity, Volatile Acidity, Citric Acid, Residual Sugar, Chlorides, Free Sulfur Dioxide, Total Sulfur Dioxide, Density, pH, Sulphates, Alcohol, Type,	Quality	

## ** ⚙️ Project Structure

Wine Quality Prediction/
│
├── WineQT.csv         
├── main.ipynb        
├── best_wine_model.pkl           
├── app.py                   
└── README.md                 

## ** 🧩 Key Features

1. Built three classifiers:
    ✅ Random Forest Classifier
    ✅ Stochastic Gradient Descent (SGD) Classifier
    ✅ Support Vector Classifier (SVC)

2. Implemented Hyperparameter Tuning using GridSearchCV

3. Applied Cross-Validation to ensure model reliability

4. Visualized data using Seaborn and Matplotlib

5. Integrated with Streamlit for interactive web-based predictions

## ** 🧮 Libraries Used

1. Pandas → For data manipulation

2. NumPy → For numerical computations

3. Matplotlib & Seaborn → For data visualization

4. Scikit-learn → For machine learning models and evaluation

5. Streamlit → For building the web app interface

## ** 🚀 How to Run the Project

1️⃣ Clone the repository
    git clone https://github.com/<Dimple-Chauhan>/Wine-Quality-Prediction.git

2️⃣ Navigate to the project folder
    cd Wine-Quality-Prediction

3️⃣ Install dependencies
     pip install -r requirements.txt

4️⃣ Run the Streamlit app
    streamlit run app.py

5️⃣ Use the app

    Enter wine parameters (acidity, pH, alcohol, etc.)
    Click on Predict Quality 
    Get instant prediction of wine quality 🎯

## ** 📈 Model Performance

After applying hyperparameter tuning and cross-validation, the Random Forest model achieved the best performance with:

1. Accuracy: ~71.6%

2. Precision, Recall, and F1-scores computed for each wine quality level

3. Visualization of the confusion matrix for detailed analysis

