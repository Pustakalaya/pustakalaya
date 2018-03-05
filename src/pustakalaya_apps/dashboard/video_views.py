from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from pustakalaya_apps.video.models import Video
from .forms import VideoFileUploadForm,VideoForm, VideoFileUploadFormSet
from django.shortcuts import redirect


class AddVideoView(SuccessMessageMixin,CreateView):
    model = Video
    form_class = VideoForm
    template_name = "dashboard/video/video_add.html/"
    success_url = "/dashboard/"

    def get_context_data(self, **kwargs):

        context = super(AddVideoView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["video_form"] = VideoForm(self.request.POST)
            context['video_file_upload_form'] = VideoFileUploadFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context["video_form"] = VideoForm()
            context['video_file_upload_form'] = VideoFileUploadFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        # form upload inlines
        inlines = context["video_file_upload_form"]
        # form = context["form"]
        status = form.is_valid()
        statusset = inlines.is_valid()
        print(status, statusset)


        if form.is_valid() and inlines.is_valid():
            # Save the object. and its children.
            self.object = form.save(commit=False)
            # Make published to no, as admin will review and set to yes.
            self.object.published = "no"
            self.object.submitted_by = self.request.user
            self.object.save()
            form.save_m2m()  # Save other m2m fields.
            # Here instance is Document.
            inlines.instance = self.object
            inlines.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

            # Handle the form in case all the invalid form.

    def form_invalid(self, form):
        print("Form is valid or invalid")
        return self.render_to_response(self.get_context_data(form=form))



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
    success_url = "/dashboard/"

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
