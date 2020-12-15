from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.crypto import get_random_string


class PhoneNumber(models.Model):
    Status_Choices = (
        ('V', "Verified"),
        ('E', "Expired"),
        ('P', "Pending"),
    )
    Token = models.TextField(max_length=6, default='', blank=False)
    Number = models.CharField(max_length=120, blank=False, default='+1000000000')
    Timestamp = models.DateTimeField(blank=True, editable=True, auto_now=True)
    Status = models.CharField(max_length=2, choices=Status_Choices, blank=False, default='P')
    NumberOfSentNumbers = models.PositiveIntegerField(default=0, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.RESTRICT, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.Token:
            self.Token = unique_token_sms(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{} - {}'.format(self.Number, self.Status)


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    Phone_number = models.OneToOneField(PhoneNumber, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.Phone_number)


def unique_token_sms(instance):
    model = instance.__class__
    unique_slug = get_random_string(length=6)
    while model.objects.filter(Token=unique_slug).exists():
        unique_slug = get_random_string(length=6)
    return unique_slug
