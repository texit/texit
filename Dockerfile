FROM python:2-onbuild
MAINTAINER Zach Latta <zach@zachlatta.com>

RUN apt-get update
RUN apt-get install -y texlive
RUN apt-get install -y texlive-latex-extra
RUN apt-get install -y pdf2svg

CMD [ "gunicorn", "texit:app", "--log-file=-" ]
