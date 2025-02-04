from django import forms
from django.contrib.auth.forms import UserCreationForm

from tasks.models import Worker, Position, Task, TaskType


class WorkerCreationForm(UserCreationForm):
    position = forms.ModelChoiceField(
        queryset=Position.objects.all(),
        widget=forms.Select
    )

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "position"
        )


class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ["username", "first_name", "last_name", "email", "position"]


class TaskCreationForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'placeholder': 'YYYY-MM-DD HH:MM'
        },
            format='%Y-%m-%dT%H:%M'
        ),
        required=False
    )

    task_type = forms.ModelChoiceField(
        queryset=TaskType.objects.all(),
        widget=forms.Select
    )

    assignees = forms.ModelMultipleChoiceField(
        queryset=Worker.objects.select_related("position").all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = "__all__"


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
