FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PORT=5200
EXPOSE 5200
CMD ["gunicorn", "-b", "0.0.0.0:5200", "app:app"]