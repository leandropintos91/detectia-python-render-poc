FROM python:3.8-slim

RUN pip install Flask

COPY app.py /app.py

# Expose the port that your Flask app will bind to
EXPOSE 5000

CMD ["python", "app.py"]
