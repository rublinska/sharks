<<<<<<< HEAD
=======

>>>>>>> 416b42aab500af35c8af310b942f535a8ddf82fe
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class User(models.Model):
    surname = models.CharField(max_length=32, default=None, blank=False, null=True)
    name = models.CharField(max_length=32, default=None, blank=False, null=True)
    email = models.EmailField(default=None, blank=False, null=True)
    phone_regex = RegexValidator(regex=r'^\+?380?\d{9}$',
                                message = ("Phone number must be entered in the format: '+38 073 000 33 00'."))
    phone_number = models.CharField(validators=[phone_regex], max_length=16, blank=True)

    def __str__(self):
        return "%s %s" % (self.surname, self.name)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class Org(models.Model):
    user = models.ForeignKey(User, blank=False, default=None, null=True, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=32, default=None, blank=False, null=True)
    description = models.TextField(max_length=1024, blank=True, default=None)
<<<<<<< HEAD
    avatar = models.ImageField(upload_to='static/media/events_gallery/admins', blank=False, null=True)
=======
    avatar = models.ImageField(upload_to='sharks-blog/static/media/events_gallery/orgs', blank=False, null=True)
>>>>>>> 416b42aab500af35c8af310b942f535a8ddf82fe

    def __str__(self):
        return "%s" % self.nickname

    class Meta:
        verbose_name = "Org"
        verbose_name_plural = "Orgs"