from django.db import models
from django.utils.translation import gettext_lazy as _


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
        choices=Pclass.choices
    )

    class Sex(models.TextChoices):
        MALE = 'male', _('Male')
        FEMALE = 'female', _('Female')

    sex = models.CharField(
        max_length=6,
        choices=Sex.choices
    )

    sibsp = models.IntegerField()
    parch = models.IntegerField()
    fare = models.IntegerField()

    prediction = models.IntegerField()

    def predict(self):
        """
        This method predicts the change of survival.
        It has to be used after the object is saved to the database to perform validations of inputs.
        """
        pass
