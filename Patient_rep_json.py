import json
import os

class PatientRepJson:
    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        """Прочитать данные из JSON файла"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return data
        return []
    
    def write(self, data):
        """Записать данные в JSON файл"""
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
          
    def add_entity(self, first_name, last_name, email, gender, phone, date_of_birth):
        """Добавить нового пациента в список с новым ID"""
        # Чтение данных из файла
        data = self.read()
        # Генерация нового ID
        new_id = max([entry['patient_id'] for entry in data], default=0) + 1
        new_entity = {
            'patient_id': new_id,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'gender': gender,
            'email': email,
            'phone': phone,
            'date_of_birth': date_of_birth
        }
      
        # Проверка на уникальность почты
        if any(entry['email'] == email for entry in data):
            raise ValueError('Email должен быть уникальным!')          
        # Добавляем нового пациента в список
        data.append(new_entity)
        # Записываем обновленные данные в файл
        self.write(data)
      
    def get_by_id(self, patient_id):
        """Получить пациента по ID"""
        data = self.read()
        for entry in data:
            if entry['patient_id'] == patient_id:
                return entry
        return None  # Если объект не найден
      
    def get_k_n_short_list(self, k, n):
        """Получить список k по счету n объектов"""
        data = self.read()
        start = (n - 1) * k
        end = start + k
        return data[start:end]
      
    def sort_by_field(self, field):
        """Сортировать элементы по выбранному полю"""
        data = self.read()
        if field in ["first_name", "last_name", "email", "date_of_birth"]:
            data.sort(key=lambda x: x.get(field))
        return data
      
    def replace_by_id(self, patient_id, first_name, last_name, email, gender, phone, date_of_birth):
        """Заменить данные пациента по ID"""
        data = self.read()
        entity = self.get_by_id(patient_id)
        if not entity:
            raise ValueError(f"Пациент с ID {patient_id} не найден.")
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
        if date_of_birth:
            entity['date_of_birth'] = date_of_birth
        # Записываем обновленные данные в файл
        self.write(data)
          
    def delete_by_id(self, patient_id):
            """Удалить пациента по ID"""
            data = self.read()
            entity = self.get_by_id(patient_id)
            if not entity:
                raise ValueError(f"Пациент с ID {patient_id} не найден.")
            data.remove(entity)
            self.write(data)
      
    def get_count(self):
            """Получить количество пациентов"""
            data = self.read()
            return len(data)
