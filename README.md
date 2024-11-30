
<b>Kurulacaklar</b> 
<hr>
<p>1- docker-compose up --build </p>
<p>2- docker exec -it docker-django-pgsql-project-web-1 python manage.py migrate</p>
<p>3- docker exec -it docker-django-pgsql-project-web-1 python manage.py createsuperuser</p>
<p>Database'ye fake veriler oluşturalım:</p>
<p>4- docker exec -it docker-django-pgsql-project-web-1 python manage.py seed</p>
<p>Endpoint testlerinin çalıştırılması</p>
<p>5- docker exec -it docker-django-pgsql-project-web-1 python manage.py test myapp.tests</p>
<hr>
<p>Redis cache mekanizmasının test edilmesi</p>
<p>terminale docker exec -it docker-django-pgsql-project-web-1 python manage.py shell diyoruz. Açılan terminale aşağıdaki kodları yapıştırıyoruz</p>
<p>from myapp.models import Todo <br>
  todo = Todo.objects.get(id={todo_id}) 
  print(todo.title)
  print(todo.completed)
  print(todo.user)
  print(todo.user.id)
</p>




