from django.core.management.base import BaseCommand
from blogs.models import Blogs, BlogMedia

class Command(BaseCommand):
    help = "Migrate Blogs.image data into BlogMedia.upload_file"

    def handle(self, *args, **kwargs):
        blogs_with_images = Blogs.objects.exclude(image__isnull=True).exclude(image__exact='')
        count = 0
        for blog in blogs_with_images:
            # BlogMedia record create
            BlogMedia.objects.create(
                blogs=blog,
                upload_file=blog.image  # copy existing image file
            )
            count += 1
        self.stdout.write(self.style.SUCCESS(f"{count} images migrated successfully!"))
