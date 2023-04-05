from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', null=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'blog'
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def summary(self):
        return self.content[:100]