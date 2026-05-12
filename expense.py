# CEO Expense Tracker - Saakya Bhagavathula | 19/07/2008 | Data Science
# Mission: "Bank balance > I love you" 😌👑
# Built: 12/05/2026 | 10PM Birth Energy | First Python App

print("=== CEO MODE: EXPENSE TRACKER ===")
print("Rule 1: Track every rupee. Billionaires do.\n")

expenses = []

while True:
    item = input("Expense item (type 'done' to finish): ")
    if item.lower() == 'done':
        break
    cost = float(input(f"₹ Cost of {item}: "))
    expenses.append(cost)
    print(f"✅ Logged: {item} - ₹{cost}\n")

total = sum(expenses)

if total > 200:
    print("💸 NKR says: Control the chase rate, Saakya.")
else:
    print("💎 Saakya says: Bank balance > I love you.")

print("\n=== CEO REPORT ===")
print(f"Total transactions: {len(expenses)}")
print(f"Total spent: ₹{total}")
print("Saakya, you just did what 99% of 17yos don't. You faced your money.")
avg = total / len(expenses) if expenses else 0
print(f"📊 Average spend: ₹{avg:.2f}")
