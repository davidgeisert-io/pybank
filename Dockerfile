FROM python:3.8

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python manage.py migrate

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]