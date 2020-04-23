from django.db import models


class Subject:
    name = models.CharField(max_length=100)
    # reg_date = models.DateTimeField('register date')
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)


# class User:
#     id = models.
#     name = models.Charfield(max_length=20)
