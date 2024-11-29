
<b>Kurulacaklar</b>
<p> docker-commpose pip install django </p>



<b>Fake Data oluştur</b>
<p>docker-compose exec web pip install faker</p>
<p>docker-compose exec web pip freeze > requirements.txt</p>
<p>docker-compose down
docker-compose build
docker-compose up -d</p>
<p>docker-compose run web python manage.py seed</p>


<p> docker-compose run web python manage.py test myapp.tests</p>

<b>Test Dosyası çalıştır</b>
<p> docker-compose run web python manage.py test myapp.tests</p>
