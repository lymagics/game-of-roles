from django.urls import path, include

from drf_spectacular import views

urlpatterns = [
    path('', include('auth.urls')),
    path('', include('roles.urls')),
    path('', include('mocks.urls')),
    path('schema/', views.SpectacularAPIView.as_view(), name='schema'),
    path('docs/', views.SpectacularSwaggerView.as_view(url_name='api:schema'), name='docs'),
]

app_name = 'api'
