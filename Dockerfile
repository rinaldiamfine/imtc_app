FROM odoo@sha256:ed8f7b440bd5b5b7b19efb639f3a3a2d733bf213e7529b7999231111b38b3f53

USER root
RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        python3-setuptools \
        groff \
        less \
    && pip3 install --upgrade pip \
    && apt-get clean

RUN pip3 install numpy==1.21.1
RUN pip3 install xlsxwriter
RUN pip3 install pandas==1.3.0
RUN pip3 install boto3
RUN pip3 --no-cache-dir install --upgrade awscli

USER odoo

COPY . /mnt/extra-addons