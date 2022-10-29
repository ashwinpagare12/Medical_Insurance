from flask import Flask,render_template,jsonify,request,redirect,url_for
from project_app.utils import MedicalInsurance

app=Flask(__name__)

@app.route("/")   # Home API
def hello_flask():
    print("Welcome to flask")
    return render_template("login.html")

@app.route("/result")
def result():
    return "Successful"

# @app.route('/hi/<name>')
# def result(name):
#     return f"Hello {name}"

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        return redirect(url_for('result', name=name))

# @app.route("/")
# def sd():
#     return 'df'


@app.route("/predict_charges")
def get_insurance_charges():
    data = request.form
    print(data)
    print(f"Data is: {data}")

    age  = eval(data["age"])
    sex  = data["sex"]
    bmi  = eval(data['bmi']) 
    children = eval(data['children'])
    smoker = data['smoker']
    region = data['region']

    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges = med_ins.get_predict_charges()

    return jsonify({"Return" : f"Predicted medical isurance charges are :{charges}"})

if __name__=="__main__":
    app.run()