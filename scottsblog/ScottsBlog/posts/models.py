from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    # display post title in administration 'posts' page
    def __str__(self):
        return self.title

    # make the publication date pretty looking
    def pubDatePretty(self):
        return self.pub_date.strftime('%b %e %Y')

    # create a shorter version of the body for the main page
    def bodySummary(self):
        return self.body[:100]
