# Подключаем библиотеку Flask
from flask import Flask

# Создаем приложение
app = Flask('__main__')

# Говорим, что при переходе на главную страницу (/) выполнять эту функцию
@app.route('/')
def hello():
    return "Привет! Я в контейнере!"

app.run(host='0.0.0.0', port=5000)