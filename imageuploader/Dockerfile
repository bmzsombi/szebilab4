FROM python:3.13-slim

# Állítsd be a munkakönyvtárat
WORKDIR /imageuploader

# Másold a requirements.txt fájlt
COPY requirements.txt .

# Telepítsd a szükséges csomagokat
RUN pip install --no-cache-dir -r requirements.txt

# Másold a Django projekt fájljait
COPY . .

# Állítsd be a környezeti változókat
ENV PYTHONUNBUFFERED 1

# Futass egy parancsot a Django alkalmazás indításához
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]