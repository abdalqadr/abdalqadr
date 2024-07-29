ROM python:3.8

RUN git clone https://github.com/A-SC/A.git /root/A

WORKDIR /root/A

RUN apt update && apt install -y pyqt5-dev-tools python3-pyqt5

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/A/bin:$PATH"

CMD ["python3","-m","A"]
