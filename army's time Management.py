import sqlite3
from datetime import datetime, timedelta

# ایجاد پایگاه داده برای کاربران
def init_user_db():
    conn = sqlite3.connect("scheduler.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL
                      )''')
    conn.commit()
    conn.close()

# ثبت‌نام کاربر جدید
def register_user(username, password):
    conn = sqlite3.connect("scheduler.db")
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO users (username, password)
                          VALUES (?, ?)''', (username, password))
        conn.commit()
        print("کاربر با موفقیت ثبت شد!")
    except sqlite3.IntegrityError:
        print("نام کاربری قبلاً ثبت شده است!")
    finally:
        conn.close()

# ورود کاربر
def login_user(username, password):
    conn = sqlite3.connect("scheduler.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM users WHERE username = ? AND password = ?''', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

# اجرای برنامه
if __name__ == "__main__":
    init_user_db()
    print("سیستم مدیریت دسترسی آماده است!")

    while True:
        print("\n1. ثبت‌نام")
        print("2. ورود")
        print("3. خروج")
        choice = input("انتخاب کنید: ")

        if choice == "1":
            username = input("نام کاربری: ")
            password = input("رمز عبور: ")
            register_user(username, password)
        elif choice == "2":
            username = input("نام کاربری: ")
            password = input("رمز عبور: ")
            if login_user(username, password):
                print("ورود موفقیت‌آمیز!")
                break  # پس از ورود موفق به منوی اصلی منتقل می‌شوید
            else:
                print("نام کاربری یا رمز عبور اشتباه است!")
        elif choice == "3":
            print("خروج از سیستم.")
            break
        else:
            print("انتخاب نامعتبر!")

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
