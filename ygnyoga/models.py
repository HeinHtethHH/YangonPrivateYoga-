from django.db import models

# Create your models here.
class Ygnyoga(models.Model): 

    id = models.CharField(max_length=10,primary_key=True,editable=False)
    title = models.CharField(max_length=255)
    image1= models.ImageField(upload_to='ygnyoga/', blank=True, null=True)
    image2= models.ImageField(upload_to='ygnyoga/', blank=True, null=True)
    image3= models.ImageField(upload_to='ygnyoga/', blank=True, null=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    reserved1 = models.CharField(max_length=255, blank=True, null=True)
    reserved2 = models.CharField(max_length=255, blank=True, null=True)
    reserved3 = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            lest_ygnyoga= Ygnyoga.objects.order_by('-id').first()
            if lest_ygnyoga:
                lest_num = int(lest_ygnyoga.id.replace("YGYOGA",""))
                new_num = lest_num + 1
            else:
                new_num = 1
            self.id = f"YGYOGA{new_num:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title