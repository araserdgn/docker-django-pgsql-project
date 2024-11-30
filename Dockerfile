# Python 3.10 slim imajını kullanıyoruz
FROM python:3.10-slim

# Çalışma dizinini /app olarak ayarlıyoruz
WORKDIR /app

# Gerekli sistem bağımlılıklarını yüklüyoruz
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt dosyasını kopyalıyoruz
COPY requirements.txt ./

# pip ve setuptools'u güncelliyoruz
RUN python -m pip install --upgrade pip setuptools \
    && pip install --default-timeout=300 --no-cache-dir -r requirements.txt


# Proje dosyalarını kopyalıyoruz
COPY . .

# Django sunucusunu başlatıyoruz
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]