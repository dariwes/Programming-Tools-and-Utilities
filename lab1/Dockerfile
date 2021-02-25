FROM python:3.8

RUN mkdir -p /Users/supersonic/Documents/ИСП/lr1/
WORKDIR /Users/supersonic/Documents/ИСП/lr1/

COPY . /Users/supersonic/Documents/ИСП/lr1/
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "dir_tree.py" ]