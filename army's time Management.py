import sqlite3
from datetime import datetime, timedelta

# ایجاد پایگاه داده و جدول‌ها
def init_db():
    conn = sqlite3.connect("scheduler.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT,
                        start_time TEXT NOT NULL,
                        end_time TEXT NOT NULL
                      )''')
    conn.commit()
    conn.close()

# افزودن یک وظیفه جدید
def add_task(title, description, start_time, end_time):
    conn = sqlite3.connect("scheduler.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO tasks (title, description, start_time, end_time)
                      VALUES (?, ?, ?, ?)''', (title, description, start_time, end_time))
    conn.commit()
    conn.close()

# نمایش تمام وظایف
def show_tasks():
    conn = sqlite3.connect("scheduler.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM tasks''')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# حذف یک وظیفه
def delete_task(task_id):
    conn = sqlite3.connect("scheduler.db")
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM tasks WHERE id = ?''', (task_id,))
    conn.commit()
    conn.close()

# اجرای برنامه
if __name__ == "__main__":
    init_db()
    print("سیستم مدیریت زمان آماده است!")

    while True:
        print("\n1. افزودن وظیفه جدید")
        print("2. نمایش وظایف")
        print("3. حذف وظیفه")
        print("4. خروج")
        choice = input("انتخاب کنید: ")

        if choice == "1":
            title = input("عنوان وظیفه: ")
            description = input("توضیحات: ")
            start_time = input("زمان شروع (YYYY-MM-DD HH:MM): ")
            end_time = input("زمان پایان (YYYY-MM-DD HH:MM): ")
            add_task(title, description, start_time, end_time)
            print("وظیفه با موفقیت اضافه شد!")
        elif choice == "2":
            tasks = show_tasks()
            for task in tasks:
                print(f"ID: {task[0]}, عنوان: {task[1]}, توضیحات: {task[2]}, شروع: {task[3]}, پایان: {task[4]}")
        elif choice == "3":
            task_id = int(input("شناسه وظیفه برای حذف: "))
            delete_task(task_id)
            print("وظیفه حذف شد!")
        elif choice == "4":
            print("خروج از سیستم.")
            break
        else:
            print("انتخاب نامعتبر!")
