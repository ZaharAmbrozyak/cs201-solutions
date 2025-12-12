def calculate_storage(value: float, start: str, end: str) -> tuple:
    UNITS_IN_BYTES = {
        "B": 1,
        "KB": 1024,
        "MB": 1024 ** 2,
        "GB": 1024 ** 3,
        "TB": 1024 ** 4
    }
    new_value = value*UNITS_IN_BYTES[start]/UNITS_IN_BYTES[end]
    return value, start, int(new_value), end

def format_report(report: tuple):
    value, start, new_value, end = report
    print(f"{value} {start} дорівнює {new_value} {end}")

format_report(calculate_storage(5, 'GB', 'MB'))