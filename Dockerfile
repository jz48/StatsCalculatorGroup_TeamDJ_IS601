FROM python:3

ADD src /src

RUN pip install statistics scipy

CMD [ "python", "./src/PopSampleTest.py"]

