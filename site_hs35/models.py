from django.db import models

class STATE:
    PUPIL = 'PUPIL'
    TEACHER = 'PUPIL'
    PARENT = 'PARENT'


STATE_CHOICES = (
    (STATE.PUPIL, 'Ученик', 'Ankete'),
    (STATE.TEACHER, 'Учитель', 'Ankete'),
    (STATE.PARENT, 'Родитель', 'Ankete'),
)

class Ankete(models.Model):
    '''
    Анкета
    '''
    external_id = models.CharField('внешний ИД', db_index=True, max_length=7, null=True, blank=True)
    subject_rf = models.CharField('Субъект РФ', max_length=50, null=True, blank=True)
    name_full = models.CharField('Полное наименование', max_length=500, default='')
    name_short = models.CharField('Краткое наименование', max_length=500, null=True, blank=True)
    name_employee = models.CharField('ФИО руководителя', max_length=200, null=True, blank=True)
    inn = models.CharField('ИНН', max_length=15, null=True, blank=True)
    orn = models.CharField('ОГРН', max_length=15, null=True, blank=True)
    legal_address = models.CharField('Юридический адрес', max_length=500, null=True, blank=True)
    actual_address = models.CharField('Фактический адрес', max_length=500, null=True, blank=True)
    phone = models.CharField('Телефон', max_length=100, null=True, blank=True)
    email = models.EmailField('Электронная почта', max_length=256, null=True, blank=True)
    more_emails = models.CharField('Дополнительные адреса электронной почты', max_length=256, default='', blank=True)
    site =models.CharField('Сайт', max_length=200, null=True, blank=True)
    count_mkd = models.IntegerField('Количество домов', null=True, blank=True)
    area_total = models.FloatField('Обслуживаемая площадь', null=True, blank=True)
    w_summ = models.FloatField('Рейтинг', null=True, blank=True)
    is_oagv = models.BooleanField('Структурное подразделение ОАГВ', default=False)

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
