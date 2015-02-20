from django import template


register = template.Library()


@register.filter(name='add_css_class')
def add_css_class(field, css):
    return field.as_widget(attrs={"class": css})

def get_label_teams(user):
    teams = user.groups.all()
    return 'lol'