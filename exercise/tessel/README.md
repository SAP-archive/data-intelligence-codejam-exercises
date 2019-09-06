# Hands-on: Warm-up with Tessel IoT data and MQTT



## Prerequisites
You are using SAP Data Hub 2.4, developer edition, and have container `datahub` running. You can check it by executing
```sh
docker ps -f name=datahub
```

## Create a new graph with Terminal only
In SAP Data Hub Modeller go to **Graphs** tab. Create a new graph.

Save the graph with parameters.

|Field|Value|
|-|-|
|Name|`codejam.warmup.mqtttcp.tessel`|
|Description|`MQTT-TCP-based IoT data wiretap`|
|Category|`CodeJam` (type it if not yet existing)|

Click on **Show Configuration** of the graph. Change the **icon** to a `at`. Save the graph.

You should see an icon of the graph changed in CodeJam category.

## Add MQTT operator
### Add an MQTT Consumer
Add an “MQTT Consumer” operator.

Define parameters of the operator as following.

|Field|Value|
|-|-|
|mqttBroker|`tcp://mqtt.eclipse.org:1883` ~~`tcp://test.mosquitto.org:1883`~~|
|topic|`sapcodejam/+/warmup/#`|
|mqttClientID|`ccjdhw<location><your-user-ID>`|

>For MQTT protocol to work it is extremely important that **each client has a unique ID!**

## Add Wiretap operator
Add an “Wiretap” operator.

Connect `outmessage` out port from "MQTT Consumer" operator to `in` in port of "Wiretap".

### Run the graph
Now you have a graph that can receive data from the MQTT server to display it in its terminal, and to send the data typed in the the terminal to the MQTT server.

![Graph with MQTT operators](images/cjdhchat040.jpg)

Save and run the graph.

Open the wiretap's UI of the running graph and check if IoT data is coming!

## Summary
This is the end of the scenario, where you built a graph to learn about:
1. Creating and running a data pipeline,
2. Wiretap operator.
