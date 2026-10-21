
from django import forms
from .models import UserInap,CustomUser

ROLE_CHOICES = [ 
    ('admin', 'Admin'), 
    ('instructor', 'Instructor'), 
    ('normal', 'Normal User'), 
    ('guest', 'Guest'), 
    ('premium','Premium')
]

class UserRegister(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = UserInap
        fields = ['name','date_of_birth','image','email','phone','address','bio','facebook','instagram','youtube','tiktok','password']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'facebook': forms.TextInput(attrs={'placeholder': 'Enter Facebook URL'}),
            'instagram': forms.TextInput(attrs={'placeholder': 'Enter Instagram URL'}),
            'youtube': forms.TextInput(attrs={'placeholder': 'Enter YouTube URL'}),
            'tiktok': forms.TextInput(attrs={'placeholder': 'Enter TikTok URL'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        self.fields['image'].required = True

class ReqUserApproveForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name','date_of_birth','image','email','phone','address','facebook','instagram','youtube','tiktok','bio','role']
        widgets = { 
            'name': forms.TextInput(attrs={'readonly':'readonly'}), 
            'date_of_birth': forms.DateInput(attrs={'readonly': 'readonly'}),
            'email': forms.EmailInput(attrs={'readonly':'readonly'}), 
            'phone': forms.TextInput(attrs={'readonly':'readonly'}), 
            'address': forms.TextInput(attrs={'readonly':'readonly'}), 
            'bio': forms.TextInput(attrs={'readonly':'readonly'}),
            'facebook': forms.TextInput(attrs={'readonly':'readonly'}),
            'instagram': forms.TextInput(attrs={'readonly':'readonly'}),
            'youtube': forms.TextInput(attrs={'readonly':'readonly'}),
            'tiktok': forms.TextInput(attrs={'readonly':'readonly'}),
            'role': forms.CheckboxSelectMultiple(),
            # 'role': forms.CheckboxSelectMultiple(choices=ROLE_CHOICES)
            # 'role': forms.TextInput(attrs={'list':'role-list','placeholder':'Enter role'})
        }
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        print("ROLE CHOICES:", self.fields['role'].choices)

class ReqUserDeleteForm(forms.ModelForm): 
    class Meta: 
        model = UserInap 
        fields = ['name','date_of_birth','email','phone','address','image','facebook','instagram','youtube','tiktok'] # show only these fields 
        widgets = { 
        'name': forms.TextInput(attrs={'readonly':'readonly'}), 
        'date_of_birth': forms.DateInput(attrs={'readonly': 'readonly'}),
        'email': forms.EmailInput(attrs={'readonly':'readonly'}), 
        'phone': forms.TextInput(attrs={'readonly':'readonly'}), 
        'address': forms.TextInput(attrs={'readonly':'readonly'}), 
        'facebook': forms.TextInput(attrs={'readonly':'readonly'}),
        'instagram': forms.TextInput(attrs={'readonly':'readonly'}),
        'youtube': forms.TextInput(attrs={'readonly':'readonly'}),
        'tiktok': forms.TextInput(attrs={'readonly':'readonly'}),
        }

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name','date_of_birth','image','email','phone','address','facebook','instagram','youtube','tiktok','role']
        widgets = { 
            'name': forms.TextInput(attrs={'readonly':'readonly'}), 
            'date_of_birth': forms.DateInput(attrs={'readonly': 'readonly'}),
            'email': forms.EmailInput(attrs={'readonly':'readonly'}), 
            'phone': forms.TextInput(attrs={'readonly':'readonly'}), 
            'address': forms.TextInput(attrs={'readonly':'readonly'}), 
            'facebook': forms.TextInput(attrs={'readonly':'readonly'}),
            'instagram': forms.TextInput(attrs={'readonly':'readonly'}),
            'youtube': forms.TextInput(attrs={'readonly':'readonly'}),
            'tiktok': forms.TextInput(attrs={'readonly':'readonly'}),
            'role': forms.CheckboxSelectMultiple(choices=ROLE_CHOICES)
            # 'role': forms.TextInput(attrs={'list':'role-list','placeholder':'Enter role'})
        }

# forms.py
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserInap
        fields = ['image', 'name', 'bio', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProfileImgForm(forms.ModelForm):
    class Meta:
        model = UserInap
        fields = ['image']  