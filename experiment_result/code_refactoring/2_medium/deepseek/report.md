### Output

```python
import logging

# Global list to store account data
accounts = []

class Bank:
    def __init__(self, logger=None):
        # Use the provided logger or default to print
        self.logger = logger if logger else self._default_logger

    def _default_logger(self, message):
        """Default logger that uses print."""
        print(message)

    def _find_account(self, name):
        for acc in accounts:
            if acc["name"] == name:
                return acc
        return None

    def create_account(self, name, monies=0):
        if not self._find_account(name):
            accounts.append({
                "name": name,
                "monies": monies
            })
            self.logger(f"Account created for {name}")
        else:
            self.logger("An account already exists")

    def credit(self, name, amount):
        account = self._find_account(name)
        if account:
            account["monies"] += amount
            self.logger(f"{amount} credited to {name}")
        else:
            self.logger(f"Account {name} not found")

    def debit(self, name, amount):
        account = self._find_account(name)
        if account:
            account["monies"] -= amount
            self.logger(f"{amount} debited from {name}")
        else:
            self.logger(f"Account {name} not found")

    def get_funds(self, name):
        account = self._find_account(name)
        if account:
            return account["monies"]
        return "Account not found!"


# Example usage:
if __name__ == "__main__":
    # Development mode: Use print for logging
    bank_dev = Bank()
    bank_dev.create_account("John Doe")
    bank_dev.credit("John Doe", 100)
    bank_dev.debit("John Doe", 50)
    funds = bank_dev.get_funds("John Doe")
    print("John Doe's funds:", funds)

    # Production mode: Use a third-party logger
    logging.basicConfig(level=logging.INFO)
    bank_prod = Bank(logger=logging.info)
    bank_prod.create_account("Jane Doe")
    bank_prod.credit("Jane Doe", 200)
    bank_prod.debit("Jane Doe", 75)
    funds = bank_prod.get_funds("Jane Doe")
    print("Jane Doe's funds:", funds)

```

### Strength

Correctly refactors the code by implementing dependency injection to
decouple the logger functionality

### Weakness

It assumes the logger must be a function that takes only one string argument.
But this can be easily fixed with better prompt

### Screenshot

![alt text](image.png)
