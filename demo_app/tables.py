from django.utils.safestring import mark_safe
from django_tables2 import Table, Column


class BasicTable(Table):
    name = Column()
    number = Column()
    link = Column()
    button = Column()

    def render_link(self, value):
        return mark_safe('<a href="/">{}</a>'.format(value))

    def render_button(self, value):
        return mark_safe('<a class="btn waves-effect" href="/">{}</a>'.format(value))
