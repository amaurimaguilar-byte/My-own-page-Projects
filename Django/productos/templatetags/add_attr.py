from django import template
registrer = template.Library()


@registrer.filter(name="add_attr")
def add_attr(field, css):
    attrs = {}
    clase, valor = css.split(':')
    attrs[clase] = valor
    return field.as_wideget(attrs=attrs)
