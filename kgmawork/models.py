from django.db import models

class KgmaWork(models.Model):

    SPECIALITY = (
        ('Старший преподаватель', 'Старший преподаватель'),
        ('Лаборант', 'Лаборант'),
        ('Лектор', "Лектор"),

    )

    title = models.CharField('ФИО преподавателя', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Фото', upload_to='')
    trailer = models.CharField('Предметы', max_length=100)
    quantity = models.CharField('Контакты', max_length=100)
    speciality = models.CharField(max_length=100, choices=SPECIALITY)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Commet_TV(models.Model):
    RATING_CHOISES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    choise_show = models.ForeignKey(KgmaWork, on_delete=models.CASCADE,
                                    related_name='comment_object')
    name = models.CharField('Введите ваше имя', max_length=100)
    text = models.TextField('Ваш коммент')
    rating = models.CharField('Поставьте оценку', max_length=100, choices=RATING_CHOISES)






