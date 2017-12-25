from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from pustakalaya_apps.video.models import Video
from .forms import VideoFileUploadForm


class AddVideoView(CreateView):
    model = Video
    fields = [
                'title',
                'collections',
                'education_levels',
                'languages',
                'publisher',
                'video_director',
                'video_genre',
                'keywords',
                'video_series',
                'license_type'
    ]

    template_name = "dashboard/video/video_add.html/"
    success_url = reverse_lazy("dashboard:profile")

    def clean(self, AddVideoView):
        cleaned_data = super(AddVideoView, self).clean()
        title = cleaned_data.get('title')
        collections = cleaned_data.get('collections')
        education_levels = cleaned_data.get('education_levels')
        languages = cleaned_data.get('languages')
        publisher = cleaned_data.get('publisher')
        video_director = cleaned_data.get('video_director')
        video_genre = cleaned_data.get('video_genre')
        keywords = cleaned_data.get('keywords')
        video_series = cleaned_data.get('video_series')
        license_type = cleaned_data.get('license_type')

        if not title and not collections and not education_levels and not languages and not video_director and not video_genre and not publisher and not keywords and not video_series and not license_type:
            raise cleaned_data.ValidationError('You have to write something!')

    def get_context_data(self, **kwargs):
        context = super(AddVideoView, self).get_context_data(**kwargs)
        if self.request.POST:
            file_upload_form = VideoFileUploadForm(self.request.POST)
            if file_upload_form.is_valid():
                file_upload_form.save()

            context['video_file_upload_form'] = VideoFileUploadForm(self.request.POST)
        else:
            context['video_file_upload_form'] = VideoFileUploadForm()

        return context


class UpdateVideoView(UpdateView):
    model = Video

    fields = [
                'title',
                'collections',
                'education_levels',
                'languages',
                'publisher',
                'video_director',
                'video_genre',
                'keywords',
                'video_series',
                'license_type'
    ]

    template_name = "dashboard/video/video_edit.html/"
    success_url = reverse_lazy("dashboard:profile")

    def clean(self, UpdateVideo):
        cleaned_data = super(UpdateVideo, self).clean()
        title = cleaned_data.get('title')
        collections = cleaned_data.get('collections')
        education_levels = cleaned_data.get('education_levels')
        languages = cleaned_data.get('languages')
        publisher = cleaned_data.get('publisher')
        video_director = cleaned_data.get('video_director')
        video_genre = cleaned_data.get('video_genre')
        keywords = cleaned_data.get('keywords')
        video_series = cleaned_data.get('video_series')
        license_type = cleaned_data.get('license_type')

        if not title and not collections and not education_levels and not languages and not video_director and not video_genre and not publisher and not keywords and not video_series and not license_type:
            raise cleaned_data.ValidationError('You have to write something!')


class DeleteVideoView(SuccessMessageMixin, DeleteView):
    model = Video

    fields = [
                'title',
                'collections',
                'education_levels',
                'languages',
                'publisher',
                'video_director',
                'video_genre',
                'keywords',
                'video_series',
                'license_type'
    ]

    template_name = "dashboard/video/video_delete.html/"
    success_url = 'dashboard:profile'
    success_message = "was deleted successfully"
