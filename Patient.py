import re
import json
from datetime import datetime
from BasePatient import BasePatient


# Полная версия класса пациента
class Patient(BasePatient):
    def __init__(self, first_name, last_name, email, gender, phone, date_of_birth, patient_id=None):
        super(Patient, self).__init__(first_name, last_name, email, patient_id)
        self.set_gender(gender)
        self.set_phone(phone)
        self.set_date_of_birth(date_of_birth)

    # Классовый метод создания клиента из JSON
    @classmethod
    def from_json(data_json):
        try:
            data = json.loads(data_json)
            date_of_birth = datetime.strptime(data['date_of_birth'].strip(), "%Y-%m-%d").date()
            return Patient(
                patient_id=data['patient_id'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                gender=data['gender'],
                phone=data['phone'],
                date_of_birth=date_of_birth
            )
        except Exception as e:
            raise ValueError("Данные JSON не верны")

    # Геттеры
    def get_phone(self):
        return self.__phone

    def get_gender(self):
        return self.__gender

    def get_date_of_birth(self):
        return self.__date_of_birth

    # Сеттеры
    def set_date_of_birth(self, date_of_birth):
        if not self.validate_date_of_birth(date_of_birth):
            raise ValueError("Дата рождения не может быть пустой.")
        self.__date_of_birth = date_of_birth

    def set_phone(self, phone):
        if not self.validate_phone(phone):
            raise ValueError("Неверный формат телефона.")
        self.__phone = phone

    def set_gender(self, gender):
        if not self.validate_gender(gender):
            raise ValueError("Пол должен быть 'м' или 'ж'.")
        self.__gender = gender

    # Функции валидации
    @staticmethod
    def validate_date_of_birth(date_of_birth):
        return bool(date_of_birth)

    @staticmethod
    def validate_gender(gender):
        return isinstance(gender, str) and gender in ('м', 'ж')

    @staticmethod
    def validate_phone(phone):
        return isinstance(phone, str) and re.fullmatch(r'((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}', phone)

    # Строковое представление для краткой версии объекта
    @property
    def short_version(self):
        return f"Patient({self.get_first_name()} {self.get_last_name()})"

    # Представление для полной версии объекта
    @property
    def full_version(self):
        return (
            f"first_name={self.get_first_name()}, last_name={self.get_last_name()}, date_of_birth={self.get_date_of_birth()}, email={self.get_email()},"
            f"gender={self.get_gender()}, phone={self.get_phone()})")

pat1= Patient('Fedorova', 'Aida', 'fedorovaaida05@gmail.com', 'ж', '89094687845', '16.05.2003')
print(pat1.__str__())
pat1.set_first_name('Shulga')
print(pat1.__str__())
print(pat1.__first_name)
