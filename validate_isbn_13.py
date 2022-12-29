from main import isbn13
import re


#  регулярное выражение для проверки правильности структуры значения ISBN13, генерируемого модулем Faker
reg_expression = r"(?P<prefix>97[89])[- ](?P<registration>\d{1,5})[- ](?P<registrator>\d{1,7})[- ](?P<publication>\d{1,6})[- ](?P<control_number>[0-9X])"
pattern = re.compile(reg_expression)

if __name__ == "__main__":
    for _ in range(1000000):
        if not pattern.fullmatch(isbn13()):
            raise ValueError("Номер ISBN не соответствует структуре ISBN13")
