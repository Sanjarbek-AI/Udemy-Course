from django import forms

from status.models import StatusModel


class StatusModelForm(forms.ModelForm):
    class Meta:
        model = StatusModel
        fields = ['user', 'content', 'image']

    def clean_content(self):
        content = self.cleaned_data.get("content", None)
        if len(content) > 240:
            raise forms.ValidationError("Content is too long !!!")
        return content

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if image is None and content is None:
            raise forms.ValidationError("Content or Image is required !")
        return super().clean()
