FROM python:3.9
WORKDIR /sk
COPY ./ ./
RUN pip install -r requirements.txt
EXPOSE 8001
CMD ["python3","app.py"]