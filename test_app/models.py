from django.db import models

class MenuItem(models.Model):
    # Название элемента меню
    name = models.CharField(max_length=255)
    # URL элемента меню
    url = models.CharField(max_length=255)
    # Родитель элемента меню
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    # Сиблинг (брат или сестра) элемента меню, для меню, отображающееся в другом меню
    sibling = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='siblings')

    def __str__(self):
        return self.name
