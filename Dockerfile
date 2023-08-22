FROM python:3
RUN pip install fastapi, uvicorn
ADD main.py /
CMD [ "python", "python -m uvicorn ./main:app --reload" ]