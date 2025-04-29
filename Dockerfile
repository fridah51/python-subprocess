FROM tiangolo/uwsgi-nginx-flask:python3.8

# Install nsenter via util-linux
RUN apt-get update && apt-get install -y util-linux

# copy over our requirements.txt file
COPY requirements.txt /tmp/

# upgrade pip and install required python packages
RUN pip install -U pip

RUN pip install -r /tmp/requirements.txt

# copy over our app code
COPY ./ /app

EXPOSE 80