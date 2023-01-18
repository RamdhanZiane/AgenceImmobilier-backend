from django.test import TestCase, Client
from .models import Annonce

# Create your tests here.

class AnnonceTestCase(TestCase):
    def setUp(self) -> None:
        client = Client()
        Annonce.objects.create(annonceur=1, titre='titre annonce', categorie='V', type='T', description='no desc', prix=44, surface=4)

    def has_desc(self):
        # Annonce.objects.get(annonceur=1)
        # self.assertEqual()
        res = self.client.get('/agence-api/annonces')
        self.assertEqual(res.status_code, 200)