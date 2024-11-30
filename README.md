
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

<p>Redis Test</p>
<p>terminale docker exec -it djangodockertest-web-1 python manage.py shell diyoruz. Açılan terminale aşağıdaki kodları yapıştırıyoruz</p>
<p>from myapp.models import Todo <br>
  todo = Todo.objects.get(id={todo_id}) 
  print(todo.title)
  print(todo.completed)
  print(todo.user.id)

</p>
