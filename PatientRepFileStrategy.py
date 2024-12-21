from abc import ABC, abstractmethod


# Абстрактный базовый класс стратегии работы с файлами
class PatientRepFileStrategy(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass
