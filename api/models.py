from django.db import models
from django.contrib.postgres.fields import JSONField
from .validators import validate_file_extension
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse


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
    packageIcon = models.ImageField(upload_to="media/", default='noimage.png')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    showcase = models.BooleanField(default=False)
    download_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=True, null=True)

    def __str__(self):
        return self.packageName

    def get_absolute_url(self):
        return reverse('getPackage', kwargs={'packageName': self.packageName})


class SubmitPackage(models.Model):
    id = models.AutoField(primary_key=True)
    packageName = models.CharField(max_length=100, blank=True, null=True)
    packageArgs = JSONField()
    packageUninstallArgs = JSONField()
    server = JSONField()
    packageIcon = models.ImageField(upload_to="media/", default='noimage.png')
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    created_at = models.DateTimeField(auto_now_add=True, editable=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=True, null=True)

    def __str__(self):
        return self.packageName

    def save(self, *args, **kwargs):
        from .helpers import compress_icon

        if self.packageIcon:
            self.packageIcon = compress_icon(self.packageIcon)
        super(SubmitPackage, self).save(*args, **kwargs)

class Setting(models.Model):
    do_update_packages = models.BooleanField(default=False)

    def __str__(self):
        return "Site settings"
