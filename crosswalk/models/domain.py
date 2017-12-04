from django.db import models
from uuslug import uuslug


class Domain(models.Model):
    slug = models.SlugField(
        blank=True, max_length=250, unique=True, editable=False)

    name = models.CharField(max_length=250, unique=True)

    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.PROTECT
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuslug(
                self.name,
                instance=self,
                max_length=250,
                separator='-',
                start_no=2
            )
        super(Domain, self).save(*args, **kwargs)

    def __str__(self):
        return self.name