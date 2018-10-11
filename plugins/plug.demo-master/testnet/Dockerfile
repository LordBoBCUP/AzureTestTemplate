FROM plugdevelopers/plug:0.0.24
LABEL author Daniel Edgecombe <edgy@qad.re>

ARG password

RUN pip install plug_top==0.0.4 -i http://plug:$password@pypi.qad.re/simple --trusted-host=pypi.qad.re

COPY . /app

RUN pip install /app && \
    rm -rf /app
