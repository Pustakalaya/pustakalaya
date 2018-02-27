from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from pustakalaya_apps.audio.models import Audio
from .forms import AudioFileUploadForm,AudioForm, AudioFileUploadFormSet
from django.shortcuts import redirect


class AddAudioView(SuccessMessageMixin, CreateView):
    model = Audio
    form_class = AudioForm
    template_name = "dashboard/audio/audio_add.html/"
    success_url = "/dashboard/"


    def get_context_data(self, **kwargs):
        context = super(AddAudioView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["audio_form"] = AudioForm(self.request.POST)
            context['audio_file_upload_form'] = AudioFileUploadFormSet(self.request.POST, self.request.FILES, instance=self.object)

        else:
            context["audio_form"] = AudioForm()
            context['audio_file_upload_form'] = AudioFileUploadFormSet()

        return context


    def form_valid(self, form):
        context = self.get_context_data()
        # form upload inlines
        inlines = context["audio_file_upload_form"]
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
