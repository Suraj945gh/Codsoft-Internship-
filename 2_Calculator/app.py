from flask import Flask, request, jsonify, render_template

# Create the app object
app = Flask(__name__)


# importing function for calculations
from my_calculator import simple_calculator

# Define calculator
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['post'])
def predict():

    num1 = request.form['num1']
    num2 = request.form['num2']
    op = str(request.form['op'])

    result = simple_calculator(num1,num2,op)

    return render_template('index.html', prediction_text=str(result))


if __name__ == "__main__":
    app.run(debug=True)