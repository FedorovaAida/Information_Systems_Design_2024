import uuid
import psycopg2.errors
from DatabaseConnection import DatabaseConnection


class PatientRepDB:

    def __init__(self, db_config):
        self.db = DatabaseConnection(db_config)

    def get_by_id(self, patient_id):
        from Patient import Patient
        with self.db.get_cursor() as cursor:
            cursor.execute("SELECT * FROM patient WHERE id = %s", (patient_id,))
            result = cursor.fetchone()
        if result:
            columns_names = [desc[0] for desc in cursor.description]
            patient = Patient(**dict(zip(columns_names, result)))
            return patient
        return None

    def get_k_n_short_list(self, k, n):
        from Patient import Patient
        with self.db.get_cursor() as cursor:
            cursor.execute("""
                SELECT id, first_name, last_name, email, gender, phone, disease FROM patient
                ORDER BY first_name, last_name, id LIMIT %s OFFSET %s
            """, (k, n))

            result = cursor.fetchall()
        columns_names = [desc[0] for desc in cursor.description]
        return[
            Patient(**dict(zip(columns_names, row)))
            for row in result
        ]

    def add(self, patient):
        new_id = str(uuid.uuid4())
        with self.db.get_cursor() as cursor:
            try:
                cursor.execute("""
                    INSERT INTO patient (id, first_name, last_name, email, gender, phone, disease)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (new_id,
                          patient.get_first_name(),
                          patient.get_last_name(),
                          patient.get_email(),
                          patient.get_gender(),
                          patient.get_phone(),
                          patient.get_disease()))
            except psycopg2.errors.UniqueViolation:
                raise ValueError('Email должен быть уникальным!')
        return new_id

    def update_by_id(self, patient):
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
        with self.db.get_cursor() as cursor:
            cursor.execute("DELETE FROM patient WHERE id = %s", (patient_id,))

    def get_count(self):
        with self.db.get_cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM patient")
            result = cursor.fetchone()
        return result[0]
