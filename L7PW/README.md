# Unit-тестирование в Django

### Как мы описали тесты?

*   Создали проект [unittesting](./unittesting)
*   Создали приложение [smaple](./sample)
*   Подключили приложение в [settings.py](./unittesting/unittesting/settings.py)

```python
INSTALLED_APPS = [
    ...
    'sample',
]
```

*   Описали test-case в [tests.py](./sample/tests.py) приложения.

### Как мы запустили тесты?

*   Использовали [manage.py](./unittesting/manage.py) проекта (переменную окружения PYTHONPATH следует использовать, если мы запускаем проект из консоли linux и python при этом не может найти путь к подключенному приложению).

```
PYTHONPATH=. python3 unittesting/manage.py test
```

*   Удовлетворились выводом консоли.

```
Creating test database for alias 'default'...
...
----------------------------------------------------------------------
Ran 3 tests in 0.008s

OK
Destroying test database for alias 'default'...
```

## Полезные ссылки

1.  [Общее описание тестирования в Django](https://docs.djangoproject.com/en/1.10/topics/testing/overview/)
2.  [Подробное описание классов модуля django.test](https://docs.djangoproject.com/en/1.10/topics/testing/tools/)
3.  [Библиотека Unittest](https://docs.python.org/3/library/unittest.html)
