## Connect Tessel2 to Wi-Fi
```sh
t2 wifi -n <network-name> -p <password>
```

## Run script
```javascript
var mqtt = require('mqtt'),
    client = mqtt.connect("mqtt://mqtt.eclipse.org", { clientId: "pcjdhw0000" }),
    tessel = require('tessel'),
    climate = require('climate-si7020').use(tessel.port['A']);

client.on('connect', function () {
    console.log('Connected to MQTT broker!');
});

climate.on('ready', function ready() {
    console.log('climate ready');
    // We will set an interval of 5 seconds to make sure we don't use up all of Tessel's 4 sockets
    setInterval(function () {
        // Read the temperature
        climate.readTemperature(function (err, temperature) {
            // If there was no error
            if (!err) {
                console.log('read temp ', temperature);
                if (client.connected == true) {
                    // Publish the string representation of the temperature
                    client.publish('sapcodejam/internet/warmup/temperature', temperature.toString(), { qos: 0 }, function (err) {
                        //console.log('Published');
                        if (err) {
                            console.log('Publishing error: ', err);
                        }
                    });
                } else {
                    console.log('Client is not connected...')
                }
            }
        });
    }, 5000);
});

client.on("error", function (error) {
    console.log("Can't connect" + error);
    process.exit(1)
});
```

```sh
t2 run mqtt_publish.js
```

Currently code is in the `C:\Users\i076835\OneDrive - SAP SE\Projects\nodecode\t2_climate_iotneo_mqtt\`
