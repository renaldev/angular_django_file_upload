from django.test import TestCase
from django.core.urlresolvers import reverse
import json


class GraphDataViewTests(TestCase):

    def test_get_start_page(self):
        response = self.client.get(reverse('graphdata-add'))
        self.assertEqual(response.status_code, 200)

    def test_post_file_data(self):

        with open('graphs/static/graphs/for_tests/Книга2.xlsx', 'rb') as fp:
            response = self.client.post(reverse('graphdata-add'), {'file': fp}, format='multipart')
            self.assertEqual(response.status_code, 302)

            response = self.client.get(response.url)
            self.assertEqual(response.status_code, 200)
            data = json.loads(str(response.content, encoding='utf8'))
            self.assertEqual(len(data["data"]), 10)
