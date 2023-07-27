from django.urls import path

from mocks.api import views

urlpatterns = [
    path('mocks/phone/',
         views.PhoneMockViewSet.as_view({'get': 'retrieve'}),
         name='phone'),
    path('mocks/color/',
         views.ColorMockViewSet.as_view({'get': 'retrieve'}),
         name='color'),
    path('mocks/passport/',
         views.PassportMockViewSet.as_view({'get': 'retrieve'}),
         name='passport'),
]

app_name = 'mocks'
