from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from pustakalaya_apps.collection.models import Collection
from django.core.urlresolvers import reverse_lazy



class AddCollection(CreateView):
    model = Collection
    fields = '__all__'
    template_name = "dashboard/collection/collection_add.html/"
    success_url = reverse_lazy("dashboard:profile")


class CollectionList(ListView):
    model = Collection
    template_name = "dashboard/collection/collection_list.html"
