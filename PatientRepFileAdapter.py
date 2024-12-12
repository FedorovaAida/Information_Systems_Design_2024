from PatientRepFile import PatientRepFile

class PatientRepFileAdapter:

    def __init__(self, patient_rep_file: PatientRepFile):
        patient_rep_file.read_data_from_file()
        self._patient_rep_file = patient_rep_file

    def get_k_n_short_list(self, k, n):
        return self._patient_rep_file.get_k_n_short_list(k, n)

    def get_by_id(self, id):
        return self._patient_rep_file.get_by_id(id)

    def delete_by_id(self, id):
        self._patient_rep_file.delete_by_id(id)
        self._patient_rep_file.write_data_to_file()

    def update_by_id(self, entity_id, first_name, last_name, email, gender, phone, disease):
        self._patient_rep_file.replace_by_id(entity_id, first_name, last_name, email, gender, phone, disease)
        self._patient_rep_file.write_data_to_file()

    def add(self, first_name, last_name, email, gender, phone, disease):
        self._patient_rep_file.add_entity(first_name, last_name, email, gender, phone, disease)
        self._patient_rep_file.write_data_to_file()

    def get_count(self):
        return self._patient_rep_file.get_count()
