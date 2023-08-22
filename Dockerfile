FROM python:3
RUN pip install fastapi, uvicorn
ADD main.py /
CMD [ "python", "./main.py" ]