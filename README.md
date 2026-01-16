

```markdown
# 🎓 College Student Placement Prediction

## 📌 Project Overview
This project builds an end-to-end Machine Learning pipeline to predict whether a college student will be placed based on their academic performance, cognitive skills, and extra-curricular activities. 

The system uses an **XGBoost Classifier**, which achieved **near-perfect accuracy** on the test set, identifying `CGPA` and `Communication Skills` as the most critical factors for success.

---

## 📂 Repository Structure

| File | Description |
| :--- | :--- |
| `EDA_Report.ipynb` | **Exploratory Data Analysis:** Visualizes data distributions, checks correlations (e.g., IQ vs. CGPA), and identifies key trends. |
| `train_model.ipynb` | **Training Pipeline:** Handles data cleaning, encoding, model training (XGBoost), and evaluation. |
| `college_student_placement_dataset.csv` | **Dataset:** The raw data used for training and testing. |
| `requirement.txt` | **Dependencies:** List of Python libraries required to run the project. |
| `trained_model.pkl` | **Saved Model:** The serialized model (generated after running the training script) for future use. |

---

## 📊 Dataset Details

The dataset consists of student records with the following key features:

* **Target Variable:** `Placement` (0 = Not Placed, 1 = Placed)
* **Academic:** `CGPA`, `Prev_Sem_Result`, `Academic_Performance`
* **Cognitive & Skills:** `IQ`, `Communication_Skills`
* **Experience:** `Internship_Experience` (Converted to Binary), `Projects_Completed`
* **Other:** `Extra_Curricular_Score`

---

## 🚀 How to Run

### 1. Prerequisites
Ensure you have Python installed. Clone this repository and install the dependencies:

```bash
# Install required libraries
pip install -r requirement.txt

```

### 2. Exploratory Analysis

Run `EDA_Report.ipynb` to see the visualizations:

* Correlation Heatmaps
* Distribution of Placed vs. Not Placed students
* Impact of Internships on success rates

### 3. Train the Model

Run `train_model.ipynb`. This notebook will:

1. Load and clean the dataset.
2. Train the XGBoost model.
3. Print evaluation metrics (Accuracy, Confusion Matrix).
4. Save the model as `trained_model.pkl`.

---

## 🧠 Model Performance

The **XGBoost Classifier** was selected for its ability to handle non-linear relationships.

| Metric | Score |
| --- | --- |
| **Accuracy** | **100%** (approx) |
| **Precision** | 1.00 |
| **Recall** | 1.00 |

### Key Insights (Feature Importance)

1. **CGPA:** The strongest indicator of placement.
2. **Communication Skills:** The second most important factor.
3. **IQ:** Important, but less correlated with placement than grades or soft skills.

---

## 🔮 Making Predictions

You can use the saved model to predict placement for new students using the code below:

```python
import joblib
import pandas as pd

# 1. Load the model
model = joblib.load('trained_model.pkl')

# 2. Define a new student
new_student = pd.DataFrame([{
    'IQ': 110,
    'Prev_Sem_Result': 8.5,
    'CGPA': 8.2,
    'Academic_Performance': 7,
    'Internship_Experience': 1,  # 1 = Yes, 0 = No
    'Extra_Curricular_Score': 6,
    'Communication_Skills': 9,
    'Projects_Completed': 3
}])

# 3. Predict
prediction = model.predict(new_student)
probability = model.predict_proba(new_student)[0][1]

print(f"Prediction: {'Placed' if prediction[0] == 1 else 'Not Placed'}")
print(f"Confidence: {probability:.2%}")

```

---

## 👨‍💻 Author

**Kaushal Nandaniya** *Winter of Code (WoC) Contribution*

```

```
