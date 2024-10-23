from django.db import models



class Tusk(models.Model):
    title = models.CharField(max_lenght = 150)
    tusk_content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tusks', verbose_name="Author")
    date = models.DateTimeField()
    prioriti = models.TextField()

    def __str__(self):
        return self.title

