# Use an official Python 3.6 image as a parent image
FROM python3.6.4-stretch

# Install python library psutil
RUN apt-get update 
    && apt-get upgrade -y 
    && apt-get install -y gcc python3-dev
RUN pip3 install psutil