FROM plugdevelopers/plug:0.0.24
LABEL author David Smith <david@qad.re>

ARG password

COPY . /app

RUN mkdir /node
RUN mkdir /plug

COPY ./audit/db.sqlite /node
COPY ./audit/config.yaml /node

RUN pip install -e /app
RUN pip install simple_peer==0.0.1 -i http://plug:$password@pypi.qad.re/simple --trusted-host=pypi.qad.re

EXPOSE 8080
EXPOSE 5555

WORKDIR /node
ENTRYPOINT [ "plug", "run", "-c", "/node/config.yaml"]
