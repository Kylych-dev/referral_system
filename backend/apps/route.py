from django.urls import path
from rest_framework.routers import DefaultRouter

# from api.auth.views import RegisterView, UserAuthenticationView
# from api.v1.accounts.views import CustomUserViewSet, UserRoleViewSet


router = DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns.extend(
    [
        # registration
        # path("register/", RegisterView.as_view({"post": "register"}), name="register"),

        # # verify
        # path("verify-code/", RegisterView.as_view({"post": "verify"}), name="verify"),
        # path("resend/verify-code/", RegisterView.as_view({"post": "resend_verify"}), name="resend-verify"),
        
    ]
)