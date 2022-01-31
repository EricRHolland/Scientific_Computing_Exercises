
"""
        problems (list[str]): Input list with problems
        calculate_solution Defaults to False.
"""


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
        for entry in self.ledger:
            items = ( "{entry.get('description')[:23]:23}"
            + "{entry.get('amount'):>7.2f}" + "\n")
        return title_row + items + "Total: " + "{self.income:.2f}"
        

def create_spend_chart(category_list):
    #Will be tested with up to 4 categories.
    for cat in category_list:
        if cat not in categories:



class Category:
    categorie : str
    ledger: List[Dict[str, Union[str, int, float]]] = field(default_factory = list)





    def deposit(self):

    def withdraw(self):

    def get_balance(self):

    def transfer(self):

    def check_funds(self):
