from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from tasks.models import Task, TaskType, Position


class TaskListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.task_type = TaskType.objects.create(name="Test Task Type")
        self.position = Position.objects.create(name="Test Position")
        self.worker = get_user_model().objects.create_user(
            username="testuser", password="testpass123", position=self.position
        )
        self.task = Task.objects.create(
            name="Test Task", task_type=self.task_type, priority="Low"
        )
        self.task.assignees.add(self.worker)
        self.client.force_login(self.worker)

    def test_task_list_view_status_code(self):
        response = self.client.get(reverse("tasks:index"))
        self.assertEqual(response.status_code, 200)

    def test_task_list_view_template(self):
        response = self.client.get(reverse("tasks:index"))
        self.assertTemplateUsed(response, "tasks/index.html")

    def test_task_list_view_context(self):
        response = self.client.get(reverse("tasks:index"))
        self.assertIn("page_obj", response.context)
        self.assertEqual(len(response.context["page_obj"]), 1)


class TaskCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.task_type = TaskType.objects.create(name="Test Task Type")
        self.position = Position.objects.create(name="Test Position")
        self.worker = get_user_model().objects.create_user(
            username="testuser", password="testpass123", position=self.position
        )
        self.client.login(username="testuser", password="testpass123")

    def test_task_create_view_status_code(self):
        response = self.client.get(reverse("tasks:task-create"))
        self.assertEqual(response.status_code, 200)

    def test_task_create_view_template(self):
        response = self.client.get(reverse("tasks:task-create"))
        self.assertTemplateUsed(response, "tasks/task_form.html")

    def test_task_create_view_form_submission(self):
        data = {
            "name": "New Task",
            "task_type": self.task_type.id,
            "priority": "Low",
            "assignees": [self.worker.id],
        }
        response = self.client.post(reverse("tasks:task-create"), data)
        self.assertEqual(
            response.status_code, 302
        )
        self.assertEqual(Task.objects.count(), 1)


class TaskUpdateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.task_type = TaskType.objects.create(name="Test Task Type")
        self.position = Position.objects.create(name="Test Position")
        self.worker = get_user_model().objects.create_user(
            username="testuser", password="testpass123", position=self.position
        )
        self.task = Task.objects.create(
            name="Test Task", task_type=self.task_type, priority="Low"
        )
        self.task.assignees.add(self.worker)
        self.client.login(username="testuser", password="testpass123")

    def test_task_update_view_status_code(self):
        response = self.client.get(reverse("tasks:task-update", args=[self.task.id]))
        self.assertEqual(response.status_code, 200)

    def test_task_update_view_template(self):
        response = self.client.get(reverse("tasks:task-update", args=[self.task.id]))
        self.assertTemplateUsed(response, "tasks/task_form.html")

    def test_task_update_view_form_submission(self):
        data = {
            "name": "Updated Task",
            "task_type": self.task_type.id,
            "priority": "High",
            "assignees": [self.worker.id],
        }
        response = self.client.post(
            reverse("tasks:task-update", args=[self.task.id]), data
        )
        self.assertEqual(
            response.status_code, 302
        )
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, "Updated Task")
        self.assertEqual(self.task.priority, "High")


class TaskDeleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.task_type = TaskType.objects.create(name="Test Task Type")
        self.position = Position.objects.create(name="Test Position")
        self.worker = get_user_model().objects.create_user(
            username="testuser", password="testpass123", position=self.position
        )
        self.task = Task.objects.create(
            name="Test Task", task_type=self.task_type, priority="Low"
        )
        self.task.assignees.add(self.worker)
        self.client.login(username="testuser", password="testpass123")

    def test_task_delete_view_status_code(self):
        response = self.client.get(reverse("tasks:task-delete", args=[self.task.id]))
        self.assertEqual(response.status_code, 200)

    def test_task_delete_view_template(self):
        response = self.client.get(reverse("tasks:task-delete", args=[self.task.id]))
        self.assertTemplateUsed(response, "tasks/task_confirm_delete.html")

    def test_task_delete_view_form_submission(self):
        response = self.client.post(reverse("tasks:task-delete", args=[self.task.id]))
        self.assertEqual(
            response.status_code, 302
        )
        self.assertEqual(Task.objects.count(), 0)


class WorkerListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.position = Position.objects.create(name="Test Position")
        self.worker = get_user_model().objects.create_user(
            username="testuser", password="testpass123", position=self.position
        )
        self.client.login(username="testuser", password="testpass123")

    def test_worker_list_view_status_code(self):
        response = self.client.get(reverse("tasks:worker-list"))
        self.assertEqual(response.status_code, 200)

    def test_worker_list_view_template(self):
        response = self.client.get(reverse("tasks:worker-list"))
        self.assertTemplateUsed(response, "tasks/worker_list.html")
