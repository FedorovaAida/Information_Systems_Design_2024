import re

class Patient:
    def __init__(self, patient_id, first_name, last_name, email, gender, phone, date_of_birth):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_gender(gender)
        self.set_phone(phone)
        self.set_date_of_birth(date_of_birth)

    # Getters
    def get_patient_id(self):
        return self.__patient_id
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_phone(self):
        return self.__phone
    def get_gender(self):
        return self.__gender
    def get_email(self):
        return self.__email
    def get_date_of_birth(self):
        return self.__date_of_birth

    # Setters
   def set_first_name(self, first_name):
        if not self.validate_name(first_name):
            raise ValueError("Имя должно быть непустой строкой.")
        self.__first_name = first_name
       
    def set_last_name(self, last_name):
        if not self.validate_name(last_name):
            raise ValueError("Фамилия должна быть непустой строкой.")
        self.__last_name = last_name
        
    def set_date_of_birth(self, date_of_birth):
        if not self.validate_date_of_birth(date_of_birth):
            raise ValueError("Дата рождения не может быть пустой.")
        self.__date_of_birth = date_of_birth    

    def set_email(self, email):
        if not self.validate_email(email):
            raise ValueError("Некорректный формат email.")
        self.__email = email

    def set_phone(self, phone):
        if not self.validate_phone(phone):
            raise ValueError("Неверный формат телефона.")
        self.__phone = phone


    # Функции валидации
    @staticmethod
    def validate_name(name):
        return isinstance(name, str) and bool(name.strip())

    @staticmethod
    def validate_date_of_birth(date_of_birth):
        return bool(date_of_birth)

    @staticmethod
    def validate_email(email):
        return "@" in email
    
    @staticmethod
    def validate_gender(gender):
        return isinstance(gender, str) and gender in ('м', 'ж'):)
    
    @staticmethod
    def validate_phone(phone):
        return sinstance(phone, str) and re.fullmatch(r'((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}', phone)
