from flask import Flask, request, render_template
import pandas as pd
import joblib
import os
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')

# If the environment variable isn't set, you could use a default (not recommended for production)
if not app.config['SECRET_KEY']:
    print("WARNING: SECRET_KEY not set in environment. Using a default key.")
    app.config['SECRET_KEY'] = 'this-is-a-default-key-for-development-only'

csrf = CSRFProtect(app)

# Load the trained model
model = joblib.load('calorie_prediction_model.pkl')

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from form
        age = float(request.form['age'])
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        intensity = request.form['intensity']
        calories = float(request.form['calories'])
        protein = float(request.form['protein'])
        carbohydrate = float(request.form['carbohydrate'])
        fat = float(request.form['fat'])
        hydration = float(request.form['hydration'])
        sleep = float(request.form['sleep'])

        # Map intensity to numerical value
        intensity_map = {
            'very Low': 1,
            'low': 2,
            'medium': 3,
            'high': 4,
            'very high': 5
        }
        training_intensity = intensity_map.get(intensity, 0)

        # Prepare input data
        user_data = pd.DataFrame({
            'Age': [age],
            'Weight': [weight],
            'Height': [height],
            'Training_Intensity': [training_intensity],
            'Calories_Burned': [calories],
            'Protein': [protein],
            'Carbohydrates': [carbohydrate],
            'Fat': [fat],
            'Hydration': [hydration],
            'Sleep_Hours': [sleep]
        })

        # Predict calories needed
        predicted_calories = model.predict(user_data)
        return render_template('result.html', calories=round(predicted_calories[0], 2))

    except Exception as e:
        return f"An error occurred: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True)