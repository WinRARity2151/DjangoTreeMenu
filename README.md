# Django Tree Menu

Данное приложение реализует древовидное меню в Django с использованием кастомного template tag. Оно позволяет управлять меню через админку Django, а затем легко вставить его на любой странице вашего проекта.

## Задача

Разработать Django приложение (Django app), которое реализует древовидное меню, удовлетворяя следующим условиям:

- Меню должно быть реализовано в виде кастомного template tag.
- При отображении меню, все элементы, находящиеся выше текущего активного пункта меню, должны быть развернуты. То же правило применяется к первому уровню вложенности под активным пунктом.
- Данные о структуре меню должны храниться в базе данных (БД).
- Редактирование структуры меню должно быть доступно через стандартную админку Django.
- Определение активного пункта меню должно происходить на основе URL текущей страницы.
- В одном проекте может использоваться несколько меню. Они идентифицируются по названию.
- При клике на пункте меню происходит переход на страницу, указанную в URL этого пункта. URL может быть задан как явным образом, так и через именованный URL.
- Для отрисовки каждого меню должен выполняться ровно 1 запрос к БД.

Разработать django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию. {% draw_menu 'main_menu' %} 

При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.

## Особенности

Реализованный нами template tag может выполнять такие же функции, как и {% draw_menu 'main_menu' %}. Для этого просто передайте имя меню вместе с request, как это реализовано в my_page.
Таким образом бы избегаем большого дублирования кода и создания второго приложения.

Динамическая маршрутизация url адресов, позволяет редактировать меню под любые нужды напрямую через админку.

## Реализация

Сама отрисовка меню выглядит следующим образом:

![img_1](https://github.com/WinRARity2151/DjangoTreeMenu/assets/128578068/5f7375e7-7f63-4762-a4f4-5881b22cffed)

![img](https://github.com/WinRARity2151/DjangoTreeMenu/assets/128578068/36c6b682-8c93-4356-9376-d98ca65fb111)

Можно увидеть, что при отображении меню, все элементы, находящиеся выше текущего активного пункта меню, должны быть развернуты. То же правило применяется к первому уровню вложенности под активным пунктом.

Переходя на следующий пункт мы можем убедиться в том, что при клике на пункте меню происходит переход на страницу, указанную в URL этого пункта и что определение активного пункта меню происходит на основе URL текущей страницы.

![img_3](https://github.com/WinRARity2151/DjangoTreeMenu/assets/128578068/a2a970c2-49fb-4c23-b64c-0a1d2111a42d)

![img_2](https://github.com/WinRARity2151/DjangoTreeMenu/assets/128578068/34e74ce5-bd76-4bbd-b4cc-166a21329e00)

Так как в одном проекте может использоваться несколько меню, перейдем на вкладку с вложенным меню.

![img_4](https://github.com/WinRARity2151/DjangoTreeMenu/assets/128578068/10365e37-7d06-40d1-93ba-7e4c08eddff2)

Переходя к вопросу {% draw_menu 'main_menu' %}, зайдем на "Пример" (my_page) и убедимся, что в нем есть меню с необходимым для нас именем.

![img_6](https://github.com/WinRARity2151/DjangoTreeMenu/assets/128578068/b51518fe-e851-4821-8070-49440986ce58)

![img_5](https://github.com/WinRARity2151/DjangoTreeMenu/assets/128578068/7ec76c07-8d61-4e97-a73e-49968180f7d0)

Так, несмотря на то, что мы находимся в my_page меню мы видим именно от "Подраздел 1".

Теперь убедимся в том, что данные о структуре меню хранятся в базе данных (БД) и что редактирование структуры меню доступно через стандартную админку Django.

![img_7](https://github.com/WinRARity2151/DjangoTreeMenu/assets/128578068/04878a6c-b463-4e33-b31e-17797981ab14)

Добавим новый элемент.

![img_8](https://github.com/WinRARity2151/DjangoTreeMenu/assets/128578068/77fe89ff-40a4-4f38-b5ec-f334c53147db)

И, наконец, увидим наши изменения.

![img_9](https://github.com/WinRARity2151/DjangoTreeMenu/assets/128578068/3bc89886-8e20-438d-a4e6-02aeacdf1003)

## Структура Записей

- `name`: Название элемента меню (CharField, максимум 255 символов).
- `url`: URL элемента меню (CharField, максимум 255 символов).
- `parent`: Ссылка на родительский элемент меню (ForeignKey), может быть пустым (null). 
- `sibling`: Ссылка на сиблинга (соседний элемент меню) (ForeignKey), может быть пустым (null). 

Эта структура позволяет представлять древовидное меню с главным элементом и его дочерними и соседними элементами.

## Использование

- Сначала установите необходимые зависимости requirements
- Затем примените миграции
- Создайте суперпользователя (для доступа к админке)
- Запустите сервер разработки Django
- При необходимости добавляйте в нужные шаблоны template tag
