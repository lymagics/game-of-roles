from django.urls import path, include

from drf_spectacular import views

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/register/', include('dj_rest_auth.registration.urls')),
    path('schema/', views.SpectacularAPIView.as_view(), name='schema'),
    path('docs/', views.SpectacularSwaggerView.as_view(url_name='api:schema'), name='docs'),
]

app_name = 'api'
