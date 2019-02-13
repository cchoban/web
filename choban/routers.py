from rest_framework import routers
from api.viewsets import ArticleViewSet, SubmitPackageViewSet, LoginViewset, RegisterViewset, GetTokenViewset, UserAccount

router = routers.DefaultRouter()

router.register(r'packages', ArticleViewSet, "Packages")
router.register(r'token', GetTokenViewset, "GetToken")
router.register(r'login', LoginViewset, "LoginAPI")
router.register(r'register', RegisterViewset, "RegisterAPI")
router.register(r'user', UserAccount, "UserSerializer")
router.register(r'push', SubmitPackageViewSet, "PushApi")
