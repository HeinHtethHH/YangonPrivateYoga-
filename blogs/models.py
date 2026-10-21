from django.db import models


class Category(models.Model):
    category_id = models.CharField(max_length=10,primary_key=True,editable=False)
    name = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    reserved1 = models.CharField(max_length=255, blank=True, null=True)
    reserved2 = models.CharField(max_length=255, blank=True, null=True)
    reserved3 = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.category_id:
            last_category = Category.objects.order_by('-category_id').first()
            if last_category:
                last_num = int(last_category.category_id.replace("CAT",""))
                new_num = last_num + 1
            else:
                new_num = 1
            self.category_id = f"CAT{new_num:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
###################################################################    
class Albums(models.Model):
    albums_id = models.CharField(max_length=10,primary_key=True,editable=False)
    name = models.CharField(max_length=20)
    cover = models.FileField(upload_to='albumcover/', blank=True, null=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    reserved1 = models.CharField(max_length=255, blank=True, null=True)
    reserved2 = models.CharField(max_length=255, blank=True, null=True)
    reserved3 = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.albums_id:
            last_album = Albums.objects.order_by('-albums_id').first()
            if last_album:
                last_num = int(last_album.albums_id.replace("ALB",""))
                new_num = last_num + 1
            else:
                new_num = 1
            self.albums_id = f"ALB{new_num:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
###################################################################

class Blogs(models.Model):
    blog_id = models.CharField(max_length=10,primary_key=True,editable=False)
    title = models.CharField(max_length=255,blank=True, null=True)
    pose_title = models.CharField(max_length=255,blank=True, null=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    post_type = models.CharField(max_length=10, choices=[('BLOG', 'Blog'), ('VLOG', 'Vlog')], default='BLOG')
    short_desc = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)
    albums = models.ForeignKey(Albums,on_delete=models.CASCADE,null=True, blank=True,db_column="albums_id",to_field="albums_id")
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    post_datetime = models.DateTimeField(auto_now_add=True)
    reserved1 = models.CharField(max_length=255, blank=True, null=True)
    reserved2 = models.CharField(max_length=255, blank=True, null=True)
    reserved3 = models.CharField(max_length=255, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.blog_id:
            last_blog= Blogs.objects.order_by('-blog_id').first()
            if last_blog:
                last_num = int(last_blog.blog_id.replace("BLG",""))
                new_num = last_num + 1
            else:
                new_num = 1
            self.blog_id = f"BLG{new_num:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
###################################################################		
class BlogMedia(models.Model):
    blogs = models.ForeignKey(Blogs,on_delete=models.CASCADE, related_name='additional_media',null=True, blank=True,db_column="blog_id",to_field="blog_id")
    upload_file = models.FileField(upload_to='blog/')

    def __str__(self):
        return f"{self.blogs.title} - {self.upload_file}"   

# class Vlogs(models.Model):
#     vlog_id = models.CharField(max_length=10,primary_key=True,editable=False)
#     title = models.CharField(max_length=255)
#     video = models.FileField(upload_to='vlog/', blank=True, null=True)
#     short_desc = models.CharField(max_length=255, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     category = models.ForeignKey(Category,on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True, null=True, blank=True)
#     post_datetime = models.DateTimeField(auto_now_add=True)
#     reserved1 = models.CharField(max_length=255, blank=True, null=True)
#     reserved2 = models.CharField(max_length=255, blank=True, null=True)
#     reserved3 = models.CharField(max_length=255, blank=True, null=True)
    
#     def save(self, *args, **kwargs):
#         if not self.vlog_id:
#             last_blog= Vlogs.objects.order_by('-vlog_id').first()
#             if last_blog:
#                 last_num = int(last_blog.vlog_id.replace("VLG",""))
#                 new_num = last_num + 1
#             else:
#                 new_num = 1
#             self.vlog_id = f"VLG{new_num:04d}"
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.title