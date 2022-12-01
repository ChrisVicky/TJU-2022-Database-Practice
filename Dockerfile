FROM python:3.10
WORKDIR /project/demo
COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["python3","app.py"]
