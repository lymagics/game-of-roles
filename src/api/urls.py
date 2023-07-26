from django.urls import path

from drf_spectacular import views

urlpatterns = [
    path('schema/', views.SpectacularAPIView.as_view(), name='schema'),
    path('docs/', views.SpectacularSwaggerView.as_view(url_name='api:schema'), name='docs'),
]

app_name = 'api'
