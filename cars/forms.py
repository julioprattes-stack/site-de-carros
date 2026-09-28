from django import forms
from cars.models import CarModel

class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')

        if value < 15000:
            self.add_error('value', 'Valor mínimo do carro deve ser de R$ 15.000')

        return value