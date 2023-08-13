from django import forms
from Work_App.models import TaskModel

# class TaskForm(forms.ModelForm):
#     description_widget = forms.Textarea(attrs={'cols': 40, 'rows': 10})
#     class Meta:
#         model = TaskModel
#         fields = ['title', 'description': description_widget]


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 10, 'rows': 5})
        }
