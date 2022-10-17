from django.contrib import admin
from django.urls import path
from matematika.views import matematika, sejarah, ilmuwan, peluang, biografi


urlpatterns = [
    path('admin/', admin.site.urls),
    path('matematika/', matematika),
    path('sejarah/', sejarah),
    path('ilmuwan/', ilmuwan),
    path('peluang/', peluang),
    path('biografi/', biografi),
]
