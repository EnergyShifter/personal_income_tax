# Program to compute US personal income tax (2009 rates)

status = int(input("Enter filing status (0=Single, 1=Married Joint, 2=Married Separate, 3=Head of Household): "))
income = float(input("Enter taxable income: "))

tax = 0

# Tax brackets for each status
if status == 0:  # Single
    brackets = [(8350, 0.10), (33950, 0.15), (82250, 0.25),
                (171550, 0.28), (372950, 0.33), (float('inf'), 0.35)]
elif status == 1:  # Married filing jointly
    brackets = [(16700, 0.10), (67900, 0.15), (137050, 0.25),
                (208850, 0.28), (372950, 0.33), (float('inf'), 0.35)]
elif status == 2:  # Married filing separately
    brackets = [(8350, 0.10), (33950, 0.15), (68525, 0.25),
                (104425, 0.28), (186475, 0.33), (float('inf'), 0.35)]
elif status == 3:  # Head of household
    brackets = [(11950, 0.10), (45500, 0.15), (117450, 0.25),
                (190200, 0.28), (372950, 0.33), (float('inf'), 0.35)]
else:
    print("Invalid filing status")
    exit()

prev_limit = 0

for limit, rate in brackets:
    if income > limit:
        tax += (limit - prev_limit) * rate
        prev_limit = limit
    else:
        tax += (income - prev_limit) * rate
        break

print("Total tax is $", round(tax, 2))
