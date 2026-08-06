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