from rest_framework import routers
from api.viewsets import ArticleViewSet, SubmitPackageViewSet

router = routers.DefaultRouter()

router.register(r'packages', ArticleViewSet)
router.register(r'push', SubmitPackageViewSet, "PushApi")

