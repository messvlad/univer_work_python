import tkinter as tk
import pymysql.cursors
import tkinter.messagebox as msg
import pandas as pd
import queue
import random
import openpyxl
import xlwt
from test import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Создание текстового поля для ввода названия Базы данных
        self.text = tk.Label(text="Введите название Базы данных")
        self.text.pack()
        self.entry_widget_1 = tk.Entry(textvariable=tk.StringVar())
        self.entry_widget_1.pack()
        # Создание кнопок для вызова методов get_input_dbname и createdb
        self.btn = tk.Button(self, text="Отправить название Базы данных", command=self.get_input_dbname)
        self.btn1 = tk.Button(self, text="Создание Базы данных и вывод в окне", command=self.createdb)
        # Создания текстового поля для ввода названия таблицу в базе данных
        self.text1 = tk.Label(text="Введите название таблицы Базы данных")
        self.text1.pack()
        self.entry_widget_2 = tk.Entry(textvariable=tk.StringVar())
        self.entry_widget_2.pack()
        # Создание кнопок для вызова методов get_input_dbtable и createtable
        self.btn2 = tk.Button(self, text="Отправить название таблицы в Базу данных", command=self.get_input_dbtable)
        self.btn3 = tk.Button(self, text="Создание таблицы в Базе данных и вывод в окне", command=self.createtable)
        # Создание кнопки для отправки данных в таблицу в отдельном окне
        self.btn4 = tk.Button(self, text="Отправить данные в таблицу", command=self.start_window_1)
        # Создание кнопки для экспорта в Excel из MySQL
        self.btn5 = tk.Button(self, text="Экспорт в Excel", command=self.start_window_2)
        # Создание кнопки для закрытия окна
        self.btn6 = tk.Button(self, text="Выйти из программы", command=self.quit)
        # Дизайн кнопок
        self.btn.pack(padx=50, pady=5)
        self.btn1.pack(padx=50, pady=5)
        self.btn2.pack(padx=50, pady=5)
        self.btn3.pack(padx=50, pady=5)
        self.btn4.pack(padx=50, pady=5)
        self.btn5.pack(padx=50, pady=5)
        self.btn6.pack(padx=50, pady=5)

    # Метод уведомления об успешном получении имени Бд и метод self.entry_widget_1
    def get_input_dbname(self):
        msg.showinfo("Уведомление", "Название Базы данных успешно передано")
        return

    # Метод создания Базы данных
    def createdb(self):
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='46GFD#un6$0',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.Cursor)
        with connection.cursor() as cursor:
            sql = f'CREATE DATABASE IF NOT EXISTS {self.entry_widget_1.get()}'
            cursor.execute(sql)
            connection.commit()
            df = pd.read_sql("SHOW DATABASES", connection)
            msg.showinfo("Базы данных", str(df))
            connection.close()
        return

    # Метод подключения к MySQL
    def mysqlconnection(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='46GFD#un6$0',
                                          charset='utf8mb4',
                                          db=self.entry_widget_1.get(),
                                          cursorclass=pymysql.cursors.Cursor)
        return

    # Метод уведомления об успешном отправлении имени таблицы
    def get_input_dbtable(self):
        msg.showinfo("Уведомление", "Название таблицы отправлено!")
        return

    # Метод создания таблицы
    def createtable(self):
        App.mysqlconnection(self)
        with self.connection.cursor() as cursor:
            sql = f'CREATE TABLE IF NOT EXISTS {self.entry_widget_2.get()} (ID varchar(255), myStack text, delStack varchar(5000), novStack text);'
            cursor.execute(sql)
            self.connection.commit()
            df = pd.read_sql("SHOW TABLES", self.connection)
            msg.showinfo("Базы данных", str(df))
            self.connection.close()
        return

    # Внесение и вывод данных из таблиц
    # Создание нового окна
    def start_window_1(self):
        self.new_window_1 = tk.Tk()
        self.new_window_1.title("Ввод данных в таблицу")
        self.new_window_1.resizable()
        self.canvas = tk.Canvas(self.new_window_1)
        self.canvas.pack()
        # Поле 1
        text3 = tk.Label(self.canvas, text="ID")
        text3.pack(expand=True, padx=10, pady=10)
        self.entry_widget_5 = tk.Entry(self.canvas, textvariable=tk.IntVar())
        self.entry_widget_5.pack()
        # Кнопка генерации стека из 500 значений
        btn16 = tk.Button(self.canvas, text="Сгенерировать стек из 500 элементов", command=self.rukopashka)
        btn16.pack(padx=50, pady=5)
        # Кнопка вывода удалённых 100 значений в стеке
        btn17 = tk.Button(self.canvas, text="Сгенерировать стек из 100 удалённых элементов", command=self.vruchnuyu)
        btn17.pack(padx=50, pady=5)
        # Кнопка отправки данных в таблицу
        btn12 = tk.Button(self.canvas, text="Ввести данные в таблицу и вывести в новом окне",
                          command=self.insert_in_table)
        btn12.pack(padx=50, pady=5)
        # Кнопка закрытия окна
        btn13 = tk.Button(self.canvas, text="Вернуться", command=self.new_window_1.destroy)
        btn13.pack(padx=50, pady=5)
        # Поиск площади трапеции
        return

    # Кнопка создания стека
    def rukopashka(self):
        msg.showinfo("Уведомление", "Стек сгенерирован успешно!")

    # Метод генерации стека
    def ruchkami(self):
        return get()

    # Метод удаления 100 элементов
    def vruchnuyu(self):
        msg.showinfo("Уведомление", "Строки удалены!")

    # Метод внесения данных в таблицу
    def insert_in_table(self):
        App.mysqlconnection(self)
        self.myStack = str(myStack1[0:500])
        self.delStack = str(delStack1)
        self.novStack = str(novStack1)
        with self.connection.cursor() as cursor:
            sql = f'INSERT INTO {self.entry_widget_2.get()}(ID, myStack, delStack, novStack) values (%s, %s, %s, %s)'
            cursor.execute(sql, (self.entry_widget_5.get(), self.myStack, self.delStack, self.novStack))
            self.connection.commit()
            df = pd.read_sql_query(f"SELECT * from {self.entry_widget_2.get()}", self.connection)
            msg.showinfo("Данные из таблицы MySQL", str(df))
            self.connection.close()
            return

    # Экспорт в Excel
    # Создание окна для экспорта в Excel
    def start_window_2(self):
        self.new_window_2 = tk.Tk()
        self.new_window_2.title("Экспорт в Excel")
        self.new_window_2.resizable()
        self.canvas1 = tk.Canvas(self.new_window_2)
        self.canvas1.pack()
        # Поле 1
        text6 = tk.Label(self.canvas1, text="Введите название файла Excel.xls")
        text6.pack(expand=True, padx=10, pady=10)
        self.entry_widget_8 = tk.Entry(self.canvas1, textvariable=tk.StringVar())
        self.entry_widget_8.pack()
        # Кнопка отправки данных в таблицу
        btn14 = tk.Button(self.canvas1, text="Экспортировать данные в Excel", command=self.export_excel)
        btn14.pack(padx=50, pady=5)
        # Кнопка закрытия окна
        btn15 = tk.Button(self.canvas1, text="Вернуться", command=self.new_window_2.destroy)
        btn15.pack(padx=50, pady=5)
        return

    # Метод эксопрта в Excel
    def export_excel(self):
        App.mysqlconnection(self)
        df = pd.read_sql_query(f'SELECT * FROM {self.entry_widget_2.get()}', self.connection)
        df.to_excel(self.entry_widget_8.get(), sheet_name='Данные из MySQL', index=False)
        return


if __name__ == "__main__":
    app = App()
    app.title("Приложение 'Базы данных'")
    app.mainloop()
