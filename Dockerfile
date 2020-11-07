FROM python:3

ADD src /src

RUN pip install statistics scipy

ENTRYPOINT ['./run_tests.sh']

