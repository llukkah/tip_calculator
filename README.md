# The Tip Calculator

### MVP

#### Make a python script (tip_calculator.py) that takes a user's input at the command line for:

- Cost of the food
- Assume there is a 10% sales tax and add to the total bill
- Number of people splitting the bill
- Percentage of the tip
- The script should output: The total bill (including tip) and how much each person should pay

---

### How to run the Tip Calculator

In your Terminal:

1. Clone this Repo with `git clone GITHUB URL`
2. `cd` into the Repo folder
3. Run `python3 tip_calculator.py`

---

### Cases the Tip Calculator should handle:

| Case Name                   | Food Costs | Number People Paying | Tip Amount | Expected Output | Total Bill     | Each Person Pays |
| --------------------------- | ---------- | -------------------- | ---------- | --------------- | -------------- | ---------------- |
| A Meal for 1                | $ 15       | 1                    | 20%        | ------->        | $19.50         | $19.50           |
| A feast to remember         | $25000000  | 3                    | 31%        | ------->        | $35,250,000.00 | $11,750,000.00   |
| No tip                      | $78.99     | 6                    | No Tip     | ------->        | $86.89         | $14.48           |
| Sharing the bill among many | $5000      | 876                  | 12%        | ------->        | $6,100.00      | $6.96            |
