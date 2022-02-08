from django.urls import path, include
from . import views


urlpatterns = [
    # Authetication urls
    # path('auth/',include([
    #     path('register', views.RegisterView.as_view(), name="register"),
    #     path('login', views.LoginView.as_view(), name="login"),
    #     path('logout', views.LogoutView.as_view(), name="logout"),
    #     path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # ])),

    path('greenhouse/', include([
        path('configure', views.ConfigureGreenhouseView.as_view()),
        path('get/', views.GetUserGreenhousesView.as_view()),
        path('get/<int:id>', views.GetUserGreenhousesView.as_view()),
        path('update/<int:id>', views.UpdateGreenhouseView.as_view()),
    ]))
]
