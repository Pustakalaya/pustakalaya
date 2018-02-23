from django.shortcuts import render
from .models import Audio
from django.views.generic import DetailView
from pustakalaya_apps.review_system.models import Review


def audios(request):
    audios = Audio.objects.all()
    return render(request, 'audio/audios.html', {'audios': audios})


class AudioDetailView(DetailView):
    model = Audio
    def get(self, request, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        # review system data extractions
        data_review = Review.objects.filter(content_id= self.object.pk,content_type='audio',published=True)
        context["data_review"]= data_review
        return self.render_to_response(context)

    template_name = "audio/audio_detail.html"

