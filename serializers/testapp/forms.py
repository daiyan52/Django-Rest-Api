from testapp.models import Student
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_roll(self):
        inputroll = self.cleaned_data['roll']
        if inputroll <= 0:
            raise forms.ValidationError('Roll must be a positive number')
        return inputroll

