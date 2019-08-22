FROM python:3.6-alpine
LABEL maintainer "Ahmet TURGUT <ahmetturgut141997@gmail.com>"
COPY . /app
WORKDIR ./
RUN \
 apk add --no-cache bash && \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["/bin/bash" , "./boot.sh"]


