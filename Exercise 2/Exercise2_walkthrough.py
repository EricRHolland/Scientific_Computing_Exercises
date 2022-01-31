
"""
        problems (list[str]): Input list with problems
        calculate_solution Defaults to False.
"""







# Ledger will contain a list of tuples

class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
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
        if not self.check_funds(amount):
            return False

        self.balance = self.balance - amount

        self.ledger.append({
            'amount' : -amount,
            'description' : description,
            })
        return True

    def get_balance(self):
        return self.balance

    def

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
