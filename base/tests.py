# from django.test import TestCase
# from rest_framework.test import APIRequestFactory, RequestsClient
# from .view import ping, posts
# from django.urls import reverse
#
# factory = APIRequestFactory()
# url = reverse('ping')
# request = factory.get(url)
# response = ping(request)
# response.render()
# assert response.status_code == 200
#
#
# factory = APIRequestFactory()
# url = reverse('posts')
# request = factory.get(url)
# response = posts(request)
# response.render()
# assert response.status_code == 400
#
# factory = APIRequestFactory()
# url = reverse('posts', args = (tag='hello', sortBy='hello'))
# request = factory.get(url)
# response = posts(request)
# response.render()
# assert response.status_code == 400
#
# factory = APIRequestFactory()
# url = reverse('posts', args = (tag='tech', sortBy='likes'))
# request = factory.get(url)
# response = posts(request)
# response.render()
# assert response.status_code == 200
#
# factory = APIRequestFactory()
# url = reverse('posts', args = (tag='tech,culture', sortBy='likes'))
# request = factory.get(url)
# response = posts(request)
# response.render()
# assert response.status_code == 200
