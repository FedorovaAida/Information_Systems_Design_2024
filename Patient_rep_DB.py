import uuid
from DatabaseConnection import DatabaseConnection

class PatientRepDB:
    """Класс для управления сущностью patient."""
    def __init__(self, db_config):
        self.db = DatabaseConnection(db_config)


    def get_by_id(self, patient_id):
        """Получить пациента по ID."""
        with self.db.get_cursor() as cursor:
            cursor.execute("SELECT * FROM patient WHERE id = %s", (patient_id,))
            result = cursor.fetchone()
        return result

    def get_k_n_short_list(self, k, n):
        """Получить список из k элементов, начиная с n-го блока."""
        with self.db.get_cursor() as cursor:
            offset = k * (n - 1)
            cursor.execute("""
                SELECT id, first_name, last_name, phone FROM patient
                ORDER BY id LIMIT %s OFFSET %s
            """, (k, offset))
            result = cursor.fetchall()
        return result

    def add(self, patient):
        """Добавить нового пациента."""
        new_id = str(uuid.uuid4())
        with self.db.get_cursor() as cursor:
            cursor.execute("""
                INSERT INTO patient (id, first_name, last_name, email, gender, phone, disease)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (new_id, patient.get_first_name(), patient.get_last_name(), patient.get_email(), patient.get_gender(), patient.get_phone(), patient.get_disease()))
        return new_id

    def update_by_id(self, patient):
        """Обновить данные пациента по ID."""
        fields = []
        values = []
        fields.append("first_name = %s")
        values.append(patient.get_first_name())
        fields.append("last_name = %s")
        values.append(patient.get_last_name())
        fields.append("email = %s")
        values.append(patient.get_email())
        fields.append("gender = %s")
        values.append(patient.get_gender())
        fields.append("phone = %s")
        values.append(patient.get_phone())
        fields.append("disease = %s")
        values.append(patient.get_disease())
        values.append(patient.get_id())
       
        with self.db.get_cursor() as cursor:
            cursor.execute(f"""
                UPDATE patient
                SET {', '.join(fields)}
                WHERE id = %s
            """, tuple(values))

    def delete_by_id(self, patient_id):
        """Удалить пациента по ID."""
        with self.db.get_cursor() as cursor:
            cursor.execute("DELETE FROM patient WHERE id = %s", (patient_id,))

    def get_count(self):
        """Получить количество записей в таблице."""
        with self.db.get_cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM patient")
            result = cursor.fetchone()
        return result[0]
