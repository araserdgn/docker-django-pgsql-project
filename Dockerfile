# Python 3.10 slim imajını kullanıyoruz
FROM python:3.10-slim

# Çalışma dizinini /app olarak ayarlıyoruz
WORKDIR /app

# Sistem bağımlılıklarını yüklüyoruz (PostgreSQL için gerekli)
RUN apt-get update && apt-get install -y libpq-dev

# requirements.txt dosyasını konteynıra kopyalıyoruz
COPY requirements.txt .

# Bağımlılıkları yüklüyoruz
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyalıyoruz
COPY . .

# Django sunucusunu başlat
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
