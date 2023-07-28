from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('stripe/', include('djstripe.urls', namespace='djstripe')),
]

from webhooks import events  # noqa F401 E402
