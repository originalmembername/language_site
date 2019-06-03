from django.db import models

class Vocabs(models.Model):
    # german vocab
    german = models.CharField(max_length=255, null=False)
    # english translation
    english = models.CharField(max_length=255, null=False)

    class Meta:
        ordering = ('german',)

    def __str__(self):
        return "{} - {}".format(self.german, self.english)
    