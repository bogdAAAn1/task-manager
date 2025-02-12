from django.test import TestCase

from tasks.forms import WorkerCreationForm, TaskCreationForm, PositionCreationForm, TaskTypeCreationForm
from tasks.models import Worker, Position, TaskType


class WorkerCreationFormTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Manager")
        self.user_data = {
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "email": "testuser@example.com",
            "password1": "Password123!",
            "password2": "Password123!",
            "position": self.position,
        }

    def test_worker_creation_form_valid(self):
        form = WorkerCreationForm(data=self.user_data)
        self.assertTrue(form.is_valid())

    def test_worker_creation_form_invalid(self):
        data = self.user_data.copy()
        data["password2"] = "DifferentPassword"
        form = WorkerCreationForm(data=data)
        self.assertFalse(form.is_valid())


class TaskCreationFormTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Manager")
        self.worker = Worker.objects.create(
            username="testworker", position=self.position, first_name="Test", last_name="Worker",
            email="worker@example.com", password="Password123"
        )
        self.task_type = TaskType.objects.create(name="Bug Fix")

        self.task_data = {
            "name": "Test Task",
            "description": "This is a test task.",
            "priority": "High",
            "task_type": self.task_type.pk,
            "assignees": [self.worker.pk],
            "deadline": "2025-12-31T23:59",
        }

    def test_task_creation_form_valid(self):
        form = TaskCreationForm(data=self.task_data)
        self.assertTrue(form.is_valid())

    def test_task_creation_form_invalid(self):
        data = self.task_data.copy()
        data["name"] = ""
        form = TaskCreationForm(data=data)
        self.assertFalse(form.is_valid())


class PositionCreationFormTest(TestCase):
    def test_position_creation_form_valid(self):
        form_data = {"name": "Developer"}
        form = PositionCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_position_creation_form_invalid(self):
        form_data = {"name": ""}
        form = PositionCreationForm(data=form_data)
        self.assertFalse(form.is_valid())


class TaskTypeCreationFormTest(TestCase):
    def test_task_type_creation_form_valid(self):
        form_data = {"name": "Feature"}
        form = TaskTypeCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_type_creation_form_invalid(self):
        form_data = {"name": ""}
        form = TaskTypeCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
