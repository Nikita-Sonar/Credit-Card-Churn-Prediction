import pickle
import numpy as np
import config
from functions import education_encoding, income_encoding, gender_encoding, card_encoding 
def get_prediction(Customer_Age,gender,Dependent_count,education,income,card,
                   Months_on_book,Total_Relationship_Count,Months_Inactive_12_mon,Contacts_Count_12_mon,
                   Credit_Limit,Total_Revolving_Bal,Avg_Open_To_Buy,Total_Amt_Chng_Q4_Q1,Total_Trans_Amt,
                   Total_Trans_Ct,Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio,Marital_Status):
    with open("creditcard_churn.pkl","rb") as f:
        model = pickle.load(f)
    
    index = np.where(config.columns_list == Marital_Status) 

    array = np.zeros(21)
    array[0] = Customer_Age
    array[1] = gender_encoding(gender)
    array[2] = Dependent_count
    array[3] = education_encoding(education)
    array[4] = income_encoding(income)
    array[5] = card_encoding(card)
    array[6] = Months_on_book
    array[7] = Total_Relationship_Count
    array[8] = Months_Inactive_12_mon
    array[9] = Contacts_Count_12_mon
    array[10] = Credit_Limit
    array[11] = Total_Revolving_Bal
    array[12] = Avg_Open_To_Buy
    array[13] = Total_Amt_Chng_Q4_Q1
    array[14] = Total_Trans_Amt
    array[15] = Total_Trans_Ct
    array[16] = Total_Ct_Chng_Q4_Q1
    array[17] = Avg_Utilization_Ratio
    array[index] = 1
    
    prediction = model.predict([array])
    print(prediction[0])
    if prediction == 1.0:
        print("Existing Customore")
    else:
        print("Attrited Customer")
    
    return prediction[0]

Customer_Age = 45.000
gender = "Female"
Dependent_count = 3.000
education = 'Graduate'
income = 12000
card = "platinum"
Months_on_book = 39.000
Total_Relationship_Count = 5.000
Months_Inactive_12_mon = 1.000
Contacts_Count_12_mon = 3.000
Credit_Limit = 12691.000
Total_Revolving_Bal = 777.000
Avg_Open_To_Buy = 11914.000
Total_Amt_Chng_Q4_Q1 = 1.335
Total_Trans_Amt = 1144.000
Total_Trans_Ct = 42.000
Total_Ct_Chng_Q4_Q1 = 1.625
Avg_Utilization_Ratio = 0.061
Marital_Status = "Married"

if __name__ == "__main__":
    get_prediction(Customer_Age,gender,Dependent_count,education,income,card,
                   Months_on_book,Total_Relationship_Count,Months_Inactive_12_mon,Contacts_Count_12_mon,
                   Credit_Limit,Total_Revolving_Bal,Avg_Open_To_Buy,Total_Amt_Chng_Q4_Q1,Total_Trans_Amt,
                   Total_Trans_Ct,Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio,Marital_Status)