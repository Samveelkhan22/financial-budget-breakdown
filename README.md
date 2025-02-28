# Financial Budget Breakdown

## 📌 Project Overview
This Python script calculates an individual's financial breakdown based on their **annual salary** and major expenses. It provides a structured **table output** showing the percentage allocation of income to different categories, including **rent, bills, food, travel, tax, and extra savings**.

## 🚀 Features
- **Accurate tax calculation** based on income brackets.
- **Breakdown of expenses** in a formatted table.
- **Graphical representation** using `#` to visualize spending.
- **Deficit warning system** when expenses exceed income.
- **Custom separator length** for neat console output.

## 📝 How It Works
1. The script takes in:
   - **Annual Salary**
   - **Monthly Rent**
   - **Monthly Bills**
   - **Weekly Food Expense**
   - **Annual Travel Cost**
2. It calculates:
   - **Annual Tax** (based on predefined brackets)
   - **Total Expenses**
   - **Remaining Savings (Extra)**
3. It prints a **formatted table** showing the financial breakdown.

## 📊 Tax Brackets
| Salary Range ($)     | Tax Rate (%) |
|----------------------|-------------|
| 0 - 15,000          | 10%         |
| 15,001 - 75,000     | 20%         |
| 75,001 - 200,000    | 25%         |
| 200,001 - 499,999   | 25%         |
| 500,000+            | 15%         |

## 🖥️ Example Usage
```python
from financial_breakdown import wheres_the_money

wheres_the_money(500000, 1000, 50, 50, 1000)
```

## 💡 Expected Output

```
---------------------------------------------------------
See the financial breakdown below, based on a salary of $500000
---------------------------------------------------------
| mortgage/rent | $  12,000.00 |   2.4% | ##
|         bills | $     600.00 |   0.1% | 
|          food | $   2,600.00 |   0.5% | 
|        travel | $   1,000.00 |   0.2% | 
|           tax | $  75,000.00 |  15.0% | ###############
|         extra | $ 408,800.00 |  81.8% | #################################################################################
---------------------------------------------------------
>>> TAX LIMIT REACHED <<<
```

## 🧪 Running Test Cases

```
wheres_the_money(10000, 100, 100, 100, 1000)  # Expected output: 94 dashes
wheres_the_money(30000, 700, 300, 200, 4000)  # Expected output: 76 dashes
wheres_the_money(40000, 750, 400, 100, 3500)  # Expected output: 65 dashes
wheres_the_money(50000, 1200, 300, 200, 5000)  # Expected output: 70 dashes
wheres_the_money(300000, 3000, 500, 500, 50000)  # Expected output: 77 dashes

```

## 🛠️ Future Improvements
-  Add a GUI interface for better user interaction.
-  Provide CSV export of the financial breakdown.
-  Integrate inflation adjustments for better projections.

