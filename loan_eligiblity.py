credit_score = int(input("Enter Your Credit Score : "))
sallary = int(input("Enter Sallry : "))
is_married = input("Are You Married : ")
age = int(input("Enter Your Age : "))
bonus = 5000 if is_married else 0
age_addon = 25000 if age < 30 and sallary > 75000 else 100000
loan_amount = (credit_score//10 + 0.3 * sallary + bonus + age_addon) * 10
if is_married and credit_score >= 800 and sallary > 75000 and age < 35:
    print(f"Eligible For The Loan Of Amount {loan_amount}")
elif credit_score >= 775 and sallary >= 45000 and age > 25:
    print(f"Eligible For The Loan. {loan_amount}")
else:
    print("Sorry, 😢 You are not eligible to take the loan.")
