
def income_encoding(income):
    if income <= 40000:
        Income_Category = 0
    elif income > 40000 or income <60000:
        Income_Category = 1
    elif income > 60000 or income < 80000:
        Income_Category = 2
    elif income > 80000 or income < 120000:
        Income_Category = 3
    elif income > 120000:
        Income_Category = 4
    return Income_Category

def gender_encoding(gender):
    if gender == "male":
        Gender = 0
    else:
        Gender = 1
    return Gender

def card_encoding(card):
    if card == "blue":
        Card_Category = 0
    elif card == "silver":
        Card_Category = 1
    elif card == "gold":
        Card_Category = 2
    if card == "platinum":
        Card_Category = 3
    return Card_Category

def education_encoding(education):
    if education == "uneducated":
        Education_Level = 0
    elif education == 'High_School':
        Education_Level = 1 
    elif education == 'College':
        Education_Level = 2  
    elif education == 'Graduate':
        Education_Level = 3 
    elif education == 'Post-Graduate':
        Education_Level = 4
    elif education == "Doctorate":
        Education_Level = 5
    return Education_Level