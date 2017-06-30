from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Product(models.Model):

    CATEGORY_CHOICES = (
        ('FD', 'Food'),
        ('BK', 'Books'),
        ('GM', 'Games'),
        ('WH','Watches'),
        ('SW','Sportswear')
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=100)

    @property
    def getimageurl(self):
        return '/img/{}.jpg'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)


class Profile(models.Model):

    user = models.OneToOneField(User, related_name='profile')
    address = models.TextField(null=True)
    phone_number = models.IntegerField(null=True)

    def __str__(self):
        return "{}, {}".format(self.user, self.phone_number)

@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Cart(models.Model):

    products = models.ManyToManyField(Product, through='ProductCount', blank=True)
    customer = models.ForeignKey(User, blank=True)
    total = models.FloatField(blank=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} ____ {}  ___{}".format(self.products.all(), self.customer, self.total)


class ProductCount(models.Model):

    product = models.ForeignKey(Product)
    cart = models.ForeignKey(Cart)
    count = models.PositiveIntegerField()

    def __str__(self):
        return "{} : {}".format(self.product, self.count)



