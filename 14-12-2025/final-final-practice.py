import json
import os

class Transaction:

    def __init__(self, amount: float, operation_type: str) -> None:
        if isinstance(amount, float) or isinstance(amount, int):
            if amount > 0:
                self.amount = amount
            else:
                self.amount = 0
        else:
            raise TypeError("Invalid amount type! Must be either float or int!")
        valid_types = ['deposit', 'withdraw']
        if operation_type not in valid_types:
            raise ValueError(f"Invalid operation type! Must be one of: {', '.join(valid_types)}")
        self.operation_type = operation_type

    def get_data(self) -> dict:
        data = {
            "amount": self.amount,
            "type": self.operation_type
        }
        return data


class JsonHandler:

    def __init__(self, filename: str = 'transactions.json') -> None:
        if filename.endswith('.json'):
            self.filename = filename
        else:
            self.filename = filename + '.json'
        self.create_file()

    def create_file(self) -> None:
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump([], file)

    def get_data(self) -> list:

        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):
                    print("👥 Error! Data was corrupted, returning empty list")
                    return []
                return data
            except json.JSONDecodeError:
                print("🛑 Error occured when trying to get data from .json file")
                return []

    def add_item(self, item: dict) -> None:
        current_data = self.get_data()
        current_data.append(item)
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(current_data, file, ensure_ascii=False, indent=4)


class AccountManager:

    def __init__(self, json_handler: JsonHandler) -> None:
        self.json_handler = json_handler

    def process_transaction(self, transaction: Transaction) -> None:
        if transaction.operation_type == 'deposit':
            self.json_handler.add_item(transaction.get_data())
            print(f"✅ Transaction was successful. Deposit ${transaction.amount}")
        elif transaction.operation_type == 'withdraw':
            data = self.json_handler.get_data()
            deposits = [operation.get('amount', 0) for operation in data if operation.get("type") == 'deposit']
            withdraws = [operation.get('amount', 0) for operation in data if operation.get("type") == 'withdraw']
            deposit_sum = sum(deposits)
            withdraw_sum = sum(withdraws)
            if deposit_sum-withdraw_sum >= transaction.amount:
                self.json_handler.add_item(transaction.get_data())
                print(f"✅ Transaction was successful. Withdraw ${transaction.amount}")
            else:
                print('⛔️ Transaction failed. Not enough money to process')


class SecurityAuditor:

    def __init__(self, json_handler: JsonHandler):
        self.json_handler = json_handler

    def scan_for_suspicious_activity(self, limit=10000):
        data = self.json_handler.get_data()
        suspicious_transactions = 0
        for transaction in data:
            if transaction.get("amount", 0) > limit:
                print(f"⁉️ ALERT: Suspicious transaction found: {transaction.get('amount')} {transaction.get('type')}")
                suspicious_transactions += 1

        print(f"📊 Overall suspicious transactions: {suspicious_transactions}")

