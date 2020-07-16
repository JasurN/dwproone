from django.urls import path

from views import CustomAuthToken

app_name = 'accounts'
# api/auth/
urlpatterns = [
    path('login/', CustomAuthToken.as_view()),
]