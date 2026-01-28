# College Student Placement Prediction

This project focuses on predicting student placement status and potential salary based on academic performance, internship experience, and other extracurricular factors. It utilizes machine learning models to analyze student data and provide insights.

## Project Structure

The project is organized as follows:

- **`ml/`**: Contains the core machine learning logic.
    - `models/`: Directory storing trained models (`placement_model.pkl`, `salary_model.pkl`) and the label encoder (`label_encoder.pkl`).
    - `predict.py`: Script for making predictions using the trained models. Contains `predict(data)` function.
    - `preprocess.py`: Helper script for data preprocessing, including encoding categorical variables and adding a synthetic salary column.
    - `train.ipynb`: Jupyter notebook used for training the machine learning models.
- **`woc/`**: Virtual environment directory (exclude from version control).
- **`college_student_placement_dataset.csv`**: The dataset used for training and analysis.
- **`EDA_Report.ipynb`**: Jupyter notebook containing Exploratory Data Analysis (EDA) on the dataset.
- **`requirement.txt`**: List of Python dependencies required for the project.

## Installation

1.  **Clone the repository** (if applicable) or navigate to the project root.
2.  **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # venv\Scripts\activate  # On Windows
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirement.txt
    ```

## Usage

### 1. Exploratory Data Analysis (EDA)
Open `EDA_Report.ipynb` in Jupyter Notebook or VS Code to view the analysis of the dataset, including visualizations and insights.

### 2. Training Models
To retrain the models, open and run the cells in `ml/train.ipynb`. This will:
- Load and preprocess the data.
- Train the placement and salary prediction models.
- Save the trained models to the `ml/models/` directory.

### 3. Making Predictions
You can use the `ml/predict.py` script to make predictions on new data.

**Example Usage (Python):**

```python
from ml.predict import predict

sample_data = {
    "IQ": 115,
    "Prev_Sem_Result": 8.0,
    "CGPA": 9.0,
    "Academic_Performance": 8,
    "Internship_Experience": "Yes",
    "Extra_Curricular_Score": 5,
    "Communication_Skills": 7,
    "Projects_Completed": 2
}

prediction = predict(sample_data)
print(prediction)
# Output: {'placed': True, 'salary': 450000.0} (Example)
```

## Dataset
The dataset `college_student_placement_dataset.csv` contains information such as:
- IQ
- CGPA
- Internship Experience
- Projects Completed
- Placement Status
- Etc.

## Requirements
- Python 3.x
- pandas
- numpy
- scikit-learn
- joblib
- matplotlib
- seaborn
- xgboost
