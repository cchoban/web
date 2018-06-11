from django.db import models
from django.contrib.postgres.fields import JSONField
from .validators import validate_file_extension


class Package(models.Model):
    id = models.AutoField(primary_key=True)
    packageName = models.CharField(max_length=100, blank=True, null=True)
    packageArgs = JSONField()
    packageUninstallArgs = JSONField()
    server = JSONField()

    def __str__(self):
        return self.packageName


class SubmitPackage(models.Model):
    id = models.AutoField(primary_key=True)
    package = models.FileField(upload_to="uploads/", validators=[validate_file_extension])
    packageName = models.CharField(max_length=100, blank=True, null=True)
    packageArgs = JSONField(default={})
    packageUninstallArgs = JSONField(default={})
    server = JSONField(default={})
    user = models.ForeignKey

    def __str__(self):
        return self.packageName
