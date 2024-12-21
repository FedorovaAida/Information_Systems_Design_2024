import yaml
import os
from PatientRepFileStrategy import PatientRepFileStrategy

# Стратегия работы с YAML
class PatientRepYamlStrategy(PatientRepFileStrategy):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = yaml.safe_load(f)
                return data
        return []

    def write(self, data):
        with open(self.filename, 'w') as f:
            yaml.dump(data, f, default_flow_style=False)
