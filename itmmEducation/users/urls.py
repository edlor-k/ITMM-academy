from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('personal_account')

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('account/', views.personal_account, name='personal_account'),
    path('logout/', LogoutView.as_view(), name='logout'),
]