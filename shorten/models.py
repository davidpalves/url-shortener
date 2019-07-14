from django.db import models
import random
import string


class Encurtador(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='urls'
    )
    url_redirect = models.URLField(max_length=500)
    slug = models.SlugField(max_length=80, unique=True, default='')
    count_redirects = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = self.get_hash()
        super(Encurtador, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_hash(self):
        tokens = string.ascii_lowercase+string.ascii_uppercase+string.digits
        max_char = 7
        _hash = ''

        _hash += _hash.join(random.choice(tokens) for y in range(max_char))

        while Encurtador.objects.filter(slug=_hash):
            _hash += ''.join(random.choice(tokens) for y in range(max_char))

        return _hash

    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLs'
