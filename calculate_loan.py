jump=[]
def main():
    temp={}
    print("Monthly loan payments calculetor: ")
    
    name=input("Enter Your name :")
    temp['name']=name
    email=input("Enter Your email :")
    if email.endswith('@gmail.com'):
        temp['email']=email
    else:
        print("your email is wrong")
        email=input("please Enter Your email again :")
        temp['email']=email
        
    principal=float(input("Need expected Loan :"))
    temp['principal']=principal
    apr=float(input("Interest Rate :"))
    temp['apr']=apr
    year=int(input("How many years need for loan :"))
    temp['year']=year
    monthly_interest_rate=apr/1200
    amount_of_month=year * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -amount_of_month)
    temp['monthly_payment']=monthly_payment
    temp.update(temp)
    # jump.append(temp)
    return temp

    
result=main()
print(result)

