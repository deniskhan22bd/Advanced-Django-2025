from django.db import models

class Resume(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    parsed_data = models.JSONField(null=True, blank=True)  # To store extracted details as JSON

    def __str__(self):
        return f"Resume {self.id} uploaded on {self.uploaded_at}"
