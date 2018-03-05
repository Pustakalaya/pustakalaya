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


class AudioFileUploadForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(AudioFileUploadForm, self).clean()
        #print(cleaned_data)

    class Meta:
        model = AudioFileUpload
        fields = (
            'file_name',
            'upload',
        )

    def __init__(self, *args, **kwargs):
        super(AudioFileUploadForm, self).__init__(*args, **kwargs)

        self.fields['upload'].widget.attrs = {
            'class': 'btn btn-small btn-primary btn-block',
            'name': 'myCustomName',
            'placeholder': 'Upload file'
        }


# Audio child forms.
AudioFileUploadFormSet = inlineformset_factory(
    Audio,
    AudioFileUpload,
    form=AudioFileUploadForm,
    extra=1,
    can_delete=False,
    can_order=False
)



class VideoForm(forms.ModelForm):
    class Meta:
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

class VideoFileUploadForm(forms.ModelForm):
    # def clean(self):
    #     cleaned_data = super(VideoFileUploadForm, self).clean()
    #     #print(cleaned_data)

    class Meta:
        model = VideoFileUpload
        fields = (
            'file_name',
            'upload',
        )

    def __init__(self, *args, **kwargs):
        super(VideoFileUploadForm, self).__init__(*args, **kwargs)

        self.fields['upload'].widget.attrs = {
            'class': 'btn btn-small btn-primary btn-block',
            'name': 'myCustomName',
            'placeholder': 'Upload file'
        }



# Audio child forms.
VideoFileUploadFormSet = inlineformset_factory(
    Video,
    VideoFileUpload,
    form=VideoFileUploadForm,
    extra=1,
    can_delete=False,
    can_order=False
)


