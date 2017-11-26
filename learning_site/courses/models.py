from django.db import models

class Course(models.Model):
    # whenever record is first added (created), it will
    # automatically be datetime.now()
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return str(self.title)