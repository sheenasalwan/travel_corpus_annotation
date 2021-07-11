FROM python:3.8-slim-buster

COPY  src/web_interface/ src/web_interface/

COPY  data/ data/

COPY . .

RUN pip install -r src/web_interface/requirements.txt

CMD ["python","src/web_interface/backend.py"]