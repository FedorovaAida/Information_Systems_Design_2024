import json
import os
from PatientRepFileStrategy import PatientRepFileStrategy


# Стратегия работы с JSON
class PatientRepJsonStrategy(PatientRepFileStrategy):

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return data
        return []

    def write(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
