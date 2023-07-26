from rest_framework.routers import DefaultRouter

from roles.api.views import RoleViewSet

router = DefaultRouter()
router.register('roles', RoleViewSet, basename='roles')
urlpatterns = router.urls

app_name = 'roles'
