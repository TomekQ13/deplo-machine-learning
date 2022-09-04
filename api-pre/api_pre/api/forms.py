from django.forms import ModelForm
from .models import Prediction


class PredictionForm(ModelForm):
    class Meta:
        model = Prediction
        fields = [
            'age',
            'sex',
            'embarked',
            'pclass',
            'sibsp',
            'parch',
            'fare'
        ]
