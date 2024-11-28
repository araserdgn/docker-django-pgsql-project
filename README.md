# docker-django-pgsql-project
proje_adi/
├── docker-compose.yml        # Docker yapılandırma dosyası
├── myapp/                    # Django uygulaması
│   ├── management/           # Özel yönetim komutları
│   ├── models/               # Django modelleri
│   ├── serializers/          # Django Rest Framework serializer'ları
│   ├── views/                # Django Rest Framework viewset'leri
│   ├── migrations/           # Veritabanı migrasyon dosyaları
│   └── urls.py               # URL yönlendirmeleri
├── Dockerfile                # Docker yapılandırma dosyası
└── requirements.txt          # Proje bağımlılıkları
