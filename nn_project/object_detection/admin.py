from django.contrib import admin
from .models import Prediction

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ["id", "label", "confidence", "keep_pinned", "created_at"]
    list_filter = ["keep_pinned", "created_at"]
    search_fields = ["label"]