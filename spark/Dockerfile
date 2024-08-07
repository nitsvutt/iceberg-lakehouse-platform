ARG JDK_VERSION=11.0.16-jre-slim-buster
ARG PYTHON_VERSION=3.10.4

FROM openjdk:$JDK_VERSION

# install base packages
RUN apt-get update
RUN apt-get install build-essential \
                    zlib1g-dev \
                    libncurses5-dev \
                    libgdbm-dev \
                    libnss3-dev \
                    libssl-dev \
                    libreadline-dev \
                    libffi-dev \
                    libsqlite3-dev \
                    wget \
                    libbz2-dev \
                    procps \
                    software-properties-common \
                    libpq-dev \
                    ca-certificates -y
RUN rm -rf /var/lib/apt/lists/*

# download python
ARG PYTHON_VERSION
RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz
RUN mkdir -p /opt/python
RUN tar -xf Python-${PYTHON_VERSION}.tgz -C /opt/python --strip-components=1
RUN rm -rf Python-${PYTHON_VERSION}.tgz

# intsall python
WORKDIR /opt/python
RUN ./configure --enable-optimizations
RUN make -j $(nproc)
RUN make altinstall
RUN update-alternatives --install /usr/bin/python python /usr/local/bin/python3.10 1

# download and install pip
RUN curl https://bootstrap.pypa.io/get-pip.py | python
RUN update-alternatives --install /usr/bin/pip pip /usr/local/bin/pip3.10 1

# download spark
ENV SPARK_VERSION=3.4.1
ENV HADOOP_VERSION=3
RUN wget -O apache-spark.tgz https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
RUN mkdir -p /opt/spark
RUN tar -xf apache-spark.tgz -C /opt/spark --strip-components=1
RUN rm -rf apache-spark.tgz

# configure spark
WORKDIR /opt/spark
ENV SPARK_HOME=/opt/spark
ENV PATH=${SPARK_HOME}/bin:${PATH}
ENV PYSPARK_PYTHON=/usr/bin/python
ENV PYSPARK_DRIVER_PYTHON=/usr/bin/python
ENV SPARK_MASTER_PORT=7077
ENV SPARK_MASTER_WEBUI_PORT=8080
ENV SPARK_MASTER_URL=spark://spark-master:7077
ENV SPARK_LOG_DIR=/opt/spark/logs
ENV SPARK_MASTER_LOG=/opt/spark/logs/spark-master.out
ENV SPARK_WORKER_LOG=/opt/spark/logs/spark-worker.out
ENV SPARK_HISTORY_LOG=/opt/spark/logs/spark-history.out
ENV SPARK_CONNECT_LOG=/opt/spark/logs/spark-connect.out
ENV SPARK_WORKER_WEBUI_PORT=8081
ENV SPARK_MODE=master
RUN mkdir -p ${SPARK_LOG_DIR}
RUN touch ${SPARK_MASTER_LOG}
RUN touch ${SPARK_WORKER_LOG}
RUN touch ${SPARK_HISTORY_LOG}
RUN touch ${SPARK_CONNECT_LOG}
RUN ln -sf /dev/stdout ${SPARK_MASTER_LOG}
RUN ln -sf /dev/stdout ${SPARK_WORKER_LOG}
RUN ln -sf /dev/stdout ${SPARK_HISTORY_LOG}
RUN ln -sf /dev/stdout ${SPARK_CONNECT_LOG}
RUN mkdir /opt/spark/event

# install pyspark dependencies
COPY ./requirements.txt $SPARK_HOME/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r $SPARK_HOME/requirements.txt

# copy config file and start file from host
COPY spark-defaults.conf $SPARK_HOME/conf/
COPY ./start-spark.sh $SPARK_HOME

CMD ["/bin/bash", "/opt/spark/start-spark.sh"]