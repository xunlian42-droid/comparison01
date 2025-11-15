<<<<<<< HEAD
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    # 全体のホームページ（各アプリへのリンクを表示）
    path('', views.index, name='index'),  # {% url 'home:index' %}

]
=======
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    # 全体のホームページ（各アプリへのリンクを表示）
    path('', views.index, name='index'),  # {% url 'home:index' %}

]
>>>>>>> 02eda6b (2025_1115_mypage_custom)
