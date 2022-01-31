## Eric H creation from January 2022 - completed
# Ledger will contain a list of tuples

class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.spent = 0.0
        self.ledger = []

    def check_funds(self, amount):
        return self.balance >= amount

    def deposit(self, amount, description=""):
        self.ledger.append({
            'amount': amount,
            'description': description,
            })
        self.balance = self.balance + amount

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.balance = self.balance - amount
            self.spent = self.spent + amount
            self.ledger.append({
                'amount' : -amount,
                'description' : description,
                })
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self,amount,other_category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to" + other_category.name)
            other_category.deposit(amount, "Transfer from" + self.name)
            return True
        else:
            return False

    def __str__(self):
        title_row = self.category_list.center(30,"*") + "\n"
        items = ""
        for entry in self.ledger
        stringtit = [self.name.center(30,"*")]

        ### redo this because I'm not even sure if it is correct.
        for entry in self.ledger:
            items = ( "{entry.get('description')[:23]:23}"
            + "{entry.get('amount'):>7.2f}" + "\n")
        return title_row + items + "Total: " + "{self.income:.2f}"


def create_spend_chart(category_list):
    #Will be tested with up to 4 categories.
    plot = "Percentage spent by category\n"

    total_spent = sum(a.spent for a in category_list)

    percentages = [(a.spent / total_spent) / 0.01 for a in category_list]

    for p_value in range (100,-10,-10):
        plot += str(p_value).rjust(3, " ") + "|"
        for percentage in percentages:
            if percentage >= p_value:
                plot = plot + " o "
            else:
                plot += " " * 3

        plot = plot + " \n"

    ## Create the x axis after you figure out what's going on above this.
    plot = plot + " " * 4 + "-" * 3 * len(pencentages) + "-\n"

    ## base it off the length of the longest category.
    longest_name = max(len(a.name) for a in category_list)

    for ch in range(longest_name):
        #start with 4 spaces? Why do we have to start with 4 spaces?
        plot = plot + " " * 4

        for namer in category_list:
            #attach namer to the row to get the vertical names
            if ch < len(namer.name):
                plot += " " + namer.name[ch] + " "
            else:
                # If there is nothing attached, add 3 spaces so it's the end of the line
                plot += " " * 3
        plot += " \n"

    plot = plot.rstrip() + " " * 2

    return plot
