from django.db import models

# Create your models here.

class Text (models.Model):
    key = models.CharField(max_length=10, primary_key=True, verbose_name="Schlüssel")
    text = models.TextField(verbose_name="Text")
    class Meta:
        verbose_name = "Text"
        verbose_name_plural ="Texte"

    def __str__(self):
        return self.key
