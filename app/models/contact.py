from django.db import models

from app.models import BaseModel


class ContactMessage(BaseModel):
    name = models.CharField("Аты", max_length=100)
    email = models.EmailField("E-mail")
    subject = models.CharField("Тақырып", max_length=200)
    message = models.TextField("Хабарлама")
    file = models.FileField(upload_to="contact_message", null=True, blank=True)
    is_checked = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Байланыс хаты"
        verbose_name_plural = "Байланыс хаттары"

    def __str__(self):
        return f"{self.name} - {self.subject}"
