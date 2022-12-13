FROM prefecthq/prefect:2.7.1-python3.11

RUN apt-get update
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Zurich
RUN apt-get install -y wget tzdata

WORKDIR /root

# copy content from local repo
COPY . .

# install relevant packages
RUN python -m pip install -r requirements.txt

ENTRYPOINT [ "bash" ]