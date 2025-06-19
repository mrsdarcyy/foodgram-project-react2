from django.core.management import BaseCommand

from recipes.models import Tag


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        data = [
            {'name': 'Завтрак', 'color': '#43e070', 'slug': 'breakfast'},
            {'name': 'Обед', 'color': '#c0ed09', 'slug': 'lunch'},
            {'name': 'Ужин', 'color': '#8775D2', 'slug': 'supper'}]
        Tag.objects.bulk_create(Tag(**tag) for tag in data)
        self.stdout.write(self.style.SUCCESS('Все тэги загружены!'))
