from django.contrib import admin
from .models import Package, SubmitPackage, Setting, Category
from django.shortcuts import get_object_or_404

admin.site.register(Package)
admin.site.register(Setting)
admin.site.register(Category)


def make_published(self, request, queryset):
    package = queryset.all()
    for i in package:
        try:
            packageExists = Package.objects.filter(
                packageName=i.packageName).exists()

            if not packageExists:
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
                message_bit = "This package is already approved!"
                self.message_user(request, message_bit, "error")

        except Exception as e:
            pass


make_published.short_description = "Mark selected packages as published"


class SubmitPackageAdmin(admin.ModelAdmin):
    actions = [make_published]


admin.site.register(SubmitPackage, SubmitPackageAdmin)
