from django.urls import path, include
from news.views import about, scrape, news_list, home, about
urlpatterns = [
  path('scrape/<str:name>', scrape, name="scrape"),
  path('news', news_list, name="home"),
  path('', home),
  path('about', about),
 
]