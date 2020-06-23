# developed from tutorial: https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application

FROM python:3.7-buster

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/cdashboard
COPY requirements.txt /opt/app/
COPY start-managed-server.sh /opt/app/
COPY .pip_cache /opt/app/pip_cache/
COPY cdashboard /opt/app/cdashboard/
WORKDIR /opt/app
RUN git clone https://github.com/mwsu-csmp/curriculum.git
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN pip install ./curriculum --cache-dir /opt/app/pip_cache
WORKDIR /opt/app
RUN chown -R www-data:www-data /opt/app

# start server
EXPOSE 80
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-managed-server.sh"]
