# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Items(models.Model):
	name= models.CharField(max_length=20)
	price= models.IntegerField(default=0)

