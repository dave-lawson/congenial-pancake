FROM ubuntu:20.04

RUN apt-get update -y && apt-get install -y python3 python3-pip && apt-get clean -y

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /api/requirements.txt

WORKDIR /api

RUN pip install -r requirements.txt

COPY ./api/api.py /api

CMD [ "/api/api.py" ]

ENTRYPOINT [ "python3" ]
