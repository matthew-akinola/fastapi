# The image you are going to inherit your Dockerfile from
FROM python:3.9-alpine

# Set the /django_blog directory as the working directory
WORKDIR /app

RUN addgroup system_user_group && adduser -D -G system_user_group developer
RUN chmod g+x /app

# Create a user that can run your container
USER developer

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Copy the requirements.txt file adjacent to the Dockerfile
COPY ./requirements.txt requirements.txt
# Install the requirements.txt file in Docker image
RUN pip install -r requirements.txt

ENV DEBUG=${DEBUG}
ENV SERVICE_2_URL=${SERVICE_2_URL}
ENV SERVICE_ACCOUNT_FILE=${SERVICE_ACCOUNT_FILE}

# copy the Fastapi project into the container image
COPY . .

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0:8001"]

