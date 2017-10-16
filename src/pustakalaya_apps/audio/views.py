from django.shortcuts import render
from .models import Audio
from django.views.generic import DetailView


def audios(request):
    audios = Audio.objects.all()
    return render(request, 'audio/audios.html', {'audios': audios})


class AudioDetailView(DetailView):
    model = Audio
    template_name = "audio/audio_detail.html"
