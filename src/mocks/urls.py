from rest_framework.routers import DefaultRouter

from mocks.api import views

router = DefaultRouter()
router.register('mocks', views.MockViewSet, basename='mocks')
urlpatterns = router.urls

app_name = 'mocks'
