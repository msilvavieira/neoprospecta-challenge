from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from rest_framework.viewsets import ModelViewSet
from api.models import Entry, Kingdom, Species
from api.serializers import EntrySerializer, KingdomSerializer, SpeciesSerializer



class FastaListView(View):
    model = Entry
    queryset = Entry.objects.all()

    def get(self, request):
        paginator = Paginator(self.queryset, 1000)
        page = request.GET.get('page')
        entries = paginator.get_page(page)

        context = {
            'queryset': self.queryset,
            'entries': entries
        }

        return render(request, 'entry_list.html', context)



class FastaViewSet(ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    from rest_framework import filters
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        queryset = Entry.objects.all()

        access_id = self.request.query_params.get('access_id', None)
        kingdom = self.request.query_params.get('kingdom', None)
        species = self.request.query_params.get('species', None)
        if kingdom is not None:
            queryset = queryset.filter(kingdom__label=kingdom)
        elif species is not None:
            queryset = queryset.filter(species__label=species)
        elif access_id is not None:
            queryset = queryset.filter(access_id=access_id)

        return queryset

