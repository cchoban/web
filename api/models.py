from django.db import models
from django.contrib.postgres.fields import JSONField
from .validators import validate_file_extension
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

class Package(models.Model):
    id = models.AutoField(primary_key=True)
    packageName = models.CharField(max_length=100, blank=True, null=True)
    packageArgs = JSONField()
    packageUninstallArgs = JSONField()
    server = JSONField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    download_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=True, null=True)

    def __str__(self):
        return self.packageName



class SubmitPackage(models.Model):
    id = models.AutoField(primary_key=True)
    package = models.FileField(upload_to="uploads/", validators=[validate_file_extension])
    packageName = models.CharField(max_length=100, blank=True, null=True)
    packageArgs = JSONField(default={})
    packageUninstallArgs = JSONField(default={})
    server = JSONField(default={})
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    created_at = models.DateTimeField(auto_now_add=True, editable=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=True, null=True)

    def __str__(self):
        return self.packageName

class Setting(models.Model):
    do_update_packages = models.BooleanField(default=False)

    def __str__(self):
        return "Site settings"
