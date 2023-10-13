from django.shortcuts import render

# Функция отображения страницы
def static_page(request, page):
    return render(request, 'test_app/menu.html')

# Функция отображения страницы с примером
def my_page(request):
    return render(request, 'test_app/my_page.html')


