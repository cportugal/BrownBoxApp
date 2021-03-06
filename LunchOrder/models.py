from django.db import models
from django.contrib.auth.models import User
# Create your models here

class UserProfile(models.Model):
    #User Info- need to get OpenId thing in here...
    user = models.ForeignKey(User, unique=True)
    department = models.CharField(max_length = 20)
    room = models.CharField(max_length = 4) 
    iskitchenstaff = models.BooleanField()



CATEGORY_CHOICES =( 
('M', 'Main'),
('V', 'Veggie'),
('C', 'Condiments'),
('WS', 'Weekly Special'),
('CH', 'Cheeses'),
('D', 'Dressings'),
('CO', 'Cookies'),
)
class Ingredient(models.Model):
    name = models.CharField(max_length = 20)  
    category = models.CharField(choices=CATEGORY_CHOICES, max_length = 2)
    def __unicode__(self): 
        return "{0} : {1}".format(self.category,self.name)
class Meal(models.Model):
    ingredients = models.ManyToManyField("Ingredient")
    def __unicode__(self):
        try:
            return "{0}".format(self.ingredients.all()[0].name)
        except IndexError:
            return "empty"
class Order(models.Model):
    STYLE_CHOICES =( 
('R', 'Roll'),
('W', 'Wrap'),
('S', 'Salad'),
)
    PACKAGE_CHOICES =( 
('BO', 'Box'),
('BA', 'Bag'),
)
    user = models.ForeignKey(User)
    meal = models.ForeignKey(Meal)
    style = models.CharField(choices=STYLE_CHOICES, max_length=1)
    submitted = models.DateTimeField()
    pickup = models.DateTimeField()
    confirmed = models.BooleanField()
    isfilled = models.BooleanField()
    ispayed = models.BooleanField()
    package = models.CharField(choices=PACKAGE_CHOICES,max_length=2)
    def __unicode__(self):
        return "Order: {0} {1} ".format(self.meal, self.get_style_display())
