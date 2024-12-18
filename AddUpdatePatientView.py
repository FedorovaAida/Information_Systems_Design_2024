import tkinter as tk
from tkinter import messagebox
from Patient import Patient

class AddUpdatePatientView:
    def __init__(self, root, controller, action, patient_data=None):
        self.controller = controller
        self.action = action
        self.patient_data = patient_data
        self.root = root

        # Поля ввода данных
        tk.Label(root, text="Фамилия").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.first_name_entry = tk.Entry(root, width=30)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Имя").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.last_name_entry = tk.Entry(root, width=30)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Email").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Пол (М/Ж)").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.gender_entry = tk.Entry(root, width=30)
        self.gender_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Телефон").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(root, text="Диагноз").grid(row=5, column=0, sticky="w", padx=10, pady=5)
        self.disease_entry = tk.Entry(root, width=30)
        self.disease_entry.grid(row=5, column=1, padx=10, pady=5)

        if patient_data != None:
            self.first_name_entry.insert(0, self.patient_data.get_first_name())
            self.last_name_entry.insert(0, self.patient_data.get_last_name())
            self.email_entry.insert(0, self.patient_data.get_email())
            self.gender_entry.insert(0, self.patient_data.get_gender())
            self.phone_entry.insert(0, self.patient_data.get_phone())
            self.disease_entry.insert(0, self.patient_data.get_disease())

        # Кнопка добавления пациента
        if action == "add":
            self.root.title("Добавить пациента")
            tk.Button(root, text="Добавить", command=self.add_update_patient).grid(row=7, column=0, columnspan=2, pady=10)
        else:
            if action == "update":
                self.root.title("Редактирование пациента")
                tk.Button(root, text="Сохранить изменения", command=self.add_update_patient).grid(row=7, column=0, columnspan=2, pady=10)

    def add_update_patient(self):
        try:
            # Получаем данные из полей ввода
            first_name = self.first_name_entry.get().strip()
            last_name = self.last_name_entry.get().strip()
            email = self.email_entry.get().strip().upper()
            gender = self.gender_entry.get().strip()
            phone = self.phone_entry.get().strip()
            disease = self.disease_entry.get().strip()

            # Вызываем метод контроллера для добавления пациента
            if self.action == "add":
                add_patient = Patient(first_name=first_name,
                    last_name=last_name,
                    email=email,
                    gender=gender,
                    phone=phone,
                    disease=disease)
                self.controller.add_patient(add_patient)
                messagebox.showinfo("Успех", "Пациент успешно добавлен!")
            else:
                if self.action == "update":
                    update_patient = Patient(id=self.patient_data.get_id(),
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        gender=gender,
                        phone=phone,
                        disease=disease)
                    self.controller.update_patient(update_patient)

                    messagebox.showinfo("Успех", "Данные пациента успешно обновлены!")
            # Уведомляем пользователя об успешном добавлении
            self.root.destroy()  # Закрываем окно добавления
        except ValueError as e:
            # Показываем ошибки валидации
            messagebox.showerror("Ошибка", str(e))
        except Exception as e:
            # Обработка других ошибок
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")
