# Шаблон проектирования Наблюдатель, где объект PatientModel уведомляет наблюдателей об изменениях
class Observable:
    # Класс для наблюдателей, другие классы могут подписаться на изменения в этом объекте,
    # и быть уведомлены при их изменении
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, action, data):
        # Уведомляет всех наблюдателей в списке, вызывая у них метод update,
        # передавая тип действия action и данные data
        for observer in self._observers:
            observer.update(action, data)


class PatientModel(Observable):
    def __init__(self, repository):
        # Инициализируем список наблюдателей, передается репозиторий,
        # который отвечает за работу с бд или файлами
        super().__init__()
        self._repository = repository

    def get_patients(self, page_size, page_num):
        offset = (page_num - 1) * page_size
        return self._repository.get_k_n_short_list(page_size, offset)

    def get_patient_by_id(self, patient_id):
        return self._repository.get_by_id(patient_id)

    def add_patient(self, patient):
        patient_id = self._repository.add(patient)
        self.notify_observers("add", {"id": patient_id, "first_name": patient.get_first_name(), "last_name": patient.get_last_name()})

    def update_patient(self, patient):
        self._repository.update_by_id(patient)
        self.notify_observers("update", {"id": patient.get_id(), "first_name": patient.get_first_name(), "last_name": patient.get_last_name()})

    def delete_patient(self, patient_id):
        self._repository.delete_by_id(patient_id)
        self.notify_observers("delete", {"id": patient_id})

    def get_count(self):
        return self._repository.get_count()
