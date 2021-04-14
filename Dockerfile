FROM ubuntu:18.04

# Setup timezone info
ENV TZ=UTC

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y software-properties-common

RUN add-apt-repository ppa:ubuntugis/ppa && \
    apt-get update && \
    apt-get install -y build-essential python3-dev python3-numpy \
    wget=1.* git=1:2.* curl nghttp2 libnghttp2-dev  \
    libssl-dev libsqlite3-dev=3.22.* zlib1g-dev=1:1.2.* \
    libhdf4-dev  && \
    apt-get autoremove && apt-get autoclean && apt-get clean

# See https://github.com/mapbox/rasterio/issues/1289
ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

# Install Python 3.8
RUN wget -q -O ~/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh
ENV PATH /opt/conda/bin:$PATH
ENV LD_LIBRARY_PATH /opt/conda/lib/:$LD_LIBRARY_PATH
RUN conda install -y python=3.8
RUN python -m pip install --upgrade pip
RUN conda install -y -c conda-forge gdal=3.2.0

RUN pip install setuptools cython numpy

# Install base packages
RUN mkdir -p /opt/src

COPY requirements.txt /opt/src/requirements.txt
RUN pip install --no-build-isolation -r /opt/src/requirements.txt

# GDAL config to optimize COG reading
ENV GDAL_CACHEMAX 200
ENV GDAL_INGESTED_BYTES_AT_OPEN 16383
ENV GDAL_DISABLE_READDIR_ON_OPEN EMPTY_DIR
ENV GDAL_HTTP_MERGE_CONSECUTIVE_RANGES YES
ENV GDAL_HTTP_MULTIPLEX YES
ENV GDAL_HTTP_VERSION 2
ENV VSI_CACHE TRUE
ENV VSI_CACHE_SIZE 5000000

COPY datasets /opt/src/datasets

WORKDIR /opt/src

EXPOSE 8888

CMD [ "jupyter", "notebook", \
    "--ip", "0.0.0.0", \
    "--port", "8888", \
    "--no-browser", \
    "--allow-root", \
    "--notebook-dir=/opt/src" \
    ]
