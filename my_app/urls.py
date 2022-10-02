from my_app.views import PersonView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people', PersonView, basename='person')
urlpatterns = router.urls