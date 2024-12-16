class MainController:
    """Контроллер для главного окна"""
    def __init__(self, model):
        self.model = model
    def get_patientss(self, page_size, page_num):
        """Получить список пациентов для отображения на странице"""
        return self.model.get_patients(page_size, page_num)
    def delete_patient(self, patient_id):
        """Удалить пациента"""
        self.model.delete_patient(patient_id)
