"""
Dashboard forms.
"""
from django import forms
from pustakalaya_apps.pustakalaya_account.models import UserProfile
from pustakalaya_apps.document.models import Document, DocumentFileUpload
from pustakalaya_apps.audio.models import Audio, AudioFileUpload
from pustakalaya_apps.video.models import Video, VideoFileUpload


class ProfileForm(forms.ModelForm):
    pass
    """
    Model form for profile user
    """
    #
    # class Meta:
    #     model = UserProfile
    #     fields = ["first_name", "last_name", "phone_no", "user.username"]


class DocumentFileUploadForm(forms.ModelForm):
    class Meta:
        model = DocumentFileUpload
        fields = ["file_name", "upload"]


class AudioFileUploadForm(forms.ModelForm):
    class Meta:
        model = AudioFileUpload
        fields = ["file_name", "upload"]


class VideoFileUploadForm(forms.ModelForm):
    pass
    class Meta:
        model = VideoFileUpload
        fields = ["file_name", "upload"]
