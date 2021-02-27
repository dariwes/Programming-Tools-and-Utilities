FROM python:3.8

RUN mkdir -p /lab1/
WORKDIR /lab1/

COPY  . /lab1/
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "dir_tree.py" ]