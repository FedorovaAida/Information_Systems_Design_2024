from Patient_rep_DB import PatientRepDB
from PatientModel import PatientModel
from MainView import MainView
from MainController import MainController
import tkinter as tk
if __name__ == "__main__":
    # Подключение к базе данных
    db_config = {
        'dbname': "DiagramClasses",
        'user': "postgres",
        'password': "123456789",
        'host': "localhost",
        'port': 5432
    }
    # Создание репозитория и модели
    repository = PatientRepDB(db_config)
    model = PatientModel(repository)
    # Создание и запуск главного окна
    root = tk.Tk()
    main_controller = MainController(model)
    MainView(root, main_controller)
    root.mainloop()
