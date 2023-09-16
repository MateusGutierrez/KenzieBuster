from django.db import models


class Choices(models.TextChoices):
    G = "G"
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    NC17 = "NC-17"


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(null=True, default=None, max_length=10)
    rating = models.CharField(max_length=20, choices=Choices.choices, default=Choices.G)
    synopsis = models.TextField(null=True, default=None)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)


class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(
        "users.User", related_name="pivot_user", on_delete=models.CASCADE
    )
    movie = models.ForeignKey(
        "movies.Movie", related_name="pivot_movie", on_delete=models.CASCADE
    )
