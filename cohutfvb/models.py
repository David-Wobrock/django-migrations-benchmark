from django.db import models


class Livljpedso(models.Model):
    ceudc = models.IntegerField(default=0)
    pass


class Qpuji(models.Model):
    saiuw = models.CharField(default='', max_length=84)
    pass


class Crzqih(models.Model):
    ttktcobp = models.CharField(default='', max_length=10)
    uanao = models.OneToOneField('joavhqi.Lfssmpr', null=True, related_name='+')
    nenil = models.ForeignKey('foijx.Qqktwujdfq', null=True, related_name='+')
    pass


class Ecgjvad(models.Model):
    dmlqug = models.CharField(default='', max_length=96)
    pass
