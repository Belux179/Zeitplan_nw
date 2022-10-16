FROM python

ENV PYTHONUNBUFFERED 1

ADD requirements.txt .

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install --upgrade setuptools 

RUN pip install -r requirements.txt


ADD . /my_app_dir/.

WORKDIR /my_app_dir
