import json
import os


class Student:

    def __init__(self, full_name: str, average_grade: float = None, finance_type: str = None) -> None:
        self.full_name = full_name
        self.average_grade = average_grade
        self.finance_type = finance_type

    def get_data(self) -> dict:
        data = {
            "full_name": self.full_name,
            "average_grade": self.average_grade,
            "finance_type": self.finance_type
        }
        return data


class JsonHandler:

    def __init__(self, filename: str = 'students_list.json') -> None:
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
        with open(self.filename, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                print("Error while trying to load json file")
                return []


    def add_item(self, item: dict) -> None:
        current_data = self.get_data()
        current_data.append(item)
        with open(self.filename, 'w') as file:
            json.dump(current_data, file, indent=4, ensure_ascii=False)


class DeansOffice:

    def __init__(self, handler: JsonHandler) -> None:
        self.handler = handler

    def assign_status(self, student: Student, grade: float, budget_threshold=85):
        student.average_grade = grade
        if grade >= budget_threshold:
            student.finance_type = "budget"
        else:
            student.finance_type = "contract"
        self.handler.add_item(student.get_data())


class ScholarshipAuditor:

    def __init__(self, handler: JsonHandler) -> None:
        self.handler = handler

    def check_scholarship(self) -> None:
        students = self.handler.get_data()

        if not students:
            print("There's no data to check")
            return

        students_budget = [student for student in students if student.get("finance_type") == 'budget']
        students_contract = [student for student in students if student.get("finance_type") == 'contract']

        if not students_contract or not students_budget:
            print("There's not enough data to compare")
            return

        max_grade_contract = max(student.get("average_grade") for student in students_contract)
        min_grade_budget = min(student.get("average_grade") for student in students_budget)

        if max_grade_contract < min_grade_budget:
            print("✅ Everything is correct.")
        else:
            print("⛔️ The rule is violated.")

            print(f"Maximum grade contract: {max_grade_contract}")
            for student in students_budget:
                if student.get("average_grade") < max_grade_contract:
                    print(f"Budget issue: {student.get('full_name')}, grade {student.get('average_grade')} < {max_grade_contract}.")

            print(f"Minimum grade budget: {min_grade_budget}")
            for student in students_contract:
                if student.get("average_grade") > min_grade_budget:
                    print(f"Contract issue: {student.get('full_name')}, grade {student.get('average_grade')} > {min_grade_budget}.")

if __name__ == "__main__":
    handler = JsonHandler()
    dean = DeansOffice(handler)
    auditor = ScholarshipAuditor(handler)

    student_1 = Student("Zahar Ambrozyak")
    student_2 = Student("Nazar Redko")
    student_3 = Student("Stanislav Tarasenko")

    dean.assign_status(student_1, 95)
    dean.assign_status(student_2, 84)
    dean.assign_status(student_3, 59)

    auditor.check_scholarship()

    print("Injecting unfair data:")

    student_4 = {"full_name": "Artem Korotenko", "average_grade": 999, "finance_type": "contract"}
    handler.add_item(student_4)
    auditor.check_scholarship()