import codecs
import os
import sys
from django.db import DatabaseError
proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "sport_news_service.settings"
import django
django.setup()
from sport_news.parsers_city import *
from sport_news.models import News, City
'''parsers = (
    (sportuspro, 'https://sportus.pro/'),
    (bezformata, 'https://krasnoyarsk.bezformata.com/sport/')
)'''
city = City.objects.filter(slug='krasnoyarsk').first()
news, errors = [], []
n, e = bezformata('https://krasnoyarsk.bezformata.com/sport/')
news += n
errors += e
for new in news:
    v = News(**new, city=city)
    try:
        v.save()
    except DatabaseError:
        pass
# h = codecs.open('tomskrosrab.txt', 'w', 'utf-8')
# h.write(str(jobs)); h.close()