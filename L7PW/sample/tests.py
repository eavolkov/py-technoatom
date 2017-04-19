from django.test import TestCase
from random import randint


class SampleTestCase(TestCase):
    '''TestCase для примера'''

    def test_ok_reponse(self):
        '''
        Когда запрашиваем в параметрах число,
        должны получать OK (проверяем статус
        и содержимое ответа).
        '''
        response = self.client.get('/42/')
        self.assertEqual(200, response.status_code)
        content = response.content.decode('utf-8')
        self.assertRegex(content, r'^\s*OK\s*$')

    def test_fail_reponse(self):
        '''
        Когда запрашиваем в параметрах не число,
        должны получать Bad Request (проверяем
        статус ответа).
        '''
        response = self.client.get('/wrong/')
        self.assertEqual(400, response.status_code)

    def test_randomly_fail(self):
        '''
        Когда не везет, фэйлим тест. Ой, все
        '''
        if not randint(0, 1):
            self.fail('No luck! Try again, loser...')
