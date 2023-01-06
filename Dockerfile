FROM python:3.10.0-slim
RUN pip install passlib
RUN pip install argon2_cffi
RUN pip install "passlib[bcrypt,argon2]"
RUN pip install "python-jose[cryptography]"
RUN pip install python-multipart
WORKDIR /code
EXPOSE 8000
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./myproject /code
RUN mkdir -p /code/sqlitedb
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
