# import requests # http://docs.python-requests.org/en/master/
import psutil   # https://pypi.python.org/pypi/psutil
import time
import uuid
import json
# import sys, platform # if need to read system params, like OS type

def readCPU():
    return psutil.cpu_percent(percpu=False, interval=1)
	
def readMEM():
    return psutil.virtual_memory().percent

def readPayload():

	d_pctCPU = readCPU()
	d_pctMEM = readMEM()
	d_tstamp = int(round(time.time()))
	api.logger.debug("\nValues to post: {} {}".format(d_pctCPU, d_tstamp))

	payload = { 'guid' : deviceUIID, 'timestmp' : d_tstamp, 'cpu_load' : d_pctCPU, 'mem_load' : d_pctMEM }
	# api.logger.debug("\nPayload: ", str(payload))

	return json.dumps(payload)

def do_tick():
    api.send("payload", readPayload())


global deviceUIID 
deviceUIID = str(uuid.uuid1())

intervalMs = int(api.config.intervalMs)
if intervalMs < 1001:
    intervalMs = 1001
    
api.add_timer(str(intervalMs-1000)+"ms", do_tick)