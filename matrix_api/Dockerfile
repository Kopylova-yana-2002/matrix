FROM python:3.9
#RUN apt update
# Allows docker to cache installed dependencies between builds
COPY matrix_api/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Mounts the application code to the image
COPY matrix_api app
ADD .env /env_file/.env
WORKDIR /app
RUN python ./manage.py migrate
RUN python ./manage.py collectstatic
#EXPOSE 8000