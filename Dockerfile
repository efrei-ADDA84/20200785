FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install requests
RUN pip install Flask
RUN pip install prometheus_client
CMD ["python", "main.py"]