from django.urls import path
from chat import views

urlpatterns = [
    path('',views.home,name='home'),
    path('join',views.main_view,name='man_view'),
    path('signup',views.signupfunc,name='signupfunc'),
    path('login',views.loginfunc, name='login'),
    # path('logout',views.logoutfunc,name='logout'),
    path('leave',views.leave,name="leave")
]