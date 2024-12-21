import tkinter as tk
from AddUpdateController import AddUpdateController
from AddUpdatePatientView import AddUpdatePatientView
from tkinter import ttk, messagebox

class MainController:

    def __init__(self, model):
        self.model = model

    def get_patients(self, page_size, page_num):
        return self.model.get_patients(page_size, page_num)

    def open_add_patient_window(self, root):
        new_window = tk.Toplevel(root)
        AddUpdatePatientView(new_window, AddUpdateController(self.model), "add")

    def delete_patient(self, table):
        selected_item = table.selection()
        if not selected_item:
            messagebox.showwarning("Вы ничего не выбрали", "Выберите пациента для удаления")
            return
        # Получаем ID выбранного пациента
        patient_id = selected_item[0]
        self.model.delete_patient(patient_id)
        messagebox.showinfo("Завершено", "Пациента успешно удален!")

    def view_details(self, table, root):
        selected_item = table.selection()
        if not selected_item:
            messagebox.showwarning("Вы ничего не выбрали", "Выберите пациента для изменения")
            return
        patient_id = selected_item[0]
        patient_data = self.model.get_patient_by_id(patient_id)
        if patient_data:
            new_window = tk.Toplevel(root)
            AddUpdatePatientView(new_window, AddUpdateController(self.model), "update", patient_data)
        else:
            messagebox.showwarning("Ошибка", "Не удалось найти пациента в базе данных")
