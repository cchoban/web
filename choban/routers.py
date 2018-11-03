from rest_framework import routers
from api.viewsets import ArticleViewSet, SubmitPackageViewSet, LoginViewset, GetTokenViewset

router = routers.DefaultRouter()

router.register(r'packages', ArticleViewSet, "sea")
router.register(r'token', GetTokenViewset, "GetToken")
router.register(r'login', LoginViewset, "LoginAPI")
router.register(r'push', SubmitPackageViewSet, "PushApi")

