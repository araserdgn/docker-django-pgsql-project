import random
from faker import Faker
from django.core.management.base import BaseCommand
from myapp.models import User, Post, Comment, Album, Photo, Todo

fake = Faker()

class Command(BaseCommand):
    help = "Seed the database with fake data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        # Kullanıcılar oluştur
        for _ in range(10):
            user = User.objects.create(
                name=fake.name(),
                username=fake.user_name(),
                email=fake.email(),
                phone=fake.phone_number(),
                website=fake.domain_name(),
            )

            # Adres ve Şirket Bilgisi Ekle
            user.address.create(
                street=fake.street_name(),
                suite=fake.secondary_address(),
                city=fake.city(),
                zipcode=fake.zipcode(),
                geo_lat=fake.latitude(),
                geo_lng=fake.longitude(),
            )
            user.company.create(
                name=fake.company(),
                catch_phrase=fake.catch_phrase(),
                bs=fake.bs(),
            )

            # Post oluştur
            for _ in range(random.randint(2, 5)):
                post = Post.objects.create(
                    user=user,
                    title=fake.sentence(),
                    body=fake.text(),
                )

                # Yorum ekle
                for _ in range(random.randint(1, 3)):
                    Comment.objects.create(
                        post=post,
                        name=fake.name(),
                        email=fake.email(),
                        body=fake.text(),
                    )

            # Albüm ve Fotoğraf ekle
            for _ in range(random.randint(1, 3)):
                album = Album.objects.create(
                    user=user,
                    title=fake.sentence(),
                )
                for _ in range(random.randint(2, 6)):
                    Photo.objects.create(
                        album=album,
                        title=fake.sentence(),
                        url=fake.image_url(),
                        thumbnail_url=fake.image_url(),
                    )

            # Todo ekle
            for _ in range(random.randint(5, 10)):
                Todo.objects.create(
                    user=user,
                    title=fake.sentence(),
                    completed=fake.boolean(),
                )

        self.stdout.write("Seeding complete.")
