from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

class GraphData(models.Model):
    file = models.FileField(upload_to="exel_data")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return '%s (date: %s)' % (self.file.name, self.pub_date)

    def get_absolute_url(self):
        return reverse('view-one-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        self.pub_date = timezone.now()
        super(GraphData, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete(False)
        super(GraphData, self).delete(*args, **kwargs)
