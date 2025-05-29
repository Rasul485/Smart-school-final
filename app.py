from flask import Flask, request
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Подключение к MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="smart_school"
)
cursor = db.cursor()

# Обед
@app.route('/order_lunch', methods=['POST'])
def order_lunch():
    try:
        dish = request.form['dish']
        drink = request.form['drink']
        dessert = request.form['dessert']
        diet = request.form['diet']
        delivery_time = request.form['delivery_time']
        comment = request.form['comment']
        sql = "INSERT INTO lunch_orders (dish, drink, dessert, diet, delivery_time, comment) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (dish, drink, dessert, diet, delivery_time if delivery_time else None, comment)
        cursor.execute(sql, values)
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        return "Заказ принят"

# Профиль
@app.route('/update_profile', methods=['POST'])
def update_profile():
    try:
        name = request.form['name']
        class_name = request.form['class']
        birthdate = request.form['birthdate']
        avatar = request.form['avatar']
        hobby = request.form['hobby']
        bio = request.form['bio']
        sql = "INSERT INTO profiles (name, class, birthdate, avatar, hobby, bio) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, class_name, birthdate, avatar, hobby, bio)
        cursor.execute(sql, values)
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        return "Профиль сохранён"

# Расписание
@app.route('/add_schedule', methods=['POST'])
def add_schedule():
    try:
        subject = request.form['subject']
        datetime_str = request.form['datetime']
        type_lesson = request.form['type']
        priority = request.form['priority']
        teacher = request.form['teacher']
        sql = "INSERT INTO schedules (subject, datetime, type, priority, teacher) VALUES (%s, %s, %s, %s, %s)"
        values = (subject, datetime_str, type_lesson, priority, teacher)
        cursor.execute(sql, values)
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        return "Урок добавлен"

# Оценки
@app.route('/add_grade', methods=['POST'])
def add_grade():
    try:
        subject = request.form['subject']
        grade = request.form['grade']
        type_work = request.form['type']
        grade_date = request.form['grade_date']
        comment = request.form['comment']
        sql = "INSERT INTO grades (subject, grade, type, grade_date, comment) VALUES (%s, %s, %s, %s, %s)"
        values = (subject, int(grade), type_work, grade_date if grade_date else None, comment)
        cursor.execute(sql, values)
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        return "Оценка добавлена"

# Календарь
@app.route('/add_event', methods=['POST'])
def add_event():
    try:
        event = request.form['event']
        date = request.form['date']
        event_time = request.form['event_time']
        category = request.form['category']
        reminder = 'reminder' in request.form
        sql = "INSERT INTO events (event, date, event_time, category, reminder) VALUES (%s, %s, %s, %s, %s)"
        values = (event, date, event_time if event_time else None, category, reminder)
        cursor.execute(sql, values)
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        return "Событие добавлено"

# Договоры
@app.route('/add_contract', methods=['POST'])
def add_contract():
    try:
        contract_id = request.form['contract_id']
        type_contract = request.form['type']
        expiry = request.form['expiry']
        status = request.form['status']
        details = request.form['details']
        sql = "INSERT INTO contracts (contract_id, type, expiry, status, details) VALUES (%s, %s, %s, %s, %s)"
        values = (contract_id, type_contract, expiry if expiry else None, status, details)
        cursor.execute(sql, values)
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        return "Договор добавлен"

# Развозка
@app.route('/add_transport', methods=['POST'])
def add_transport():
    try:
        route = request.form['route']
        time = request.form['time']
        vehicle = request.form['vehicle']
        pickup = request.form['pickup']
        seats = request.form['seats']
        sql = "INSERT INTO transports (route, time, vehicle, pickup, seats) VALUES (%s, %s, %s, %s, %s)"
        values = (route, time, vehicle, pickup, int(seats))
        cursor.execute(sql, values)
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        return "Поездка добавлена"

# Заявки
@app.route('/submit_request', methods=['POST'])
def submit_request():
    try:
        service = request.form['service']
        urgency = request.form['urgency']
        contact_phone = request.form['contact_phone']
        details = request.form['details']
        sql = "INSERT INTO requests (service, urgency, contact_phone, details) VALUES (%s, %s, %s, %s)"
        values = (service, urgency, contact_phone, details)
        cursor.execute(sql, values)
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        return "Заявка подана"

# Суббота
@app.route('/add_saturday', methods=['POST'])
def add_saturday():
    try:
        activity = request.form['activity']
        time = request.form['time']
        type_activity = request.form['type']
        difficulty = request.form['difficulty']
        duration = request.form['duration']
        sql = "INSERT INTO saturday_activities (activity, time, type, difficulty, duration) VALUES (%s, %s, %s, %s, %s)"
        values = (activity, time, type_activity, difficulty, int(duration))
        cursor.execute(sql, values)
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        return "Занятие добавлено"

# Сообщения
@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        recipient = request.form['recipient']
        topic = request.form['topic']
        message_priority = request.form['message_priority']
        message = request.form['message']
        sql = "INSERT INTO messages (recipient, topic, message_priority, message) VALUES (%s, %s, %s, %s)"
        values = (recipient, topic, message_priority, message)
        cursor.execute(sql, values)
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        return "Сообщение отправлено"

# Чаты
@app.route('/create_chat', methods=['POST'])
def create_chat():
    try:
        chat_name = request.form['chat_name']
        participants = request.form['participants']
        role = request.form['role']
        purpose = request.form['purpose']
        max_participants = request.form['max_participants']
        sql = "INSERT INTO chats (chat_name, participants, role, purpose, max_participants) VALUES (%s, %s, %s, %s, %s)"
        values = (chat_name, participants, role, purpose, int(max_participants))
        cursor.execute(sql, values)
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        return "Чат создан"

if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0')
    finally:
        cursor.close()
        db.close()