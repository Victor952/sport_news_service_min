import codecs
import os
import sys
from django.db import DatabaseError
proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "sport_news_service.settings"
import django
django.setup()
from sport_news.parsers_sport_type import *
from sport_news.parsers_city import *
from sport_news.models import News, City, Sport_type
parsers = (
    (sovsport, 'https://www.sovsport.ru/tennis'),
    (sport24, 'https://sport24.ru/boxing/leagues/boxing')
)
sport_type = Sport_type.objects.filter(slug='boxing').first()
city = City.objects.filter(slug='krasnoyarsk').first()
news, errors = [], []
for func, url in parsers:
    n, e = func(url)
    news += n
    errors += e
for new in news:
    v = News(**new, city=city, sport_type=sport_type)
    try:
        v.save()
    except DatabaseError:
        pass
# h = codecs.open('tomskrosrab.txt', 'w', 'utf-8')
# h.write(str(jobs)); h.close()