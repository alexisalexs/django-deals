from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from uuid import uuid4
#MAJOR TO-DO'S
#TODO photo field and use amazon S3 buckets to store images


class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff,
        is_active=True,
        is_superuser=is_superuser,
        last_login=now,
        date_joined=now,
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    user.save(using=self._db)
    return user





class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(
        unique=True,primary_key=False,default=uuid4,editable=False,
    )
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=30,blank=True,null=True)
    last_name = models.CharField(max_length=30,blank=True,null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.uuid)



class Item(models.Model):
    """
    THIS IS THE ITEM THAT WILL BE POSTED & TWEETED
    LINKS TO ITEM AND PHOTOS SHOULD NOT BE HARD CODED.

    MUST BE FLEXIBLE FOR ITEMS THAT ARE BOTH BRAND NEW AND
    ON SALE

    """

    item_name = models.CharField(blank=True,null=True,max_length=100)
    retail_price = models.CharField(blank=True,null=True,max_length=6)
    sale_price = models.CharField(blank=True,null=True,max_length=6)
    percent_off = models.CharField(blank=True,null=True,max_length=3)
    promo_code = models.CharField(blank=True,null=True,max_length=30)\
    #TODO configure photofield, future
    #photo = models.ImageField(upload_to)
    date_time_created = models.DateField(auto_now_add=True)
    #TODO when user model is created create a created_by field
    #created_by = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.item_name)



class Link(models.Model):
    """
    REASON WHY LINK IS ON A DIFFERENT MODEL IS TO ADD AS MANY
    LINKS AS WE NEED TO PER ITEM.
    EXAMPLE:
        A SNEAKER WILL RELEASE ON MULTIPLE SITES AND WE DO NOT
        WANT TO HARDCODE/LIMIT THE AMOUNT OF LINK INCASE THE LIST
        GETS LONG
    """
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    #EITHER SITE NAME WILL LIVE ON A DIFFERENT MODEL (doesn't seem right yet)
    #MORE THAN LIKELY LIST OF SITES WILL LIVE ON A LIST FILE. NEED TO TEST
    #WHICH ONE IS MORE EFFICIENT
    site_name = models.CharField(blank=True,null=True,max_length=50)
    site_url = models.URLField()
    date_time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.site_name)

