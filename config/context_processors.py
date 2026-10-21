from django.conf import settings
def role_based_menus(request):
    if not request.user.is_authenticated:
        return {}
    role = request.user.role
    return {
        "show_admin_menu": "admin" in role, # or "instructor" in role,
        "show_user_menu": "admin" in role,
        "show_blog_menu": "admin" in role,
        "show_class_menu": "admin" in role, # ("instructor" in role) or ("admin" in role and "instructor" in role) or ("admin" in role),
        'MEDIA_URL': 'settings.MEDIA_URL'
    }