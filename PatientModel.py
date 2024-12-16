class Observable:

    """Класс для реализации паттерна Наблюдатель"""
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        """Добавить наблюдателя"""
        self._observers.append(observer)

    def remove_observer(self, observer):
        """Удалить наблюдателя"""
        self._observers.remove(observer)

    def notify_observers(self, action, data):
        """Уведомить всех наблюдателей"""
        for observer in self._observers:
            observer.update(action, data)

class PatientModel(Observable):

    """Модель для управления пациентами"""
    def __init__(self, repository):
        super().__init__()
        self._repository = repository

    def get_patients(self, page_size, page_num):
        """Получить список пациентов для отображения на странице"""
        offset = (page_num - 1) * page_size
        return self._repository.get_k_n_short_list(page_size, offset)

    def get_patient_by_id(self, patient_id):
        """Получить пациента по ID"""
        return self._repository.get_by_id(patient_id)

    def add_patient(self, first_name, last_name, email, gender, phone, disease):
        """Добавить нового пациента и уведомить наблюдателей"""
        client_id = self._repository.add(
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender,
            phone=phone,
            disease=disease
        )
        self.notify_observers("add", {"id": client_id, "first_name": first_name, "last_name": last_name})

    def update_patient(self, patient_id, first_name, last_name, email, gender, phone, disease):
        """Обновить данные пациента и уведомить наблюдателей"""
        self._repository.update_by_id(patient_id, first_name, last_name, email, gender, phone, disease)
        self.notify_observers("update", {"id": patient_id, "first_name": first_name, "last_name": last_name})

    def delete_patient(self, patient_id):
        """Удалить пациента и уведомить наблюдателей"""
        self._repository.delete_by_id(patient_id)
        self.notify_observers("delete", {"id": patient_id})

    def get_count(self):
        return self._repository.get_count()
