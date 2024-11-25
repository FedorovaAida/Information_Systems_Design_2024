Тема: Психологическая клиника

Вы работаете в психологической клинике, оказывающей психологическую помощь пациентам. Работа с пациентами организована следующим образом: у каждого пациента есть стандартные данные - фамилия, имя, почта, телефон и пол. У психологов, которые будут работать с пациентами,
будут такие поля, как: фамилия, имя, телефон, номр лицензии и почта. Связывающим звеном будут сессии, которые будут хранить пациента, психолога, дата и время прима и цена сеанса.

В итоге была построена ER-модель имеющая 3 таблицы: пациенты, психологи и сессии. Добавленные поля отображены в прикрепленном рисунке

Код создания таблиц и выполнение связи для сайта https://databasediagram.com/app (DBML):

Table patients {
  patient_id int [pk, increment]
  first_name varchar
  last_name varchar
  email varchar
  gender varchar
  phone varchar
  date_of_birth date
}

Table sessions {
  session_id int [pk, increment]
  date date
  time time
  price decimal
  patient_id int [ref: > patients.patient_id]
  psychologist_id int [ref: > psychologists.psychologist_id ]
}

Table psychologists {
  psychologist_id int [pk, increment]
  first_name varchar
  last_name varchar
  phone varchar
  license varchar
  email varchar
}
