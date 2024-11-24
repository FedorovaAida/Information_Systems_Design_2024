import re

class Patient:
    def __init__(self, patient_id, first_name, last_name, email, gender, phone, date_of_birth):
        self.__patient_id = patient_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__gender = gender
        self.__phone = phone
        self.__date_of_birth = date_of_birth
    
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
        self.__first_name = first_name
    def set_last_name(self, last_name):
        self.__last_name = last_name
    def set_phone(self, phone):
        self.__phone = phone
    def set_gender(self, gender):
        self.__gender = gender
    def set_email(self, email):
        self.__email = email
    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth
