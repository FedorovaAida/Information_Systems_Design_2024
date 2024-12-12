import os
from PatientRepFileStrategy import PatientRepFileStrategy

# Класс, который использует стратегию для работы с файлами
class PatientRepFile:
    
    def __init__(self, strategy: PatientRepFileStrategy):
        self.strategy = strategy
    
    def get_all(self):
        """Получить все элементы"""
        return self.strategy.read()
    
    def add_entity(self, first_name, last_name, email, gender, phone, disease):      
        """Добавить нового пациента в список с новым ID"""
        # Чтение данных из файла
        data = self.strategy.read()
        # Генерация нового ID
        new_id = max([entry['id'] for entry in data], default=0) + 1   
        new_entity = {
            'id': new_id,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'gender': gender,
            'email': email,
            'phone': phone,
            'disease': disease
        }
        # Проверка на уникальность почты
        if any(entry['email'] == email for entry in data):
            raise ValueError('Email должен быть уникальным!')       
        # Добавляем нового пациента в список
        data.append(new_entity)      
        # Записываем обновленные данные в файл
        self.strategy.write(data)

    def get_by_id(self, patient_id):
        """Получить пациента по ID"""
        data = self.strategy.read()
        for entry in data:
            if entry['id'] == id:
                return entry
        return None  # Если объект не найден

    def get_k_n_short_list(self, k, n):
        """Получить список k по счету n объектов"""
        data = self.strategy.read()
        start = (n - 1) * k
        end = start + k
        return data[start:end]

    def sort_by_field(self, field):
        """Сортировать элементы по выбранному полю"""
        data = self.strategy.read()
        if field in ["first_name", "last_name", "email"]:
            data.sort(key=lambda x: x.get(field))
        return data

    def replace_by_id(self, entity_id, first_name, last_name, email, gender, phone, disease):
        """Заменить данные пациента по ID"""
        data = self.strategy.read()
        entity = self.get_by_id(entity_id)
        if not entity:
            raise ValueError(f"Пациент с ID {entity_id} не найден.")
        # Проверка на уникальность почты
        if email and email != entity['email'] and any(entry['email'] == email for entry in data):
            raise ValueError('Email должен быть уникальным!')
        # Обновляем данные
        if first_name:
            entity['first_name'] = first_name
        if last_name:
            entity['last_name'] = last_name
        if email is not None:
            entity['email'] = email
        if gender:
            entity['gender'] = gender
        if phone:
            entity['phone'] = phone
        if disease:
            entity['disease'] = disease
        # Записываем обновленные данные в файл
        self.strategy.write(data)

    def delete_by_id(self, entity_id):
        """Удалить пациента по ID"""
        data = self.strategy.read()
        entity = self.get_by_id(entity_id)
        if not entity:
            raise ValueError(f"Пациент с ID {entity_id} не найден.")
        data.remove(entity)
        self.strategy.write(data)

    def get_count(self):
            """Получить количество элементов"""
            data = self.strategy.read()
            return len(data)
