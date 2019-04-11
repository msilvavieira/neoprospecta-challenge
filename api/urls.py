from django.urls import include, path, re_path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'entry', views.FastaViewSet)

urlpatterns = [
    path('', views.FastaListView.as_view()),
    path('', include(router.urls)),
]
