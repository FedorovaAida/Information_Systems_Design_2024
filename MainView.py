import tkinter as tk
from AddUpdatePatientController import AddUpdatePatientController
from AddUpdatePatientView import AddUpdatePatientView
from tkinter import ttk, messagebox

class MainView:
    """Главное окно для отображения списка клиентов"""
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Список пациентов")
        # Подписываем MainView на изменения модели
        self.controller.model.add_observer(self)
        # Создаем таблицу с колонками для отображения пациентов
        self.table = ttk.Treeview(
            root,
            columns=('№', 'Фамилия', 'Имя', 'Пол', 'E-mail', 'Телефон'),
            show='headings'
        )
        self.table.heading('№', text='№')
        self.table.heading('Фамилия', text='Фамилия')
        self.table.heading('Имя', text='Имя')
        self.table.heading('E-mail', text='E-mail')
        self.table.heading('Пол', text='Пол')
        self.table.heading('Телефон', text='Телефон')
        self.table.pack(fill=tk.BOTH, expand=True)
        # Кнопки для добавления, изменения и удаления пациента
        button_frame = tk.Frame(root)
        button_frame.pack(fill="x",pady=10)
        add_button = tk.Button(button_frame, text="Добавить пациента", command=self.open_add_patient_window)
        add_button.pack(side="left", pady=10)
        delete_button = tk.Button(button_frame, text="Удалить пациента", command=self.delete_patient)
        delete_button.pack(side="left", pady=10)
        delete_button = tk.Button(button_frame, text="Скорректировать", command=self.view_details)
        delete_button.pack(side="left", pady=10)
        next_button = tk.Button(button_frame, text="Следующий", command=self.next_page)
        next_button.pack(side="right", pady=10)
        prev_button = tk.Button(button_frame, text="Предыдущий", command=self.prev_page)
        prev_button.pack(side="right", pady=10)
        self.current_page = 1
        self.page_size = 10
        self.refresh_table()  # Загрузка данных в таблицу
    def update(self, action, data):
        """Метод для обновления таблицы при изменении модели"""
        if action in ("add", "update", "delete"):
            self.refresh_table()
    def refresh_table(self):
        """Обновить таблицу с данными из модели"""
        # Удаляем старые данные из таблицы
        for row in self.table.get_children():
            self.table.delete(row)
        # Получаем данные из модели
        patients = self.controller.get_patients(self.page_size, self.current_page)
        if not patients:
            if self.controller.model.get_count() > 0:
                self.current_page -= 1
                self.refresh_table()
            print("Нет данных для отображения")
            return
        for index, patient in enumerate(patients, 1):
            self.table.insert(
                '',
                'end',
                values=(
                    index + (self.current_page - 1) * 10,
                    patient['first_name'],
                    patient['last_name'],
                    patient['email'],
                    patient['gender'],
                    patient['phone']
                ),
                iid=patient['id']  # Сохраняем ID как идентификатор строки
            )
    def open_add_patient_window(self):
        """Открытие окна добавления клиента"""
        new_window = tk.Toplevel(self.root)
        AddUpdatePatientView(new_window, AddUpdatePatientController(self.controller.model), "add")
    def delete_patient(self):
        """Удаление клиента"""
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("Ошибка", "Выберите пациента для удаления")
            return
        # Получаем ID выбранного клиента
        patient_id = selected_item[0]
        self.controller.delete_patient(patient_id)
        messagebox.showinfo("Успех", "Пациент успешно удален!")
    def view_details(self):
        """Открытие окна с подробной информацией о пациенте для редактирования"""
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("Ошибка", "Выберите пациента для удаления")
            return
        patient_id = selected_item[0]
        patient_data = self.controller.model.get_patient_by_id(patient_id)
        if patient_data:
            new_window = tk.Toplevel(self.root)
            AddUpdatePatientView(new_window, AddUpdatePatientController(self.controller.model), "update", patient_data)
        else:
            messagebox.showwarning("Ошибка", "Не удалось найти пациента в базе данных")
    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.refresh_table()
    def next_page(self):
        self.current_page += 1
        self.refresh_table()
