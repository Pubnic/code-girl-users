from django.db import models


class BaseQuerySet(models.query.QuerySet):
    # .delete is a queryset's method not a manager's method,
    # this is why we need a BaseQuerySet
    def delete(self):
        return super(BaseQuerySet, self).update(deleted=True)


class BaseManager(models.Manager):
    use_for_related_fields = True

    def get_queryset(self):
        return BaseQuerySet(self.model, using=self._db).filter(deleted=False)


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        'Data de criação',
        help_text='Data na qual o objeto foi criada.',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Data de atualização',
        help_text='Data na qual os dados do objeto foi atualizado no sistema.',
        auto_now=True
    )

    deleted = models.BooleanField(
        'Foi deletado?',
        help_text='Verifica se o objeto ainda está ativo no sistema.',
        default=False
    )

    objects = BaseManager()
    raw_objects = models.Manager()

    def delete(self):
        self.deleted = True
        self.save()

    class Meta:
        abstract = True
