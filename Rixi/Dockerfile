FROM ubuntu:20.04
ENTRYPOINT []
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa==2.4.1 && python -m spacy download en_core_web_md 
ADD . /app/
RUN chmod +x /app/start_services.sh
CMD /app/start_services.sh
