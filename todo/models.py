from unittest.util import _MAX_LENGTH
from random import choice
from django.db import models

product_status = [property
                            (1, 'si'),
                            ( 2,'no' )
]

class tarea (models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField (max_length = 100, unique = True)
    lugar = models.CharField (max_length = 100)
    def __str__(self):
        return self.nombre
    
    