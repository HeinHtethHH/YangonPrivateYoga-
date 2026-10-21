from django import forms
from django.forms import inlineformset_factory
from .models import Blogs, BlogMedia, Albums


class PostForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title','pose_title','short_desc','description','category','albums','post_type']

BlogMediaFormSet = inlineformset_factory(
    Blogs, 
    BlogMedia, 
    fields=['upload_file'], 
    extra=1,      # အလွတ်ပုံစံ ၃ ခု ပြထားမယ်
    can_delete=True
)

# class PostVlogForm(forms.ModelForm):
    
#     class Meta:
#         model = Vlogs
#         fields = ['title','video','pose','short_desc','description','category','albums']

class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Albums
        fields = ['name','cover']
