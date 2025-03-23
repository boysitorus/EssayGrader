# Gunakan image Python yang ringan
FROM python:3.9-slim

# Set direktori kerja
WORKDIR /app

# Salin file requirements dan aplikasi ke dalam container
COPY requirements.txt .
COPY app.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8081
EXPOSE 8081

# Jalankan aplikasi dengan Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8081"]
