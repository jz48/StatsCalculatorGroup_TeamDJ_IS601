FROM python:3

ADD src /src

RUN pip install statistics scipy

CMD sh ./src/run_tests.sh

