from django.db import models

class Prediction(models.Model):
    image = models.ImageField(upload_to="uploads/")
    label = models.CharField(max_length=255, blank=True)
    confidence = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
