# Zahar Ambrozyak property
import json
import os


class Car:
    def __init__(self, model: str, max_speed: float = None, status: str = None) -> None:

        self.statuses = ["sport", "regular"]
        self.model = model


        self.max_speed = max_speed
        self.status = status

    def get_info(self) -> dict:
        data = {
            "model": self.model,
            "max_speed": self.max_speed,
            "status:": self.status
        }
        return data


class JsonStorage:
    def __init__(self, filename: str = 'cars.json') -> None:
        if filename.endswith('.json'):
            self.filename = filename
        else:
            self.filename = 'output.json'
        self.create_file()

    def create_file(self) -> None:
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump([], file)

    def read_data(self) -> list:
        with open(self.filename, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                return []
            except json.JSONDecodeError:
                return []

    def add_item(self, item: dict) -> None:
        current_data = self.read_data()
        current_data.append(item)

        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(current_data, file, indent=4, ensure_ascii=False)


class CarClassifier:
    def __init__(self, storage: JsonStorage) -> None:
        self.storage = storage

    def classify(self, car: Car, max_speed: float, sport_speed: float = 200) -> None:
        car.max_speed = max_speed
        if max_speed >= sport_speed:
            car.status = "sport"
        else:
            car.status = "regular"

        self.storage.add_item(car.get_info())


class ClassicationChecker:
    def __init__(self, storage: JsonStorage):
        self.storage = storage

    def check_fairness(self):
        data = self.storage.read_data()

        if not data:
            print("Error. There's no data")
            return

        sport_cars = [car for car in data if car.get("status") == "sport"]
        regular_cars = [car for car in data if car.get("status") == "regular"]

        if not sport_cars or not regular_cars:
            print("There's not enough data to compare")
            return

        max_regular_speed = max(car["max_speed"] for car in regular_cars)
        min_sport_speed = min(car["max_speed"] for car in sport_cars)

        if max_regular_speed < min_sport_speed:
            print("✅ Everything is correct.")
        else:
            print("⛔️ The rule is violated.")
            print(f"Minimal sport car speed: {min_sport_speed}")
            for car in regular_cars:
                if car["max_speed"] >= min_sport_speed:
                    print(f"Regular car issue: {car['model']} (Speed: {car['max_speed']} => {min_sport_speed})")

            print(f"Maximal regular car speed: {max_regular_speed}")
            for car in sport_cars:
                if car["max_speed"] <= max_regular_speed:
                    print(f"Sport car issue: {car['model']} (Speed: {car['max_speed']} <= {max_regular_speed}")

if __name__ == "__main__":
    pass