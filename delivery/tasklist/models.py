from django.db import models

import django.utils.timezone

# Create your models here.

'''Создать свой класс,
Зарегистировать его в админке,
Выполнить создание таблицы в БД,
показать работу.
Отчетность - скриншот с админки'''

class Task(models.Model): # этот класс соответсвует таблице; таблица хранит информацию по задачам
    deadline = models.DateField()
    given = models.DateTimeField ()#default=django.utils.timezone.now)
   
    description = models.CharField(max_length=1024)
    done = models.BooleanField(default=False)
    
'''
     Column    |           Type           | Collation | Nullable |             Default              
-------------+--------------------------+-----------+----------+----------------------------------
 id          | bigint                   |           | not null | generated by default as identity
 given       | timestamp with time zone |           |          | 
 deadline    | date                     |           | not null | 
 description | character varying(1024)  |           | not null | 
 done        | boolean                  |           | not null | 
'''