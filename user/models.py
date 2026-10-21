from django.db import models, connection
from django.contrib.auth.models import AbstractUser, Group, Permission,BaseUserManager
from multiselectfield import MultiSelectField

class UserInap(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=128)  # temporarily store raw password
    bio = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=255,blank=True, null=True)
    instagram = models.CharField(max_length=255,blank=True, null=True)
    youtube = models.CharField(max_length=255,blank=True, null=True)
    tiktok = models.CharField(max_length=255,blank=True, null=True)
    reserved1 = models.CharField(max_length=255, blank=True, null=True)
    reserved2 = models.CharField(max_length=255, blank=True, null=True)
    reserved3 = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending','Pending'),('approved','Approved'),('rejected','Rejected')],
        default='pending'
    )

    def save(self, *args, **kwargs):
        if not self.user_id:
        # last user_id
            inap_user_id = UserInap.objects.order_by('-user_id').first()
            user_id = CustomUser.objects.order_by('-id').first()

            if inap_user_id:
                inap_user_id_num = int(inap_user_id.user_id.replace("USR",""))
                if user_id.id and user_id.id.startswith("USR"):
                    num_part = user_id.id.replace("USR", "")
                    user_id_num = int(num_part) if num_part.isdigit() else 0
                else:
                    user_id_num = 0
                
                if user_id_num >= inap_user_id_num:
                    lest_user = user_id
                    lest_user_id = lest_user.id
                else:
                    lest_user = inap_user_id
                    lest_user_id = lest_user.user_id
            else:
                lest_user = user_id
                lest_user_id = lest_user.id

            if lest_user and lest_user_id:
            # "USR0001" → "0001" → int
                lest_num = int(lest_user_id.replace("USR", ""))
                new_num = lest_num + 1
            else:
                new_num = 1
        # USR0001 format
            self.user_id = f"USR{new_num:04d}"
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.name} ({self.user_id})"

class CustomUserManager(BaseUserManager): 
    def create_user(self, email, password=None, **extra_fields): 
        if not email: 
            raise ValueError("The Email field must be set") 
        email = self.normalize_email(email) 
        user = self.model(email=email, **extra_fields) 
        user.set_password(password) # hash password 
        user.save(using=self._db) 
        return user 
    
    def create_superuser(self, email, password=None, **extra_fields): 
        extra_fields.setdefault("is_staff", True) 
        extra_fields.setdefault("is_superuser", True) 
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    id = models.CharField(max_length=20, primary_key=True, editable=False)  # same as UserInap.user_id
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    ROLE_CHOICES = [ 
        ('CEO','CEO'),
        ('consultant','Consultant'),
        ('admin','Admin'), 
        ('instructor','Instructor'), 
        ('normal','Normal User'), 
        ('guest','Guest'), 
        ('premium','Premium')
        ]
    
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=255,blank=True, null=True)
    instagram = models.CharField(max_length=255,blank=True, null=True)
    youtube = models.CharField(max_length=255,blank=True, null=True)
    tiktok = models.CharField(max_length=255,blank=True, null=True)
    role = MultiSelectField(choices=ROLE_CHOICES, default=['guest']) 
    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False) 
    reserved1 = models.CharField(max_length=255, blank=True, null=True)
    reserved2 = models.CharField(max_length=255, blank=True, null=True)
    reserved3 = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = ["name"]

    objects = CustomUserManager()

    def __str__(self):
        # return f"{self.name}  {self.username} ({self.id})"
        return f"{self.name}"
    
class Instructor(models.Model):
    id = models.CharField(max_length=20, primary_key=True, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    reserved1 = models.CharField(max_length=255, blank=True, null=True)
    reserved2 = models.CharField(max_length=255, blank=True, null=True)
    reserved3 = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            lest_classes= Instructor.objects.order_by('-id').first()
            if lest_classes:
                lest_num = int(lest_classes.id.replace("INS",""))
                new_num = lest_num + 1
            else:
                new_num = 1
            self.id = f"INS{new_num:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.name

