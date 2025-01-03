from PatientRepFile import PatientRepFile

class PatientRepFileAdapter:

    def __init__(self, patient_rep_file: PatientRepFile):
        patient_rep_file.read()
        self._patient_rep_file = patient_rep_file

    def get_k_n_short_list(self, k, n):
        return self._patient_rep_file.get_k_n_short_list(k, n)

    def get_by_id(self, id):
        return self._patient_rep_file.get_by_id(id)

    def delete_by_id(self, id):
        self._patient_rep_file.delete_by_id(id)
        self._patient_rep_file.write()

    def update_by_id(self, patient):
        self._patient_rep_file.replace_by_id(patient)
        self._patient_rep_file.write()

    def add(self, patient):
        self._patient_rep_file.add_entity(patient)
        self._patient_rep_file.write()

    def get_count(self):
        return self._patient_rep_file.get_count()
