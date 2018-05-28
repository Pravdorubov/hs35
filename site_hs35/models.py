from django.db import models

class STATUS:
    PUPIL = 'PUPIL'
    TEACHER = 'TEACHER'
    PARENT = 'PARENT'


class DISCIPLINE:
    MATH = 'Mathematic'  
    INFO = 'Informatic'   


STATUS_CHOICES = (
    (STATUS.PUPIL, 'Ученик'),
    (STATUS.TEACHER, 'Учитель'),
    (STATUS.PARENT, 'Родитель'),
)

DISCIPLINE_CHOICES = (
    (DISCIPLINE.MATH, 'Математика'),
    (DISCIPLINE.INFO, 'Информатика'),
)

class Ankete(models.Model):
    '''
    Анкета
    '''
    status = models.CharField('Статус', max_length=6, choices=STATUS_CHOICES, default=STATUS.PUPIL)
    name = models.CharField('Имя', max_length=256)
    wishes = models.CharField('Пожелания', max_length=1000)
    discipline = models.CharField('Дисциплина', max_length=10, choices=DISCIPLINE_CHOICES, default=DISCIPLINE.PUPIL)

    def __str__(self):
        if self.name:
            return self.name
        return self.name       

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
        ordering = ['name']

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
