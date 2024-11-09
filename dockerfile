FROM python:3.12.7 AS python-build

COPY /gmt/ /source/gmt/
COPY /requirements.txt /source/requirements.txt

USER root

WORKDIR /source

RUN apt install -y libmariadb-dev
RUN pip install -r requirements.txt


FROM python:3.12.7-slim AS alpine

COPY --from=python-build /source/ /source/
COPY --from=python-build /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=python-build /usr/local/bin/ /usr/local/bin/

WORKDIR /source/gmt

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD python manage.py makemigrations --settings=gmt.settings.prod && \
python manage.py migrate --settings=gmt.settings.prod && \ 
python manage.py runserver 0.0.0.0:8000 --settings=gmt.settings.prod
