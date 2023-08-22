from flask import jsonify,redirect,Flask, request
import config
from utils import get_prediction

app = Flask(__name__)
@app.route("/")
def flask():
    print("We are in flask")

    return jsonify({"Result": "We are testing Flask"})

@app.route("/pred")    
def prediction():
    data = request.form 
    Customer_Age = int(data["Customer_Age"])
    gender = data["gender"]
    Dependent_count = int(data["Dependent_count"])
    education = data["education"]
    income = eval(data["income"])
    card = data["card"]
    Months_on_book = eval(data["Months_on_book"])
    Total_Relationship_Count = eval(data["Total_Relationship_Count"])
    Months_Inactive_12_mon = eval(data["Months_Inactive_12_mon"])
    Contacts_Count_12_mon = eval(data["Contacts_Count_12_mon"])
    Credit_Limit = eval(data["Credit_Limit"])
    Total_Revolving_Bal = eval(data["Total_Revolving_Bal"])
    Avg_Open_To_Buy = eval(data["Avg_Open_To_Buy"])
    Total_Amt_Chng_Q4_Q1 = eval(data["Total_Amt_Chng_Q4_Q1"])
    Total_Trans_Amt = eval(data["Total_Trans_Amt"])
    Total_Trans_Ct = eval(data["Total_Trans_Ct"])
    Total_Ct_Chng_Q4_Q1 = eval(data["Total_Ct_Chng_Q4_Q1"])
    Avg_Utilization_Ratio = eval(data["Avg_Utilization_Ratio"])
    Marital_Status = data["Marital_Status"]

    result = get_prediction(Customer_Age,gender,Dependent_count,education,income,card,
                   Months_on_book,Total_Relationship_Count,Months_Inactive_12_mon,Contacts_Count_12_mon,
                   Credit_Limit,Total_Revolving_Bal,Avg_Open_To_Buy,Total_Amt_Chng_Q4_Q1,Total_Trans_Amt,
                   Total_Trans_Ct,Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio,Marital_Status)

    print("prediction : ", result)
    return jsonify({"result":result})
app.run()

