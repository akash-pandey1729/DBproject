from django.forms import ModelForm
from .models import *

class DataForm(ModelForm):
    class Meta:
        model = Data
        exclude = ('created_at', 'updated_at')
    def __init__(self, *args, **kwargs):
        super(DataForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        exclude = ('created_at', 'updated_at')
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'