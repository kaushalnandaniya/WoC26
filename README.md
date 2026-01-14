# 🎓 College Student Placement Prediction

### ❄️ Winter of Codes Contribution
**Project:** End-to-End Machine Learning Pipeline for Student Placement Prediction  
**Dataset:** [College Student Placement Factors Dataset](https://www.kaggle.com/datasets/sahilislam007/college-student-placement-factors-dataset)

---

## 📌 Project Overview
This project focuses on building a Machine Learning model to predict whether a college student will get placed based on various academic and personal factors. The workflow includes **Exploratory Data Analysis (EDA)**, **Data Preprocessing**, and **Model Training**.

The goal is to identify key indicators of placement success (such as CGPA, IQ, and internships) and assist educational institutions in providing targeted support to students.

---

## 📂 Dataset Details
The dataset contains student information regarding academic performance, cognitive abilities, and extra-curricular activities.

- **Source:** Kaggle (sahilislam007)
- **Target Variable:** `placement` (Binary: 1 = Placed, 0 = Not Placed)
- **Key Features:**
  - `iq`: Intelligence Quotient score.
  - `cgpa`: Cumulative Grade Point Average.
  - `internship_experience`: Participation in internships.
  - `communication_skills`: Assessment of soft skills.
  - `projects_completed`: Number of academic/technical projects.
  - `academic_performance`: General academic standing.
  - `10th_marks` / `12th_marks`: Secondary education scores.

---

## 📊 Exploratory Data Analysis (EDA)
We analyzed the data to understand distributions and correlations. Key insights included:
1.  **Correlation Heatmap:** Checked for multicollinearity among independent variables.
2.  **Distribution Analysis:** Visualized the spread of `cgpa` and `iq` for placed vs. non-placed students.
3.  **Categorical Analysis:** Examined how `internship_experience` impacts placement probabilities.
4.  **Missing Values:** Identified and visualized missing data patterns (if any).

---

## ⚙️ Data Preprocessing
Before training, the raw data underwent the following transformations:
- **Handling Missing Values:** Imputed missing entries using mean/median strategies.
- **Encoding Categorical Variables:** Converted text-based features (e.g., `internship_experience`) into numerical format using Label Encoding or One-Hot Encoding.
- **Feature Scaling:** Applied Standardization (`StandardScaler`) to numerical features like `iq` and `cgpa` to ensure uniform model performance.
- **Train-Test Split:** Split the dataset into training (80%) and testing (20%) sets.

---

## 🤖 Model Training
Various classification algorithms were trained and evaluated:
1.  **Logistic Regression:** Baseline model for binary classification.
2.  **Decision Tree Classifier:** To capture non-linear patterns.
3.  **Random Forest Classifier:** For improved accuracy and to reduce overfitting.

### 📈 Evaluation Metrics
The models were evaluated based on:
- **Accuracy Score**
- **Precision & Recall**
- **Confusion Matrix**

---

## 🛠️ Installation & Usage

### Prerequisites
Ensure you have Python installed. Install the required libraries using:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
