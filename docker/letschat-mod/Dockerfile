FROM sdelements/lets-chat
MAINTAINER Hussein Galal
USER root
RUN set -x \
&& apt-get update \
&& apt-get install -yqq python python-pip python-setuptools 

ENV MONGO_SERVICE_NAME=mongo
ADD mongoseed.sh mongoseed.sh
ADD api_rancher.py api_rancher.py
RUN chmod a+x mongoseed.sh

USER node

CMD ["./mongoseed.sh"]

