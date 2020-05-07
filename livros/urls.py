from rest_framework import routers
from livros.views import LivroViewSet

router = routers.DefaultRouter()
router.register(r'', LivroViewSet, basename='livros')

livros_urls = router.urls