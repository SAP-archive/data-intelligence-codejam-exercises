##Connect Tessel2 to Wi-Fi
```sh
t2 wifi -n <network-name> -p <password>
```

##Run script
```javascript
// Code by Michał Korzeń && Vitaliy Rudnytskiy
var mqtt = require('mqtt'),
    client = mqtt.connect('mqtt://mqtt.eclipse.org?clientId=pcjdhw00'),
    tessel = require('tessel'),
    climate = require('climate-si7020').use(tessel.port['A']);

climate.on('ready', function ready() {
  console.log('climate ready');
  // We will set an interval of 5 seconds to make sure we don't use up all of Tessel's 4 sockets
  setInterval(function() {
    // Read the temperature
    climate.readTemperature(function(err, temperature) {
      // If there was no error
      if (!err) {
        console.log('publishing temp', temperature);
        // Publish the string representation of the temperature
        client.publish('codejam/location/warmup/temperature', temperature.toString());
      }
    });
  }, 5000);
});
```

```sh
t2 run mqtt_publish.js
```

Currently code is in the `C:\Users\i076835\OneDrive - SAP SE\Projects\nodecode\t2_climate_iotneo_mqtt\`
