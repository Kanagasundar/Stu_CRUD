from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_no', 'dob', 'department', 'year_of_studying']

    dob = forms.DateField(
        input_formats=['%d-%m-%Y'],  # The format used by the user
        widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'dd-mm-yyyy'})  # Type text for custom format
    )

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if not dob:
            raise forms.ValidationError('Enter a valid date in the format dd-mm-yyyy.')
        return dob
