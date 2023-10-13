from django import template
from test_app.models import MenuItem
from django.utils.safestring import mark_safe

# Объявляем register для тега
register = template.Library()

# Загружаем все элементы меню один раз и используем их везде
all_menu_items = MenuItem.objects.all()

# Функция для построения пути меню от текущего элемента к родителю
def build_menu_path(item: MenuItem) -> str:
    if item.parent:
        parent_path = build_menu_path(item.parent)
        menu_path = f'{parent_path}{item.url}'
    else:
        menu_path = f'{item.url}'
    return menu_path


# Проверяет, связан ли элемент меню с главной страницей (index)
def is_linked_to_index(menu_item: MenuItem) -> bool:
    current_item = menu_item
    while current_item.parent:
        if current_item.parent.url == '/index':
            return True
        current_item = current_item.parent
    return False


# Рекурсивно строит родительские элементы меню для текущего элемента
def render_parents(menu_html: str, item: MenuItem, prefix: str) -> str:
    if item.parent:
        menu_html = render_parents(menu_html, item.parent, prefix)
        menu_html += f'<ul><li><a href="{prefix}{build_menu_path(item.parent)}">{item.parent.name}</a></li></ul>'
    return menu_html


# Отрисовывает текущее меню и его дочерние элементы
def render_menu(current_item: MenuItem, prefix: str) -> str:
    menu_html = ''

    menu_html = render_parents(menu_html, current_item, prefix)

    menu_html += f'<ul><li>{current_item.name}</li></ul>'

    child_items = [item for item in all_menu_items if item.parent == current_item]

    if child_items:
        menu_html += '<ul>'
        for child_item in child_items:
            menu_html += f'<li><a href="{prefix}{build_menu_path(child_item)}">{child_item.name}</a></li>'
        menu_html += '</ul>'

    return f'<div class="main-menu">{menu_html}</div>'


# Обрабатывает текущий путь, удаляя завершающий слеш (если есть)
def process_current_path(current_path: str) -> str:
    current_path = current_path[:-1]
    if len(current_path.split('/')[-1]) > 0:
        current_path = '/' + current_path.split('/')[-1]
    return current_path


# Обрабатывает текущий элемент меню
# Если меню является главным (связанным с index), то сначала мы рендерим его
def process_current_item(all_menu_items: list, current_path: str, prefix: str) -> str:
    current_item = next((item for item in all_menu_items if item.url == current_path), None)
    if current_item:
        menu_html = render_menu(current_item, prefix)
        if current_item.sibling:
            if is_linked_to_index(current_item.sibling):
                menu_html = render_menu(current_item.sibling, prefix) + menu_html
            else:
                menu_html += render_menu(current_item.sibling, prefix)
        return menu_html
    return ''


# Регистрирует тег для использования в шаблонах Django
@register.simple_tag
def tree(request, name) -> str:
    # При наличии name он заносит нужное меню на страницу
    if name:
        menu_item = next((item for item in all_menu_items if item.url == name), None)
        if menu_item:
            current_path = build_menu_path(menu_item) + '/'
        name = ''
    else:
        # Если имя не указано, то используется request.path
        current_path = request.path

    prefix = request.scheme + '://' + request.get_host()
    current_path = process_current_path(current_path)
    return mark_safe(process_current_item(all_menu_items, current_path, prefix))
