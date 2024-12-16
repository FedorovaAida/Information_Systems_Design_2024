from Patient import Patient
class AddUpdatePatientController:
    """Контроллер для добавления пациента"""
    def __init__(self, model):
        self.model = model
    @staticmethod
    def validate_data(first_name, last_name, email, gender, phone, disease):
        """Использует функции из Patient и BasePatient для валидации данных"""
        errors = []
        if not Patient.validate_name(first_name):
            errors.append("Фамилия не может быть пустой или некорректной.")
        if not Patient.validate_name(last_name):
            errors.append("Фамилия не может быть пустой или некорректной.")
        if not Patient.validate_email(email):
            errors.append("Некорректный e-mail.")
        if not Patient.validate_gender(gender):
            errors.append("Пол должен быть указан как 'М' или 'Ж'.")
        if not Patient.validate_phone(phone):
            errors.append("Некорректный номер телефона.")
        if not Patient.validate_disease(disease):
            errors.append("Диагноз должен быть корректной строкой.")
        if errors:
            raise ValueError("\n".join(errors))

    def add_patient(self, first_name, last_name, email, gender, phone, disease):
        """Добавить пациента после валидации"""
        # Валидация данных
        self.validate_data(first_name, last_name, email, gender, phone, disease)
        # Если данные корректны, вызываем метод модели для добавления пациента
        self.model.add_patient(
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender,
            phone=phone,
            disease=disease
        )
    def update_patient(self, id, first_name, last_name, email, gender, phone, disease):
        """Добавить пациента после валидации"""
        # Валидация данных
        self.validate_data(first_name, last_name, email, gender, phone, disease)
        # Если данные корректны, вызываем метод модели для корректирования пациента
        self.model.update_patient(
            patient_id=id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender,
            phone=phone,
            disease=disease
        )
