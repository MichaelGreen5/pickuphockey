from django.conf import settings
from django.db import models



class EmailVerification(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_query_name="verification"
    )
    verified = models.BooleanField(default=False)

    
    














   



