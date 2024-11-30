
<b>Kurulacaklar</b> 
<hr>
<p>1- docker-compose up --build </p>
<p>2- docker exec -it docker-django-pgsql-project-web-1 python manage.py migrate</p>
<p>3- docker exec -it docker-django-pgsql-project-web-1 python manage.py createsuperuser</p>
<p>**Database'ye fake veriler oluşturalım**</p>
<p>4- docker exec -it docker-django-pgsql-project-web-1 python manage.py seed</p>
<p>**Endpoint testlerinin çalıştırılması**</p>
<p>5- docker exec -it docker-django-pgsql-project-web-1 python manage.py test myapp.tests</p>
<hr>
<p>Redis cache mekanizmasının test edilmesi</p>
<p>terminale "docker exec -it docker-django-pgsql-project-web-1 python manage.py shell" kodunu yazıyoruz. Açılan terminale aşağıdaki kodları sırasıyla yapıştırıyoruz</p>
<p>from myapp.models import Todo</p> 
<p>todo = Todo.objects.get(id={todo_id}) </p>
<p>todo = Todo.objects.get(id={todo_id})</p>
<p> print(todo.title)</p>
<p>print(todo.completed)</p>
<p>print(todo.user)</p>
   






