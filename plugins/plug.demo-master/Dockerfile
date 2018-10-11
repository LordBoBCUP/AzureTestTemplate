FROM plug
LABEL author David Smith <david@qad.re>
COPY . /app
RUN pip install -e /app
WORKDIR /app/node
ENTRYPOINT [ "plug", "run" ]
