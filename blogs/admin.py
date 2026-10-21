from django.contrib import admin
from .models import Category,Albums,Blogs, BlogMedia

admin.site.register(Category)
admin.site.register(Albums)
admin.site.register(BlogMedia)
# admin.site.register(Blogs)
# admin.site.register(Vlogs)
#  Register your models here.
class blogMediaInline(admin.TabularInline):
    model = BlogMedia
    extra = 1
@admin.register(Blogs)
class blogsAdmin(admin.ModelAdmin):
    inlines = [blogMediaInline]
