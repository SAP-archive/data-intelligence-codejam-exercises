import time
import locale
import json
#import ast

# Number of max devices
max_devices_qty = 100

locale.setlocale(locale.LC_ALL,"")

def main(payload):
    last_timestamp = int(round(time.time()))
    ubody = payload.body.decode("utf-8") # Must be converted to Unicode first
    
    #body = ast.literal_eval(ubody) #ast.literal_eval works only with strings, but can be improperly formatted JSON, like a result of str(json_object)
    
    body=json.loads(ubody)
    body['loc_timestmp'] = last_timestamp
    send_blob(json.dumps([body]))
    
    guid = body["guid"]
    del body["guid"]
    devices[guid] = body
    
    message = ""
    message = generate_html_head(message)
    message = generate_html_body(message, last_timestamp)
    send_html(message)

# Generates head of HTML/CSS, including Style parameters
def generate_html_head(message):
    message += '''

<head>
<style>
body {
    font-family: Verdana, Geneva, sans-serif;
    background: #b5b5bf;
}
table.dataTable {
  border: 1px solid #1C6EA4;
  background-color: #EEEEEE;
  text-align: center;
  border-collapse: collapse;
}
table.dataTable td, table.dataTable th {
  border: 2px solid #AAAAAA;
  padding: 3px 2px;
}
table.dataTable tbody td {
  font-size: 15px;
}
table.dataTable thead {
  background: #1C6EA4;
  background: -moz-linear-gradient(top, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
  background: -webkit-linear-gradient(top, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
  background: linear-gradient(to bottom, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
  border-bottom: 2px solid #888888;
}
table.dataTable thead th {
  font-size: 15px;
  font-weight: bold;
  color: #FFFFFF;
  text-align: center;
  border-left: 2px solid #D0E4F5;
}
table.dataTable thead th:first-child {
  border-left: none;
}

table.dataTable tfoot td {
  font-size: 14px;
}
table.dataTable tfoot .links {
  text-align: right;
}
table.dataTable tfoot .links a{
  display: inline-block;
  background: #1C6EA4;
  color: #FFFFFF;
  padding: 2px 8px;
  border-radius: 5px;
}
</style>
</head>
    '''
    return message

# Concatenates HTML body to previously generated head.
def generate_html_body(message, last_timestamp):
    # Title, description and table header
    message += '''

<body>
<center>

<h2> Prototype IoT Data Viewer </h2>
<br>
</center>
<p style="margin-left:15%; margin-right:15%"> The purpose of this Graph is to serve as a stub for the HTML Viewer operator. 
Combining the HTML Viewer with a Python Operator, it is possible to adapt IoT data for real time display in a simple and flexible manner.

<br><br>
The data structure generation is happening in the Python3 Operator, which is messaging a String containing an HTML page to the HTML Viewer 
through WebSocket with every update. The HTML Viewer then updates the display as soon as a message is received.
<br><br>
</p>

<center>
Last time stamp: {}
<br><br>


<table class="dataTable" id="salesTable">
<thead>
<tr>
<th style="width:400px"> Device UUID </th>
<th style="width:300px"> Last timestamp </th>
<th style="width:100px"> CPU % </th>
<th style="width:100px"> Mem % </th>
</tr>
</thead>
<tbody>
    '''.format(time.ctime(round(time.time())))

    # Iterates each store to add them to table
    for i in devices:
        message += '''
<tr>
<td> {} </td>
<td> {} </td>
<td> {} %</td>
<td> {} %</td> 
</tr>
    '''.format(
        i, 
        time.ctime(int(devices[i]["timestmp"])),
        locale.format("%.2f", devices[i]["cpu_load"], 1),
        locale.format("%.2f", devices[i]["mem_load"], 1)
        )

    message += '''
</tbody>
</table>
<br><br>
</center>
</body>
    '''
    return message

# Sends the String containing HTML page through WebSocket
def send_html(message):
    api.send("outhtml", message)

# Sends the String containing HTML page through WebSocket
def send_blob(blb):
    api.send("outblob", blb)

api.send("outhtml", "Waiting for data...")
devices = {} #Empty dictionary

api.set_port_callback("inmsg", main)