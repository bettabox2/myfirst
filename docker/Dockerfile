FROM python:3.9-slim
ENV ALLOWED_HOST='http://127.0.0.1'
ENV DEBUG='True'
WORKDIR /django
EXPOSE 8000
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT docker/entrypoint.sh
