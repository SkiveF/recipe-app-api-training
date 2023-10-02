""""
URL mappings for the usr API
"""

from django.urls import path

from user import views as v

app_name = 'user'

urlpatterns = [
    path('create/', v.CreateUserView.as_view(), name='create'),
    path('token/', v.CreateTokenView.as_view(), name='token'),
    path('me/', v.ManegeUserview.as_view(), name='me'),
]
