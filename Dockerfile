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
                    curl \
                    texinfo \
                    make \
                    openssh-server \
                    openssh-client \
#                    gdb= \
                    sudo \
                    git-core \
                    vim \
                    htop \
                    python-pip
                    python-software-properties && \
                    supervisor 
     wget http://security.ubuntu.com/ubuntu/pool/main/g/gdb/gdb_7.4-2012.02-0ubuntu2_amd64.deb  && \
     dpkg -i ./gdb_7.4-2012.02-0ubuntu2_amd64.deb

# echo "================== Installing python requirements ====="
RUN mkdir -p /home/shippable /src
ADD . /home/shippable/appBase
RUN pip install -r /home/shippable/appBase/requirements.txt  && \
# echo "================= Installing Node ==================="
     add-apt-repository ppa:chris-lea/node.js  && \
     apt-get update  && \
     apt-get install -y nodejs  && \
     cd /home/shippable/appBase && \
     npm install -g && \
# echo "================== Adding empty known hosts file =============="
     mkdir -p /root/.ssh  && \
     touch /root/.ssh/known_hosts

# echo "================== Disabling scrict host checking for ssh ====="
ADD config /root/.ssh/config

# echo "================= Adding gclould binaries ============"
# RUN mkdir -p /opt/gcloud
# ADD google-cloud-sdk /opt/gcloud/google-cloud-sdk
# RUN cd /opt/gcloud/google-cloud-sdk && ./install.sh --usage-reporting=false --bash-completion=true --path-update=true
# ENV PATH $PATH:/opt/gcloud/google-cloud-sdk/bin
# RUN gcloud components update preview

RUN echo 'ALL ALL=(ALL) NOPASSWD:ALL' | tee -a /etc/sudoers
