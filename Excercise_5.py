revenue = float(input("Please, enter revenue amount for the period: "))
expenses = abs(float(input("Please, enter expense amount for the period: ")))
financial_result = round(revenue - expenses, 2)
print(f"Your company has ended the period with {'income' if financial_result > 0 else 'loss'} of {financial_result}"
      f" USD")

if financial_result > 0:
    print(f"Your company revenue profitability for the period is equal to {round(financial_result / revenue, 5)}%")
    amount_of_employees = int(input("Please, enter number of employees: "))
    print(f"Your company profit attribute per one worker for the period is equal to"
          f" {round(financial_result / amount_of_employees, 5)} USD")



