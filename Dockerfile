FROM python:3

ADD src /src

RUN pip install coverage pytest Statistics

CMD [ "python", "./src/PopSampleTest.py"]

