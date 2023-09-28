from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'category', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_title(self):
        cleaned_data = self.cleaned_data['title'].lower()
        prohibited_words_arr = self.get_prohibited_words_arr()
        for prohibited_word in prohibited_words_arr:
            if prohibited_word in cleaned_data:
                raise forms.ValidationError('В названии есть недопустимые слова')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description'].lower()
        prohibited_words_arr = self.get_prohibited_words_arr()
        for prohibited_word in prohibited_words_arr:
            if prohibited_word in cleaned_data:
                raise forms.ValidationError('В описании есть недопустимые слова')

        return cleaned_data

    @staticmethod
    def get_prohibited_words_arr():
        return ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                'радар']


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('version_title', 'version_number', 'is_current')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_current':
                field.widget.attrs['class'] = 'form-control'
