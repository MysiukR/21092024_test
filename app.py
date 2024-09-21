from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список для зберігання завдань
tasks = []

# Маршрут для головної сторінки
@app.route('/')
def home():
    return "Вітаю у веб-сервісі на Flask!"

# Маршрут для перегляду списку завдань
@app.route('/tasks')
def task_list():
    return render_template('tasks.html', tasks=tasks)

# Маршрут для додавання нового завдання
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        new_task = request.form['task']
        if new_task:  # Перевірка, чи поле не порожнє
            tasks.append(new_task)
        else:
            return "Завдання не може бути порожнім", 400
        return redirect(url_for('task_list'))
    return render_template('add_task.html')

# Запуск сервера
if __name__ == '__main__':
    app.run(debug=True)
