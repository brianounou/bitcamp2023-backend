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
