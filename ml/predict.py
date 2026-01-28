
import joblib
import pandas as pd
import numpy as np

def load_models():
    try:
        placement_model = joblib.load("ml/models/placement_model.pkl")
        salary_model = joblib.load("ml/models/salary_model.pkl")
        label_encoder = joblib.load("ml/models/label_encoder.pkl")
        return placement_model, salary_model, label_encoder
    except FileNotFoundError as e:
        print(f"Error loading models: {e}")
        return None, None, None

def predict(data):

    placement_model, salary_model, label_encoder = load_models()
    
    if not placement_model:
        return {"error": "Models not found"}

    df = pd.DataFrame([data])
    
    if "Internship_Experience" in df.columns and label_encoder:
        try:
            df["Internship_Experience"] = label_encoder.transform(df["Internship_Experience"])
        except ValueError:
            if df["Internship_Experience"].dtype == 'object':
                 df["Internship_Experience"] = df["Internship_Experience"].str.title()
                 try:
                     df["Internship_Experience"] = label_encoder.transform(df["Internship_Experience"])
                 except:
                     df["Internship_Experience"] = 0

    placement_pred = placement_model.predict(df)[0]
    
    result = {
        "placed": bool(placement_pred == 1),
        "salary": 0.0
    }
    
    if result["placed"]:

        salary_pred = salary_model.predict(df)[0]
        result["salary"] = round(float(salary_pred), 2)
        
    return result

if __name__ == "__main__":
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
    print("Test Prediction:")
    print(predict(sample_data))
