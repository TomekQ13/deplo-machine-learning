from django.db import models
from django.utils.translation import gettext_lazy as _
import pandas as pd


class Prediction(models.Model):

    age = models.IntegerField()

    class Embarked(models.TextChoices):
        CHERBOURG = 'C', _('Cherbourg')
        QUEENSTOWN = 'Q', _('Queenstown')
        SOUTHAMPTION = 'S', _('Southampton')

    embarked = models.CharField(
        max_length=1,
        choices=Embarked.choices
    )

    class Pclass(models.TextChoices):
        FIRST = '1', _('First class')
        SECOND = '2', _('Second class')
        THIRD = '3', _('Third class')

    pclass = models.CharField(
        max_length=1,
        choices=Pclass.choices,
        verbose_name='Ticket class'
    )

    class Sex(models.TextChoices):
        MALE = 'male', _('Male')
        FEMALE = 'female', _('Female')

    sex = models.CharField(
        max_length=6,
        choices=Sex.choices
    )

    sibsp = models.IntegerField(
        verbose_name='Number of siblings or spouses abord'
    )
    parch = models.IntegerField(
        verbose_name='Number of children or parents abord'
    )
    fare = models.IntegerField(verbose_name='Ticket price')

    prediction = models.IntegerField()

    def predict(self, pipeline):
        """
        This method predicts the change of survival.
        It has to be used after the object is saved to the database to perform validations of inputs.
        """
        df = pd.DataFrame.from_dict({
            "Age": [self.age],
            "Embarked": [self.embarked],
            "Pclass": [self.pclass],
            "Sex": [self.sex],
            "SibSp": [self.sibsp],
            "Parch": [self.parch],
            "Fare": [self.fare]
        })
        df = df.astype({"Pclass": 'int32'})
        prediction = pipeline.predict_proba(df)[0][1]
        self.prediction = round(prediction * 10000)
        return prediction
