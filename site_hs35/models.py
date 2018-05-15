from django.db import models

class STATUS:
    PUPIL = 'PUPIL'
    TEACHER = 'PUPIL'
    PARENT = 'PARENT'


STATUS_CHOICES = (
    (STATUS.PUPIL, 'Ученик', 'Ankete'),
    (STATUS.TEACHER, 'Учитель', 'Ankete'),
    (STATUS.PARENT, 'Родитель', 'Ankete'),
)

class Ankete(models.Model):
    '''
    Анкета
    '''
    status = models.CharField('Статус', max_length=6, choices=SOURCE_CHOICES, default=STATUS.PUPIL)
    name = models.CharField('Имя')

    def __str__(self):
        if self.name_short:
            return self.name_short
        return self.name_full       

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
        ordering = ['name_full']

    @classmethod
    def get_no_executor(cls):
        """
        Возвращает исполнителя NO_EXECUTOR.
        """
        return cls.objects.get_or_create(name_full=NO_EXECUTOR)[0]


    @classmethod
    def get_no_executor_id(cls):
        """
        Возвращает исполнителя NO_EXECUTOR.
        """
        return cls.objects.get_or_create(name_full =NO_EXECUTOR)[0].id
