from django.db import models

# Create your models here.
class Feature:
    id: int
    name: str
    details: str
    is_true: bool       # For each features check if they are True or Not