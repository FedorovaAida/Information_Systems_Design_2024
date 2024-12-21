from PatientRepFileStrategy import PatientRepFileStrategy
from BasePatient import BasePatient

# Класс, который использует стратегию для работы с файлами
class PatientRepFile:

    def __init__(self, strategy: PatientRepFileStrategy):
        self._data = []
        self._strategy = strategy

    def write(self):
        self._strategy.write(self._data)

    def read(self):
        self._data = self._strategy.read()

    def add_entity(self, first_name, last_name, email, gender, phone, disease):
        from Patient import Patient
        # Генерация нового ID
        new_id = max([entry['id'] for entry in self._data], default=0) + 1
        new_patient = Patient(
            id=new_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender,
            phone=phone,
            disease=disease
        )
        # Проверка на уникальность почты
        if any(entry == new_patient for entry in self._data):
            raise ValueError('Email должен быть уникальным!')
        # Добавляем нового пациента в список
        self._data.append(new_patient)

    def get_by_id(self, patient_id):
        for entry in self._data:
            if entry.get_id() == patient_id:
                return entry
        return None  # Если объект не найден

    def get_k_n_short_list(self, k, n):
        data = self._data.copy()

        start = (n - 1) * k
        end = start + k
        page_data = data[start:end]

        # Преобразуем в BasePatient
        return [
            BasePatient(
                id=patient['id'],
                first_name=patient['first_name'],
                last_name=patient['last_name'],
                email=patient['email']
            )
            for patient in page_data
        ]

    def sort_by_field(self, field):
        if field in ["first_name", "last_name", "email"]:
            self._data.sort(key=lambda x: x.get(field))
        return self._data

    def replace_by_id(self, entity_id, first_name, last_name, email, gender, phone, disease):
        entity = self.get_by_id(entity_id)
        if not entity:
            raise ValueError(f"Пациент с ID {entity_id} не найден.")

        # Проверка на уникальность почты
        patient = BasePatient(first_name=first_name, last_name=last_name, email=email)
        if any(entry == patient for entry in self._data):
            raise ValueError('Email должен быть уникальным!')
        # Обновляем данные
        if first_name:
            entity.set_first_name(first_name)
        if last_name:
            entity.set_last_name(last_name)
        if email is not None:
            entity.set_email(email)
        if gender:
            entity.set_gender(gender)
        if phone:
            entity.set_phone(phone)
        if disease:
            entity.set_disease(disease)


    def delete_by_id(self, entity_id):
        entity = self.get_by_id(entity_id)
        if not entity:
            raise ValueError(f"Пациент с ID {entity_id} не найден.")
        self._data.remove(entity)

    def get_count(self):
        return len(self._data)
