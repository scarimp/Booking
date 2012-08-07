from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from userena.models import UserenaBaseProfile

import datetime

class BaseProfile(UserenaBaseProfile):
    """ Default profile """
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name= ('user'),
                                related_name='base_profile')
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    emailAddress = models.EmailField(max_length=254)
    role = models.CharField(max_length=25)

    
