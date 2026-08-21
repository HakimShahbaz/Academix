from django import template

register = template.Library()

@register.inclusion_tag(
    "includes/sortable_header.html",
    takes_context=True,
)
def sortable_header(context, field, label):
    current_sort = context["request"].GET.get("sort", "")

    if current_sort == field:
        next_sort = f"-{field}"
    else:
        next_sort = field

    return {
        "field": field,
        "label": label,
        "current_sort": current_sort,
        "next_sort": next_sort,
        "query": context["request"].GET.get("q", ""),
    }
