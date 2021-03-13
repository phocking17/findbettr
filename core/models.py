from django.db import models
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.forms import USStateField


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


### All tags


class Tag_Type(models.Model):
	name=models.CharField(max_length=50)
	question = models.CharField(max_length=500)

class Arching_Tag(models.Model):
	name=models.CharField(max_length=50)

class Tag(models.Model):
	name=models.CharField(max_length=50)
	tag_type=models.ManyToManyField(Tag_Type)




# Create your models here.
class Organization(models.Model):
	name = models.CharField(max_length=200)
	street = models.CharField(max_length=300)
	city=models.CharField(max_length=100)
	state=USStateField()
	zipcode = models.CharField(max_length=5)
	description = models.CharField(max_length=1000)
	tags=models.ManyToManyField(Tag)
	overall_tags = models.ManyToManyField(Arching_Tag)

	website=models.URLField(max_length=500)
	phone_number=models.CharField(max_length=12)
	email = models.EmailField(max_length=254)
	org_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

	contact_phone_number=models.CharField(max_length=12)
	contact_email = models.EmailField(max_length=254)
	contact_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)






class Quote(models.Model):
	words= models.CharField(max_length=250)
	author= models.CharField(max_length=100)