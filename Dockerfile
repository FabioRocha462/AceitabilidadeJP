FROM python

COPY account/ /app/
COPY aceitabilidade /app/
COPY Myapp /app/
COPY static/ /app/
COPY templates/ /app/
COPY users /app/
COPY .gitignore /app/
COPY db.sqlite3 /app/
COPY manage.py/ /app
COPY requirements.txt /app/ 

RUN (cd /app/ && pip install -r requirements.txt)
# RUN (cd /app/ && pip install requests)

ENV PYTHONUMBUFFERED = 1


CMD python /app/manage.py runserver 0.0.0.0:8000