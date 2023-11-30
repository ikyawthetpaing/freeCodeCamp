class Category:
    def __init__(self, name) -> None:
        self.name = name
        self.balance = 0.0
        self.ledger = []

    def deposit(self, amount, description=""):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if (self.check_funds(amount)):
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, category):
        if (self.check_funds(amount)):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
    
    def check_funds(self, amount):
        return not amount > self.balance
    
    def debug(self):
        print(f"{self.name}")

    def __str__(self) -> str:
        title_line = "*" * ((30 - len(self.name)) // 2)
        result = title_line + self.name + title_line + "\n"
        for ledger in self.ledger:
            description = ledger["description"][0:23]
            amount = format(ledger["amount"], ".2f")
            result += description + (" " * (30 - (len(description) + len(amount)))) + amount + "\n"
        result += f"Total: {self.balance}"
        return result


def create_spend_chart(categories):
    total_spent = 0.0
    categories_spent = []
    longest_name_len = max(len(category.name) for category in categories)

    for category in categories:
        spent = sum(ledger["amount"] * -1 for ledger in category.ledger if ledger["amount"] < 0)
        total_spent += spent
        categories_spent.append({"name": category.name, "amount": spent})

    chart = "Percentage spent by category\n"
    for percentage in range(100, -1, -10):
        chart += f"{percentage: >3}| "
        for category_spent in categories_spent:
            percentage_spent = category_spent["amount"] / total_spent * 100
            chart += "o  " if percentage_spent >= percentage else "   "
        chart += "\n"

    chart += "    " + "---" * len(categories_spent) + "-\n"

    for i in range(longest_name_len):
        chart += "    "
        for category_spent in categories_spent:
            char = category_spent["name"][i] if i < len(category_spent["name"]) else " "
            chart += f" {char} "

        if (i < longest_name_len - 1):
            chart += " \n"
        else:
            chart += " "

    return chart