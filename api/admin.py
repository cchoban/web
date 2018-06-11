from django.contrib import admin
from .models import Package, SubmitPackage
from django.shortcuts import get_object_or_404
admin.site.register(Package)


def make_published(self, request, queryset):
    packageName = queryset.get()
    package = queryset.filter(packageName=packageName)[:1]
    for i in package:
        try:
            packageExists = get_object_or_404(Package, packageName=i.packageName)

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
        break




make_published.short_description = "Mark selected stories as published"

class SubmitPackageAdmin(admin.ModelAdmin):
    actions = [make_published]

admin.site.register(SubmitPackage, SubmitPackageAdmin)