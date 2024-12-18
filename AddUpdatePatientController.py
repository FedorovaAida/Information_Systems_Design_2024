from Patient import Patient


class AddUpdateController:

    def __init__(self, model):
        self.model = model

    @staticmethod
    def validate_data(patient):
        errors = []
        if not Patient.validate_name(patient.get_first_name()):
            errors.append("Фамилия не может быть пустой или некорректной.")
        if not Patient.validate_name(patient.get_last_name()):
            errors.append("Имя не может быть пустым или некорректным.")
        if not Patient.validate_email(patient.get_email()):
            errors.append("Некорректный email")
        if not Patient.validate_gender(patient.get_gender()):
            errors.append("Пол должен быть указан как 'М' или 'Ж'.")
        if not Patient.validate_phone(patient.get_phone()):
            errors.append("Некорректный номер телефона.")
        if not Patient.validate_disease(patient.get_disease()):
            errors.append("Диагноз не может быть пустым или некорректным.")
        if errors:
            raise ValueError("\n".join(errors))

    def add_patient(self, patient):
        # Валидация данных
        self.validate_data(patient)
        # Если данные корректны, вызываем метод модели для добавления клиента
        self.model.add_patient(patient)

    def update_patient(self, patient):
        # Валидация данных
        self.validate_data(patient)
        # Если данные корректны, вызываем метод модели для корректирования клиента
        self.model.update_patient(patient)
