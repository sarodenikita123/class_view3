from django.db import models


class College(models.Model):
    Branch = [("IT", "information technology"), ("EXT", "electrical"), ("MECH", "mechanical"), ("CV", "civil")]
    name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    college = models.CharField(max_length=20)
    branch = models.CharField(max_length=20, choices=Branch)
    date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


