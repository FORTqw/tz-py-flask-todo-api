import unittest
import requests


class TaskModelCase(unittest.TestCase):
    BASE_URL = 'http://127.0.0.1:5000/tasks'

    def test_create_task(self):
        # Тест создания задачи
        response = requests.post(self.BASE_URL, json={'title': 'Test Task'})
        self.assertEqual(response.status_code, 201)
        task = response.json()['task']
        self.assertEqual(task['title'], 'Test Task')

    def test_get_tasks(self):
        # Тест получения всех задач
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)
        tasks = response.json()['tasks']
        self.assertIsInstance(tasks, list)

    def test_update_task(self):
        # Сначала создаем задачу
        response = requests.post(self.BASE_URL, json={'title': 'Test Task'})
        task = response.json()['task']

        # Затем обновляем задачу
        response = requests.put(f"{self.BASE_URL}/{task['id']}", json={'title': 'Updated Task'})
        self.assertEqual(response.status_code, 200)
        updated_task = response.json()['task']
        self.assertEqual(updated_task['title'], 'Updated Task')

    def test_delete_task(self):
        # Сначала создаем задачу
        response = requests.post(self.BASE_URL, json={'title': 'Test Task'})
        task = response.json()['task']

        # Затем удаляем задачу
        response = requests.delete(f"{self.BASE_URL}/{task['id']}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], True)

if __name__ == '__main__':
    unittest.main()
