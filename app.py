#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,render_template
app = Flask(__name__)


# In[2]:


import pickle

@app.route("/")
def hello():
    return"Hello world"

if __name__ == '__main__':
    app.run()
# In[ ]:




# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('modelhr1.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the form
    input_data = {
        'Age': int(request.form['age']),
        'Gender': int(request.form['gender']),
        'EducationLevel': int(request.form['education_level']),
        'Salary': int(request.form['salary']),
        'PerformanceRating': int(request.form['performance_rating']),
        'WorkLifeBalance': int(request.form['work_life_balance']),
        'EmployeeSatisfaction': int(request.form['employee_satisfaction']),
        'TrainingHours': int(request.form['training_hours']),
        'YearsInCurrentRole': int(request.form['years_in_current_role']),
        'YearsWithCurrentManager': int(request.form['years_with_current_manager'])
    }

    # Preprocess the input data
    input_df = pd.DataFrame([input_data])

    # Apply the trained model to make predictions
    predictions = model.predict(input_df)

    # Prepare the output
    output = ['Yes' if pred == 1 else 'No' for pred in predictions]

    # Render the result page with the predicted output
    return render_template('modelhr1.html', prediction=output[0])

if __name__ == '__main__':
    app.run()


# In[ ]:




