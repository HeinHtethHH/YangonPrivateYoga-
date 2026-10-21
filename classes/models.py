# models.py
from django.db import models
from user.models import Instructor
from blogs.models import Category
from multiselectfield import MultiSelectField

class Classes(models.Model):
    DAY_CHOICES = [ 
        ("Sunday", "Sunday"),
        ("Monday", "Monday"), 
        ("Tuesday", "Tuesday"), 
        ("Wednesday", "Wednesday"), 
        ("Thursday", "Thursday"), 
        ("Friday", "Friday"), 
        ("Saturday", "Saturday"),  
    ] 

    CLASS_TYPE = [
         ("Discussion","Discussion"),
         ("Practice","Practice"),
         ("Workshop","Workshop"),
         ("TTC","TTC")
     ]

    classes_id = models.CharField(max_length=10,primary_key=True,editable=False)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='classes/', blank=True, null=True)
    instructor_image = models.ImageField(upload_to='Otherinst/', blank=True, null=True)
    other_instructor_expertise = models.CharField(max_length=150, null=True, blank=True)
    other_instructor_bio = models.TextField(null=True, blank=True)
    short_des = models.CharField(max_length=100)
    description = models.TextField() 
    schedule = models.DateTimeField(blank=True, null=True)
    class_start_date = models.DateField(blank=True, null=True) 
    class_end_date = models.DateField(blank=True, null=True)
    class_start_time = models.TimeField(blank=True, null=True)
    class_end_time = models.TimeField(blank=True, null=True)
    class_day = MultiSelectField(choices=DAY_CHOICES)
    location = models.CharField(max_length=255)
    class_category = models.ForeignKey( 
        Category, 
        on_delete=models.CASCADE, 
        related_name="classes",
        blank=True, null=True 
        )
    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name='classes',
        null=True, # ✅ allow NULL in DB 
        blank=True # ✅ allow empty in forms
    )
    other_instructor = models.CharField(max_length=150, null=True, blank=True)
    class_type = models.CharField(max_length=20, choices=CLASS_TYPE)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    reserved1 = models.CharField(max_length=255, blank=True, null=True)
    reserved2 = models.CharField(max_length=255, blank=True, null=True)
    reserved3 = models.CharField(max_length=255, blank=True, null=True)
   
    def save(self, *args, **kwargs):
        if not self.classes_id:
            lest_classes= Classes.objects.order_by('-classes_id').first()
            if lest_classes:
                lest_num = int(lest_classes.classes_id.replace("CLS",""))
                new_num = lest_num + 1
            else:
                new_num = 1
            self.classes_id = f"CLS{new_num:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class SundayClass(models.Model):
    id = models.CharField(max_length=10,primary_key=True,editable=False)
    title = models.CharField(max_length=100)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    reserved1 = models.CharField(max_length=255, blank=True, null=True)
    reserved2 = models.CharField(max_length=255, blank=True, null=True)
    reserved3 = models.CharField(max_length=255, blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.id:
            lest_classes= SundayClass.objects.order_by('-id').first()
            if lest_classes:
                lest_num = int(lest_classes.id.replace("SUN",""))
                new_num = lest_num + 1
            else:
                new_num = 1
            self.id = f"SUN{new_num:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class MondayClass(models.Model):
    id = models.CharField(max_length=10,primary_key=True,editable=False)
    title = models.CharField(max_length=100)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    reserved1 = models.CharField(max_length=255, blank=True, null=True)
    reserved2 = models.CharField(max_length=255, blank=True, null=True)
    reserved3 = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            lest_classes= MondayClass.objects.order_by('-id').first()
            if lest_classes:
                lest_num = int(lest_classes.id.replace("MON",""))
                new_num = lest_num + 1
            else:
                new_num = 1
            self.id = f"MON{new_num:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class TuesdayClass(models.Model):
    id = models.CharField(max_length=10,primary_key=True,editable=False)
    title = models.CharField(max_length=100)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    reserved1 = models.CharField(max_length=255, blank=True, null=True)
    reserved2 = models.CharField(max_length=255, blank=True, null=True)
    reserved3 = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            lest_classes= TuesdayClass.objects.order_by('-id').first()
            if lest_classes:
                lest_num = int(lest_classes.id.replace("TUE",""))
                new_num = lest_num + 1
            else:
                new_num = 1
            self.id = f"TUE{new_num:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class WednesdayClass(models.Model):
    id = models.CharField(max_length=10,primary_key=True,editable=False)
    title = models.CharField(max_length=100)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    reserved1 = models.CharField(max_length=255, blank=True, null=True)
    reserved2 = models.CharField(max_length=255, blank=True, null=True)
    reserved3 = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            lest_classes= WednesdayClass.objects.order_by('-id').first()
            if lest_classes:
                lest_num = int(lest_classes.id.replace("WED",""))
                new_num = lest_num + 1
            else:
                new_num = 1
            self.id = f"WED{new_num:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class ThursdayClass(models.Model):
    id = models.CharField(max_length=10,primary_key=True,editable=False)
    title = models.CharField(max_length=100)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    reserved1 = models.CharField(max_length=255, blank=True, null=True)
    reserved2 = models.CharField(max_length=255, blank=True, null=True)
    reserved3 = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            lest_classes= ThursdayClass.objects.order_by('-id').first()
            if lest_classes:
                lest_num = int(lest_classes.id.replace("THU",""))
                new_num = lest_num + 1
            else:
                new_num = 1
            self.id = f"THU{new_num:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class FridayClass(models.Model):
    id = models.CharField(max_length=10,primary_key=True,editable=False)
    title = models.CharField(max_length=100)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    reserved1 = models.CharField(max_length=255, blank=True, null=True)
    reserved2 = models.CharField(max_length=255, blank=True, null=True)
    reserved3 = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            lest_classes= FridayClass.objects.order_by('-id').first()
            if lest_classes:
                lest_num = int(lest_classes.id.replace("FRI",""))
                new_num = lest_num + 1
            else:
                new_num = 1
            self. id = f"FRI{new_num:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class SaturdayClass(models.Model):
    id = models.CharField(max_length=10,primary_key=True,editable=False)
    title = models.CharField(max_length=100)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    reserved1 = models.CharField(max_length=255, blank=True, null=True)
    reserved2 = models.CharField(max_length=255, blank=True, null=True)
    reserved3 = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            lest_classes= SaturdayClass.objects.order_by('-id').first()
            if lest_classes:
                lest_num = int(lest_classes.id.replace("SAT",""))
                new_num = lest_num + 1
            else:
                new_num = 1
            self.id = f"SAT{new_num:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title