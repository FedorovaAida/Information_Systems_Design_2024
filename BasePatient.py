import re
from datetime import datetime

# Базовый класс для пациента с общей логикой
class BasePatient():
    def __init__(self, first_name, last_name, email, patient_id=None):
        self.__patient_id = patient_id
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)

    # Геттеры
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    # Сеттеры
    def set_first_name(self, first_name):
        if not self.validate_name(first_name):
            raise ValueError("Имя должно быть непустой строкой.")
        self.__first_name = first_name

    def set_last_name(self, last_name):
        if not self.validate_name(last_name):
            raise ValueError("Фамилия должна быть непустой строкой.")
        self.__last_name = last_name

    def set_email(self, email):
        if not self.validate_email(email):
            raise ValueError("Некорректный формат email.")
        self.__email = email

    # Функции валидации
    @staticmethod
    def validate_name(name):
        return isinstance(name, str) and bool(name.strip())

    @staticmethod
    def validate_email(email):
        return "@" in email


    # Сравнение объектов на равенство
    def __eq__(self, other):
        if self.get_first_name() != other.get_first_name() and self.get_last_name() != other.get_last_name() and self.get_email() != other.get_email():
            return False
        return True


    def __hash__(self):
        return hash(self.get_first_name(), self.get_last_name(), self.get_email())


    def __str__(self):
        return f"Patient name is {self.get_first_name()} {self.get_last_name()}, (email: {self.get_email()})"


    def __repr__(self):
        return f"Name:{self.get_first_name()} {self.get_last_name()}, email: {self.get_email()})"
