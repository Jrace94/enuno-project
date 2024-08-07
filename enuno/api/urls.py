from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from .views import CorpView, CustomTokenObtainPairView

router = routers.DefaultRouter()
router.register(r"corp", CorpView, "corp")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("docs/", include_docs_urls(title="Corp API")),
]
