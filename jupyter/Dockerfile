FROM jupyter/pyspark-notebook:latest

# add needed packages
# RUN apt-get update && apt-get install 

# Install Python requirements
COPY requirements.txt /home/jovyan/requirements.txt 
RUN pip3 install -r /home/jovyan/requirements.txt

#COPY jupyter_lab_config.json /home/jovyan/




