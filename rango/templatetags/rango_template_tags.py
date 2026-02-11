from django import template

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list(current_category=None):
    from rango.models import Category
    return {'categories': Category.objects.all(),
            'current_category': current_category}
