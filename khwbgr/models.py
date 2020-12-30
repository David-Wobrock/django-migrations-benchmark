from django.db import models


class Ibuazau(models.Model):
    pssnb = models.OneToOneField('bniworfy.Trjyk', on_delete=models.CASCADE, null=True, related_name='+')
    pass
