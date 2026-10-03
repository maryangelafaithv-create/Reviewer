# inputs
# owner_age(integer)
# monthly_revenue (float)
# credit_score(integer)
# years_in_business(float)
# has_defaults(boolean)
# collateral_name(string)
# collateral_values(float)

age = int(input("AGE--->"))
rev = float(input("REVENUE --->"))
cc = int(input("CREDIT SCORE--->"))
yrs = float(input("YEARS IN BUSINESS--->"))
has_defaults = bool(input("FILE FOR BANKRUPCY--->"))
collateral = input("COLLATERAL NAME--->")
c_value = float(input("COLLATERAL VALUE--->"))

max_loan = 0
base_fee = 0

if age >= 21 and has_defaults == False and yrs >= 2.0:
    print("BASELINE PASSED")
    if cc >= 720:
        print("CREDIT SCORE IS HGH")
        max_loan = rev * 3
        if rev >= 50000:
            print("ABOVE 50K REVENUE")
            base_fee = max_loan * 0.015
            print("BASE FEE IS SET TO", base_fee)
        else:
            print("REVENUE BELOW 50K")
            base_fee = max_loan * 0.025
            print("BASE FEE IS SET TO", base_fee)

            #collateral
            if c_value >= max_loan:
                print("COLLATERAL", collateral, "WITH A VALUE OF", c_value, "IS ACCEPTED")
            else: 
                print("REJECTED: INSUFFICIENT COLLATERAL VALUE FOR",collateral)

            #surcharge
            if c_value % 5000 !=0:
                base_fee += 250
                print("ADDITIONAL CHARGE ADDED TO BASE FEE, TOTAL BASE FEE IS", base_fee)
            else:
                print("COLLATERAL VALUE IS DIVISIBLE BY 5000")

    elif cc <= 620 and cc < 720: 
        print("CREDIT SCORE IS IN RANGE OF 620 AND 720")
        max_loan = rev * 1.5
        if yrs >= 5.0:
            base_fee = max_loan * 0.02
            print("BASE FEE OF YEARS IN  BUSINESS IS GREATER THAN 5 YEARS", base_fee)
        else:
            base_fee = max_loan * 0.035
            print("YEARS IN BUSINESS IS LOWER THAN 5 YEARS THEREFORE BASE FEE IS",)

            #collateral
            if c_value >= max_loan: 
                 print("COLLATERAL", collateral, "WITH A VALUE OF", c_value, "IS ACCEPTED")
            else:
                print("REJECTED: INSUFFICIENT COLLATERAL VALUE FOR",collateral)
            
            #surcharge
            if c_value % 5000 !=0:
                 base_fee += 250
                 print("ADDITIONAL CHARGE ADDED TO BASE FEE, TOTAL BASE FEE IS", base_fee)
            else:
                print("COLLATERAL VALUE IS DIVISIBLE BY 5000")
    elif cc <620: 
        print("CREDIT IS TOO LOW")
    else: 
        print("YOUR CRIDET SCORE IS TOO LOW")

else:
    print("BASELINE FAILED")