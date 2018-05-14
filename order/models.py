from django.db import models
import datetime
from landing.models import User
from event.models import Event

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, blank=False, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False, default=1.)
    sum = models.IntegerField(blank=True)
    datetime = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s bought %s ticket(s) on %s at %s" % (self.user.surname, self.amount, self.event, self.datetime)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def save(self, *args, **kwargs):
        price = self.event.price
        self.sum = price*self.amount
        super(Order,self).save(*args, **kwargs)