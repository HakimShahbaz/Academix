from django.db.models import Q

class SearchableListViewMixin:
    search_param = "q"
    search_fields = []

    def get_search_query(self):
        return self.request.GET.get(self.search_param, "").strip()

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.get_search_query()

        if not query:
            return queryset

        filters = Q()

        for field in self.search_fields:
            filters |= Q(**{f"{field}__icontains": query})

        return queryset.filter(filters).distinct()

class SortableListViewMixin:
    sort_param = "sort"
    sort_fields = []

    def get_sort_field(self):
        sort = self.request.GET.get(self.sort_param)

        if not sort:
            return None

        field = sort.lstrip("-")

        if field not in self.sort_fields:
            return None

        return sort

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_field = self.get_sort_field()
        if sort_field:
            queryset = queryset.order_by(sort_field)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_sort"] = self.request.GET.get(
            self.sort_param,
            ""
        )

        return context