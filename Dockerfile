FROM python:3.10
WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN chmod 755 .
RUN alembic upgrade head
COPY . .
