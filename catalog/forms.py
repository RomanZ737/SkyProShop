from django import forms
from .models import Product
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile


not_allowed_words = ['казино', 'криптовалюта', 'крипта',
                             'биржа', 'дешево', 'бесплатно',
                             'обман', 'полиция', 'радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'image']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'image':
                field.widget = forms.FileInput(attrs={'accept': 'image/*'})
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        name_lower = name.lower()
        for word in not_allowed_words:
            if word in name_lower:
                raise forms.ValidationError(
                    f'В названии продукта содержится недопустимое слово! '
                    f'Пожалуйста уберите это слово: {word}'
                )
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        description_lower = description.lower()
        for word in not_allowed_words:
            if word in description_lower:
                raise forms.ValidationError(
                    f'В описании продукта содержится недопустимое слово! '
                    f'Пожалуйста уберите это слово: {word}'
                )
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError(
                'Цена не может равняться нулю или иметь отрицательное значение'
            )
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if not image:
            return image

        if isinstance(image, (InMemoryUploadedFile, TemporaryUploadedFile)):
            max_size = 5 * 1024 * 1024
            if image.size > max_size:
                size_mb = image.size / (1024 * 1024)
                raise forms.ValidationError(
                    f'Размер изображения не должен превышать 5 МБ. '
                    f'Текущий размер: {size_mb:.1f} МБ'
                )

            allowed_types = ['image/jpeg', 'image/png']
            if image.content_type not in allowed_types:
                raise forms.ValidationError(
                    f'Допустимы только изображения в формате JPEG или PNG. '
                    f'Загруженный формат: {image.content_type}'
                )

        return image