"""
Flask Backend for College Placement Prediction Model
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_models():
    """Load the trained models and label encoder."""
    try:
        placement_model = joblib.load(os.path.join(BASE_DIR, "ml/models/placement_model.pkl"))
        salary_model = joblib.load(os.path.join(BASE_DIR, "ml/models/salary_model.pkl"))
        label_encoder = joblib.load(os.path.join(BASE_DIR, "ml/models/label_encoder.pkl"))
        return placement_model, salary_model, label_encoder
    except FileNotFoundError as e:
        print(f"Error loading models: {e}")
        return None, None, None

# Load models at startup
placement_model, salary_model, label_encoder = load_models()

@app.route('/')
def index():
    """Serve the main page."""
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    """Handle prediction requests."""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        if not placement_model:
            return jsonify({"error": "Models not loaded"}), 500
        
        # Create DataFrame from input
        df = pd.DataFrame([{
            "IQ": float(data.get("iq", 0)),
            "Prev_Sem_Result": float(data.get("prev_sem_result", 0)),
            "CGPA": float(data.get("cgpa", 0)),
            "Academic_Performance": float(data.get("academic_performance", 0)),
            "Internship_Experience": data.get("internship_experience", "No"),
            "Extra_Curricular_Score": float(data.get("extra_curricular_score", 0)),
            "Communication_Skills": float(data.get("communication_skills", 0)),
            "Projects_Completed": int(data.get("projects_completed", 0))
        }])
        
        # Encode internship experience
        if label_encoder:
            try:
                df["Internship_Experience"] = label_encoder.transform(df["Internship_Experience"])
            except ValueError:
                df["Internship_Experience"] = df["Internship_Experience"].str.title()
                try:
                    df["Internship_Experience"] = label_encoder.transform(df["Internship_Experience"])
                except:
                    df["Internship_Experience"] = 0
        
        # Make predictions
        placement_pred = placement_model.predict(df)[0]
        
        result = {
            "placed": bool(placement_pred == 1),
            "salary": 0.0,
            "confidence": "High" if placement_pred == 1 else "Moderate"
        }
        
        if result["placed"]:
            salary_pred = salary_model.predict(df)[0]
            result["salary"] = round(float(salary_pred), 2)
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("🚀 Starting Placement Prediction Server...")
    print("📊 Models loaded successfully!" if placement_model else "❌ Failed to load models")
    app.run(debug=True, port=5000)
