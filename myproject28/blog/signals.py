from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import Blog

# triggered before saving a Blog 
@receiver(pre_save, sender=Blog)
def blog_pre_save(sender, instance, **kwargs):
    print(f'About to save blog post: {instance.title}')

# triggered after saving a Blog
@receiver(post_save, sender=Blog)
def blog_post_save(sender, instance, created, **kwargs):
    if created:
        print(f'New blog post created: {instance.title}')
    else:
        print(f'Blog post updated: {instance.title}')
     