from django.urls import path
from . import views

app_name = 'task_page'

urlpatterns = [
    path("", views.index, name='index'),
    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register"),
    path("logout/", views.logout_user, name="logout"),
    path("update_user/", views.update_user, name="update_user"),
    path("task_creation/", views.task_creation, name="task_creation"),
    path("task_completion/<int:id>/", views.task_completion, name="task_completion"),
    path("task_update/<int:id>/", views.task_update, name="task_update"),
    path("task_delete/<int:id>/", views.task_delete, name="task_delete"),
    path("user_profile/", views.user_profile, name='user_profile'),
    path("task_completed/<int:id>/", views.task_completed, name='task_completed')



]

