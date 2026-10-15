# Student Pass/Fail Prediction ML Project

A simple demonstration project using Python, scikit-learn, and Flask.

## Files
- `train.py`: Generates sample student data, trains a Random Forest model, and saves `model.pkl`.
- `app.py`: Flask web app that predicts Pass/Fail from study hours, attendance, and internal marks.
- `requirements.txt`: Python dependencies.

## Run locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Train the model:
   ```bash
   python train.py
   ```
3. Start the Flask app:
   ```bash
   python app.py
   ```
4. Open http://127.0.0.1:5000 in your browser.

The app displays `Model Version: 1.0`.

Note: This is a demonstration model trained on synthetic data and is not intended for real student assessment.
