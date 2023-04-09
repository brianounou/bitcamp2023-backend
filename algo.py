def housing_advice(credit_card_debt, mortgage_rent, liquid_assets, recurring_liabilities, unemployment_benefits):
    debtToIncomeRatio = (credit_card_debt + mortgage_rent + recurring_liabilities) / (liquid_assets + unemployment_benefits)

    # Step 1: Evaluate the debt-to-income ratio
    if debtToIncomeRatio > 0.3:
        return "Your debt to income ratio suggests that it would be beneficial that you not consider any new housing options at this time. Possible solutions include: paying off debt, increasing income, or decreasing expenses."


    # 30% INSERT MORTGAGE/RENT TO MONTHLY INCOME RATIO
    if mortgage_rent > 0.3 * unemployment_benefits:
        return "Your mortgage/rent to monthly income ratio suggests that you should consider new housing options at this time. Your mortgage/rent is 30% or more of your monthly income. Consider renting a cheaper apartment or buying a cheaper house."

    # 10% CREDIT CARD DEBT
    if credit_card_debt > 0.1 * liquid_assets:
        return "Your credit card debt to liquid assets ratio suggests that you should consider paying off credit card debts before considering any new housing options. Your credit card debt is 10% or more of your liquid assets."

    # 17% of ASSETS SHOULD BE MONTHLY BUDGET
    if liquid_assets < 0.17 * recurring_liabilities:
        return "Your liquid assets to monthly expenses ratio suggests that you should consider new housing options at this time. Monthly expenses can include car payments, bills, loan repayments,etc. Your liquid assets are less than 17% of your monthly expenses. Consider renting a cheaper apartment or buying a cheaper house in order to reduce monthly expenses."

    # Step 3: Evaluate unemployment benefits
    if unemployment_benefits > 0:
        return "Avoid major purchases or additional debt until employed again."
    elif liquid_assets < 3 * recurring_liabilities:
        return "Prioritize building up emergency fund before considering a home purchase."



def credit_card_advice(credit_card_debt, assets):
    # Check the percentage of credit card debt to assets
    percent_debt = credit_card_debt / assets * 100
    
    # Check the percentage range and give advice accordingly
    if percent_debt <= 10:
        print("Your credit card debt is less than 10% of your assets. Keep up the good work!")
    elif percent_debt <= 15:
        print("Your credit card debt is between 10% and 15% of your assets. Consider paying more than the minimum payment to lower your debt faster.")
    elif percent_debt <= 20:
        print("Your credit card debt is between 15% and 20% of your assets. Consider finding ways to reduce your expenses and increase your income to pay off your debt faster.")
    elif percent_debt <= 25:
        print("Your credit card debt is between 20% and 25% of your assets. You may want to consider seeking the help of a financial advisor to help you create a plan to pay off your debt faster.")
    elif percent_debt <= 30:
        print("Your credit card debt is between 25% and 30% of your assets. You should consider taking immediate action to pay off your debt, such as transferring your balance to a 0% APR credit card or consolidating your debt with a personal loan.")
    elif percent_debt <= 35:
        print("Your credit card debt is more than 30% of your assets. This is an urgent situation and you should take immediate action to pay off your debt. Consider seeking the help of a credit counseling agency or debt settlement firm to help you negotiate with your creditors and lower your interest rates.")

# Take input from the user
credit_card_debt = float(input("Enter your credit card debt: "))
assets = float(input("Enter your assets: "))

# Call the function with user input
credit_card_advice(credit_card_debt, assets)


def financial_stability_advice(assets, monthly_expenses):
    # Calculate the percentage of assets spent each month
    percent_expenses = monthly_expenses / assets * 100

    # Calculate the exact number of months until assets are depleted
    months_remaining = int(assets / monthly_expenses)

    # Check the percentage range and give advice accordingly
    if percent_expenses <= 17:
        print("Based on your current assets and monthly expenses, you have {months_remaining} months a healthy financial cushion.")
    elif percent_expenses <= 20:
        print(f"Based on your current assets and monthly expenses, you have approximately {months_remaining} months until you exhaust all available financial resources. Consider finding ways to reduce your expenses and increase your income to extend your financial cushion.")
    elif percent_expenses <= 23:
        print(f"Based on your current assets and monthly expenses, you have approximately {months_remaining} months until you exhaust all available financial resources. Consider taking immediate action to reduce your expenses and increase your income, such as downsizing your home, finding a higher-paying job, or starting a side business.")
    elif percent_expenses <= 26:
        print(f"Based on your current assets and monthly expenses, you have approximately {months_remaining} months until you exhaust all available financial resources. This is an urgent situation and you should take immediate action to reduce your expenses and increase your income, such as selling assets or taking on a second job.")
    elif percent_expenses <= 29:
        print(f"Based on your current assets and monthly expenses, you have approximately {months_remaining} months until you exhaust all available financial resources. You should consider seeking the help of a financial advisor to help you create a plan to manage your finances and avoid depleting all financial reserves.")
    elif percent_expenses <= 32:
        print(f"Based on your current assets and monthly expenses, you have approximately {months_remaining} months until you exhaust all available financial resources. This is a critical situation and you should take extreme measures to reduce your expenses and increase your income, such as liquidating assets or moving to a less expensive area.")
    elif percent_expenses > 32:
        print(f"Based on your current assets and monthly expenses, you have approximately {months_remaining} months until you exhaust all available financial resources. You should take immediate and extreme measures to reduce your expenses and increase your income, such as seeking financial assistance or declaring bankruptcy. Running low on financial assets.")

# Take input from the user
assets = float(input("Enter your assets: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

# Call the function with user input
financial_stability_advice(assets, monthly_expenses)
