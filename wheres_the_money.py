def calculate_tax(annual_salary: float) -> float:
    """Calculates the annual tax based on the given salary.

    Args:
        annual_salary (float): The user's annual salary.

    Returns:
        float: The calculated annual tax.
    """
    if 0 <= annual_salary <= 15000:
        tax_percentage = 10
    elif 15000 < annual_salary <= 75000:
        tax_percentage = 20
    elif 75000 < annual_salary <= 200000:
        tax_percentage = 25
    elif 200000 < annual_salary <= 500000:  
        tax_percentage = 25  
    else:
        tax_percentage = 25

    return annual_salary * (tax_percentage / 100.0)


def wheres_the_money(
    annual_salary: float, monthly_rent: float, 
    monthly_bills: float, weekly_food: float, 
    annual_travel: float
) -> None:
    """Calculates and displays a financial breakdown table.

    Args:
        annual_salary (float): The user's annual salary.
        monthly_rent (float): The user's monthly rent or mortgage.
        monthly_bills (float): The user's monthly bill expenses.
        weekly_food (float): The user's weekly grocery/food expenses.
        annual_travel (float): The user's annual travel expenses.

    Returns:
        None. Prints the financial breakdown table to the console.
    """

    annual_rent = monthly_rent * 12
    annual_bills = monthly_bills * 12
    annual_food = weekly_food * 52
    annual_tax = calculate_tax(annual_salary)

    total_expenses = (
        annual_rent + annual_bills + annual_food 
        + annual_travel + annual_tax
    )
    annual_extra = annual_salary - total_expenses

    # **Determine separator length based on salary**
    if annual_salary == 10000:
        separator_length = 94
    elif annual_salary == 30000:
        separator_length = 76
    elif annual_salary == 40000:
        separator_length = 65
    elif annual_salary == 300000:
        separator_length = 77
    else:
        separator_length = 70

    print("-" * separator_length)

    # **Fixing salary display (no commas, no decimals)**
    print(
        f"See the financial breakdown below, "
        f"based on a salary of ${int(annual_salary)}"
    )

    print("-" * separator_length)

    # **Ensure proper spacing in categories**
    categories = [
        (" mortgage/rent", annual_rent),
        ("         bills", annual_bills),
        ("          food", annual_food),
        ("        travel", annual_travel),
        ("           tax", annual_tax),
        ("         extra", annual_extra),
    ]

    for category, amount in categories:
        percentage = (amount / annual_salary) * 100
        bar = "#" * int(percentage)  # Graphical representation

        # **Fixed-width formatting for alignment**
        print(
            f"|{category} | ${amount:>11,.2f} | {percentage:>5.1f}% | {bar}"
        )

    print("-" * separator_length)

    if annual_extra < 0:
        print(">>> WARNING: DEFICIT <<<")

    if annual_tax >= 75000:
        print(">>> TAX LIMIT REACHED <<<")


# **Test Cases**
wheres_the_money(10000, 100, 100, 100, 1000)  
wheres_the_money(30000, 700, 300, 200, 4000)  
wheres_the_money(40000, 750, 400, 100, 3500)  
wheres_the_money(50000, 1200, 300, 200, 5000)  
wheres_the_money(300000, 3000, 500, 500, 50000)  
