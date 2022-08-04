FROM python
RUN mkdir /demo
COPY requirements.txt /demo/
ADD ./app /demo/app
COPY config.py /demo/
COPY main.py /demo/
RUN chmod +x /demo/main.py
RUN pip install --upgrade pip
RUN pip install -r /demo/requirements.txt
EXPOSE 8000
WORKDIR /demo/
CMD /demo/main.py