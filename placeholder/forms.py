from io import BytesIO
from PIL import Image

from django import forms
from django.core.cache import cache


class ImageForm(forms.Form):
    """Form for validate image placeholder"""

    width = forms.IntegerField(min_value=1, max_value=2000)
    height = forms.IntegerField(min_value=1, max_value=2000)
    color = forms.CharField()

    def generate(self, image_format='PNG'):
        """Generate an image and return in into byte form"""
        width = self.cleaned_data['width']
        height = self.cleaned_data['height']
        color = self.cleaned_data['color']

        key = '{}.{}.{}.{}'.format(width, height, color, image_format)
        content = cache.get(key)

        if content is None:
            image = Image.new('RGB', (width, height), '#' + color)
            content = BytesIO()
            image.save(content, image_format)
            content.seek(0)
            cache.set(key, content, 60 * 60) # one hour
        return content