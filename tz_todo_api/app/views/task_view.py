from flask import request, jsonify
from run import app, db
from app.models.task import Task
from flask import abort


@app.route('/tasks', methods=['POST'])
def create_task():
    # Проверяем, что запрос содержит JSON и поле title
    if not request.json or not 'title' in request.json:
        abort(400)
    # Создаем новую задачу
    task = Task(title=request.json['title'], description=request.json.get('description', ""))
    db.session.add(task)
    # Сохраняем изменения в базе данных
    db.session.commit()
    # Возвращаем созданную задачу в формате json
    return jsonify({'task': task.to_json()}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    # Возвращаем список всех задач в формате json
    return jsonify({'tasks': [task.to_json() for task in tasks]})

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    if task is None:
        abort(404)
    # Возвращаем задачу в формате json
    return jsonify({'task': task.to_json()})

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)
    if task is None:
        abort(404)
    # Если запрос не содержит JSON, возвращаем ошибку 400
    if not request.json:
        abort(400)
    # Проверяем, что title это строка
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    # Проверяем, что description это строка
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    # Обновляем поля задачи
    task.title = request.json.get('title', task.title)
    task.description = request.json.get('description', task.description)
    # Сохраняем изменения в базе данных
    db.session.commit()
    # Возвращаем обновленную задачу в формате json
    return jsonify({'task': task.to_json()})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if task is None:
        abort(404)
    # Удаляем задачу из базы данных
    db.session.delete(task)
    # Сохраняем изменения в базе данных
    db.session.commit()
    # Возвращаем результат операции в формате json
    return jsonify({'result': True})