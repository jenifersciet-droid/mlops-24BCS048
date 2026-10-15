from flask import Flask, request, render_template_string
import pickle

app = Flask(__name__)

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Student Pass/Fail Prediction</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f0f4f8;
            text-align: center;
            margin: 0;
            padding: 40px 12px;
        }
        .container {
            box-sizing: border-box;
            background: white;
            max-width: 380px;
            margin: auto;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 12px #cccccc;
        }
        input {
            box-sizing: border-box;
            width: 100%;
            padding: 11px;
            margin: 9px 0;
        }
        button {
            background: #007bff;
            color: white;
            padding: 12px 20px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }
        .result { font-size: 22px; font-weight: bold; margin-top: 20px; }
        .version { color: gray; font-size: 14px; }
        .error { color: #b00020; margin-top: 12px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Student Result Prediction</h2>
        <p class="version">Model Version: 1.0</p>
        <form method="POST">
            <input type="number" name="study_hours"
                   placeholder="Study Hours (0-10)" min="0" max="10"
                   step="0.1" required>
            <input type="number" name="attendance"
                   placeholder="Attendance % (0-100)" min="0" max="100"
                   step="0.1" required>
            <input type="number" name="internal_marks"
                   placeholder="Internal Marks (0-100)" min="0" max="100"
                   step="0.1" required>
            <button type="submit">Predict Result</button>
        </form>
        {% if prediction %}
            <div class="result">Prediction: {{ prediction }}</div>
        {% endif %}
        {% if error %}
            <div class="error">{{ error }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            study_hours = float(request.form["study_hours"])
            attendance = float(request.form["attendance"])
            internal_marks = float(request.form["internal_marks"])

            if not (0 <= study_hours <= 10):
                raise ValueError("Study hours must be between 0 and 10.")
            if not (0 <= attendance <= 100):
                raise ValueError("Attendance must be between 0 and 100.")
            if not (0 <= internal_marks <= 100):
                raise ValueError("Internal marks must be between 0 and 100.")

            prediction = model.predict([[
                study_hours, attendance, internal_marks
            ]])[0]
        except (ValueError, KeyError):
            error = "Please enter valid values within the ranges shown."

    return render_template_string(HTML, prediction=prediction, error=error)

if __name__ == "__main__":
    app.run(debug=False)
