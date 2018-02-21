"""
Dashboard forms.
"""
from django import forms
from django.forms import models
from pustakalaya_apps.document.models import Document, DocumentFileUpload
from pustakalaya_apps.audio.models import Audio, AudioFileUpload
from pustakalaya_apps.video.models import Video, VideoFileUpload
from django.forms.models import inlineformset_factory


class ProfileForm(forms.ModelForm):
    pass
    """
    Model form for profile user
    """
    #
    # class Meta:
    #     model = UserProfile
    #     fields = ["first_name", "last_name", "phone_no", "user.username"]


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = (
            'title',
            'collections',
            'document_file_type',
            'languages',
            'document_interactivity',
            'document_type',
            'license_type',
            'thumbnail',
        )

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)

        self.fields['thumbnail'].widget.attrs = {
            'class': 'btn btn-small btn-primary btn-block',
            'name': 'myCustomName',
            'placeholder': 'Item thumbnail'
        }


class DocumentFileUploadForm(forms.ModelForm):
    class Meta:
        model = DocumentFileUpload
        fields = (
            'upload',
        )

    def __init__(self, *args, **kwargs):
        super(DocumentFileUploadForm, self).__init__(*args, **kwargs)

        self.fields['upload'].widget.attrs = {
            'class': 'btn btn-small btn-primary btn-block',
            'name': 'myCustomName',
            'placeholder': 'Upload file'
        }


# Document child forms.
DocumentFileUploadFormSet = inlineformset_factory(
    Document,
    DocumentFileUpload,
    form=DocumentFileUploadForm,
    extra=1 ,
    can_delete=False,
    can_order=False
)



class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = (
            "title",
            "abstract",
            "collections",
            "education_levels",
            "languages",
            "year_of_available",
            "audio_types",
            "audio_running_time",
            "published",
            "audio_genre",
            "keywords",
            "license_type",
            "custom_license",
            "publication_year",
            "sponsors",
            "thumbnail"
        )


class AudioFileUploadForm(forms.ModelForm):
    class Meta:
        model = AudioFileUpload
        fields = ["file_name", "upload"]


class VideoFileUploadForm(forms.ModelForm):
    pass

    class Meta:
        model = VideoFileUpload
        fields = ["file_name", "upload"]
