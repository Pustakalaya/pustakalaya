from django.shortcuts import render
from .models import Audio
from django.views.generic import DetailView
from pustakalaya_apps.review_system.models import Review
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger


def audios(request):
    audios = Audio.objects.all()
    return render(request, 'audio/audios.html', {'audios': audios})


class AudioDetailView(DetailView):
    model = Audio
    def get(self, request, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        # review system data extractions
        data_review = Review.objects.filter(content_id=self.object.pk, content_type='audio', published=True)

        #adding pagination to the review system
        ##########################Review pagination add########################
        #print(len(data_review))
        length = len(data_review)
        number_per_page = 15
        if length > number_per_page:
            #print("inside pagination")
            # for pagination we have following code
            paginator = Paginator(data_review, number_per_page)
            page = request.GET.get('page')
            try:
                users = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                users = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 7777), deliver last page of results.
                users = paginator.page(paginator.num_pages)

            context["paginated_data"] = users

            ########################Review Pagination end########################
        if length > 0 and length <= number_per_page:
            context["data_review"]= data_review


        return self.render_to_response(context)

    template_name = "audio/audio_detail.html"

