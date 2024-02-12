from django.db import models


class Recipes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.FloatField()
    image = models.ImageField(upload_to='', blank=True)
    author = models.IntegerField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.description} {self.cooking_steps} {self.cooking_time}'
