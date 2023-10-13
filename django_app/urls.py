from django.urls import path
from test_app import views
from django.views.generic import RedirectView
from django.contrib import admin

urlpatterns = [

    path('admin/', admin.site.urls),

    # Это правило перенаправляет корневой URL сразу на прмиер с 'my_page'
    path('', RedirectView.as_view(url='index/')),

    # 'my_page' - это пример отрисовки меню по имени
    path('index/my_page/', views.my_page, name='my_page'),

    # Здесь определен путь с переменной page, который передается в виде параметра во views.static_page.
    # Так мы можем динамически использовать любые url
    path('<path:page>/', views.static_page, name='static-page'),
]
