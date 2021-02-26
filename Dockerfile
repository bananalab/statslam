FROM python:3.8
COPY . /statslam
WORKDIR /statslam
RUN pip install pipenv &&\
    pipenv install --deploy --ignore-pipfile
ENTRYPOINT [ "pipenv", "run", "statslam" ]