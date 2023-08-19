FROM python:3.10
WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN alembic upgrade head
RUN chmod 755 .
COPY . .
