from django import forms

from .models import Birthday


class BirthdayForm(forms.ModelForm):
    class Meta():
        model = Birthday
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birthday'].input_formats = ['%Y-%m-%d']
 