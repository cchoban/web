from django.contrib import admin
from .models import Package, SubmitPackage, Setting, Category
from django.shortcuts import get_object_or_404
from . import Logger as log

admin.site.register(Package)
admin.site.register(Setting)
admin.site.register(Category)


def make_published(self, request, queryset):
    package = queryset.all()
    for i in package:
        try:
            packageExists = Package.objects.filter(
                packageName=i.packageName)

            if not packageExists.exists():
                Package.objects.create(
                    packageName=i.packageName,
                    packageArgs=i.packageArgs,
                    packageUninstallArgs=i.packageUninstallArgs,
                    server=i.server
                )
                queryset.delete()

                if queryset:
                    message_bit = "Successfully moved to approved packages."
                self.message_user(request, message_bit)
            else:
                package = packageExists[0]
                message_bit = "Updated version from '{}' to '{}' of package '{}'".format(
                    package.packageArgs['version'], i.packageArgs['version'], i.packageName)
                packageExists.update(
                    packageArgs=i.packageArgs, packageUninstallArgs=i.packageUninstallArgs, server=i.server)
                queryset.delete()
                self.message_user(request, message_bit, "success")

        except Exception as e:
            log.new(e).logError()
            pass


make_published.short_description = "Mark selected packages as published"


class SubmitPackageAdmin(admin.ModelAdmin):
    actions = [make_published]


admin.site.register(SubmitPackage, SubmitPackageAdmin)
