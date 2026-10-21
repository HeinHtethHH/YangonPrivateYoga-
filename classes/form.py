from django import forms
from .models import Classes
from user.models import Instructor

class CreateClass(forms.ModelForm): 
    instructor = forms.ModelChoiceField( 
        queryset=Instructor.objects.all(), 
        required=False 
    ) 
    other_instructor = forms.CharField(required=False)
    class Meta:
        model = Classes
        fields = [
            'title','image','short_des',
            'description','schedule',
            'class_start_date','class_end_date',
            'class_start_time','class_end_time',
            'class_day','location','class_category',
            'instructor','class_type'
        ]
        widgets = {
            'class_start_date': forms.DateInput(attrs={'type': 'date'}),
            'class_end_date': forms.DateInput(attrs={'type': 'date'}),
            'class_start_time': forms.TimeInput(attrs={'type': 'time'}),
            'class_end_time': forms.TimeInput(attrs={'type': 'time'}),
        }
    

class DeleteClass(forms.ModelForm):  
    class Meta:
        model = Classes
        fields = [
            'title','image',
            'short_des','description',
            'schedule','class_start_date','class_end_date',
            'class_start_time','class_end_time','class_day','location',
            'class_category','instructor','class_type'
        ]
        widgets = { 
            'title': forms.TextInput(attrs={'readonly':'readonly'}),
            'Short_Des': forms.TextInput(attrs={'readonly':'readonly'}),
            'description': forms.TextInput(attrs={'readonly':'readonly'}),
            'schedule': forms.TextInput(attrs={'readonly':'readonly'}),
            'class_start_date': forms.DateInput(attrs={'readonly': 'readonly'}),
            'class_end_date': forms.DateInput(attrs={'readonly': 'readonly'}),
            'class_start_time':forms.TimeInput(attrs={'readonly':'readonly'}),
            'class_end_time':forms.TimeInput(attrs={'readonly':'readonly'}),
            'day': forms.TextInput(attrs={'readonly':'readonly'}),
            'location': forms.TextInput(attrs={'readonly':'readonly'}),
            'class_category': forms.TextInput(attrs={'readonly':'readonly'}),
            'instructor': forms.TextInput(attrs={'readonly':'readonly'}),
            'class_type': forms.TextInput(attrs={'readonly':'readonly'})
        }