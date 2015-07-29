FROM ubuntu:14.04
# MAINTAINER Avi "avi@shippable.com"

ENV DEBIAN_FRONTEND noninteractive
RUN dpkg-divert --local --rename --add /sbin/initctl && \
    locale-gen en_US en_US.UTF-8 && \
    dpkg-reconfigure locales

# force all apt-get commands with a yes
ADD 90forceyes /etc/apt/apt.conf.d/

# echo "================= Installing core binaries ==================="
RUN apt-get update  && \
     apt-get install -yy python-dev software-properties-common  && \
     add-apt-repository -y ppa:ubuntu-toolchain-r/test  && \
     apt-get update && \
     echo "deb http://archive.ubuntu.com/ubuntu trusty main universe restricted multiverse" > /etc/apt/sources.list  && \
     apt-get install -yy g++-4.9 \
                    wget \
                    texinfo \
                    sudo \
                    git-core \
                    python-pip

# echo "================== Installing python requirements ====="
RUN mkdir -p /home/shippable
ADD . /home/shippable/demobase
RUN pip install -r /home/shippable/demobase/requirements.txt
# echo "================= Installing Node ==================="
RUN add-apt-repository ppa:chris-lea/node.js
RUN apt-get update
RUN apt-get install -y nodejs
RUN cd /home/shippable/demobase
RUN npm install -g \
  grunt \
  grunt-cli \
  body-parser@~1.12.0 \
  cookie-parser@~1.3.4 \
  cors@>2.7.1 \
  debug@~2.1.1 \
  express@~4.12.2 \
  express-session@>1.11.2 \
  method-override@>2.3.3 \
  morgan@~1.5.1 \
  request@~2.55.0 \
  sync-request@2.0.1 \
  winston@>1.0.1
# echo "================== Adding empty known hosts file =============="
RUN mkdir -p /root/.ssh
RUN touch /root/.ssh/known_hosts

# echo "================== Disabling scrict host checking for ssh ====="
ADD config /root/.ssh/config

# echo "================= Adding gclould binaries ============"
RUN mkdir -p /opt/gcloud
ADD google-cloud-sdk /opt/gcloud/google-cloud-sdk
RUN cd /opt/gcloud/google-cloud-sdk && ./install.sh --usage-reporting=false --bash-completion=true --path-update=true
ENV PATH $PATH:/opt/gcloud/google-cloud-sdk/bin
RUN gcloud components update preview

RUN echo 'ALL ALL=(ALL) NOPASSWD:ALL' | tee -a /etc/sudoers
