from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from pustakalaya_apps.audio.models import Audio
from .forms import AudioFileUploadForm


class AddAudioView(CreateView):
    model = Audio
    fields = [
                'title',
                'collections',
                'education_levels',
                'languages',
                'publisher',
                'audio_types',
                'audio_read_by',
                'audio_genre',
                'keywords',
                'audio_series',
                'license_type'
    ]

    template_name = "dashboard/audio/audio_add.html/"
    success_url = reverse_lazy("dashboard:profile")

    def clean(self, AddAudioView):
        cleaned_data = super(AddAudioView, self).clean()
        title = cleaned_data.get('title')
        collections = cleaned_data.get('collections')
        education_levels = cleaned_data.get('education_levels')
        languages = cleaned_data.get('languages')
        audio_types = cleaned_data.get('audio_types')
        publisher = cleaned_data.get('publisher')
        audio_types = cleaned_data.get('audio_types')
        audio_read_by = cleaned_data.get('audio_read_by')
        audio_genre = cleaned_data.get('audio_genre')
        keywords = cleaned_data.get('keywords')
        audio_series = cleaned_data.get('audio_series')
        license_type = cleaned_data.get('license_type')

        if not title and not collections and not education_levels and not languages and not \
            audio_types and not publisher and not audio_types and not keywords and not audio_read_by \
            and not audio_genre and not audio_series and not license_type:
            raise cleaned_data.ValidationError('You have to write something!')

    def get_context_data(self, **kwargs):
        context = super(AddAudioView, self).get_context_data(**kwargs)
        if self.request.POST:
            file_upload_form = AudioFileUploadForm(self.request.POST)
            if file_upload_form.is_valid():
                file_upload_form.save()

            context['audio_file_upload_form'] = AudioFileUploadForm(self.request.POST)
        else:
            context['audio_file_upload_form'] = AudioFileUploadForm()

        return context


class UpdateAudioView(UpdateView):
    model = Audio
    fields = [
                'title',
                'collections',
                'education_levels',
                'languages',
                'publisher',
                'audio_types',
                'audio_read_by',
                'audio_genre',
                'keywords',
                'audio_series',
                'license_type'
    ]

    template_name = "dashboard/audio/audio_edit.html/"
    success_url = reverse_lazy("dashboard:profile")

    def clean(self, UpdateAudioView):
        cleaned_data = super(UpdateAudioView, self).clean()
        title = cleaned_data.get('title')
        collections = cleaned_data.get('collections')
        education_levels = cleaned_data.get('education_levels')
        languages = cleaned_data.get('languages')
        audio_types = cleaned_data.get('audio_types')
        publisher = cleaned_data.get('publisher')
        audio_types = cleaned_data.get('audio_types')
        audio_read_by = cleaned_data.get('audio_read_by')
        audio_genre = cleaned_data.get('audio_genre')
        keywords = cleaned_data.get('keywords')
        audio_series = cleaned_data.get('audio_series')
        license_type = cleaned_data.get('license_type')

        if not title and not collections and not education_levels and not languages and not \
            audio_types and not publisher and not audio_types and not keywords and not audio_read_by \
            and not audio_genre and not audio_series and not license_type:
            raise cleaned_data.ValidationError('You have to write something!')


class DeleteAudioView(SuccessMessageMixin, DeleteView):
    model = Audio
    fields = [
                'title',
                'collections',
                'education_levels',
                'languages',
                'publisher',
                'audio_types',
                'audio_read_by',
                'audio_genre',
                'keywords',
                'audio_series',
                'license_type'
    ]

    template_name = "dashboard/audio/audio_delete.html/"
    success_url = 'dashboard:profile'
    success_message = "was deleted successfully"
