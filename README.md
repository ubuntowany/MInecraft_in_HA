# Minecraft_in_HA
<h1>Integration of Minecraft Server with Home Assistant</h1>
<h2>1. Introduction</h2>
   This tutorial will show you how to integrate a Minecraft server with Home Assistant, enabling server management from the HA panel. We will use MQTT for communication and Bash and Python scripts for server management.
<h2>2. Steps to Follow</h2>
<h3>2.1. Configuring the Python Script</h3>
     Create a Python script named <code>mqtt_minecraft_launcher.py</code> to listen for MQTT messages and manage the Minecraft server.
<h3>2.2. Bash Scripts for Server Management</h3>
<h4>2.2.1 Server Startup Script (<code>start_minecraft.sh</code>)</h4>
<h4>2.2.2 Server Shutdown Script (<code>stop_minecraft.sh</code>)</h4>
<h4>2.2.3 Make sure both scripts have execution permissions:</h4>

  <code>chmod +x /path/to/start_minecraft.sh</code> <br>
  <code>chmod +x /path/to/stop_minecraft.sh</code> </br>
  
<h3>2.3 Configuring the Systemd Service</h3>
<h4>2.3.1 Create a bash script (<code>start_mqtt_listener.sh</code>) that will wait for the availability of the MQTT port</h4>
<h4>2.3.2 Grant execution permissions:</h4><br>
<code>chmod +x /path/to/start_mqtt_listener.sh</code> </br>
<h4>2.3.3 Create the <code>mqtt_listener.service</code> file in <code>/etc/systemd/system/</code></h4>
<h4>2.3.4 Load the new systemd services and start the service:</h4> <br>
<code>sudo systemctl daemon-reload</code><br>
<code>sudo systemctl enable mqtt_listener.service</code><br>
<code>sudo systemctl start mqtt_listener.service</code> </br>
<h3>2.4 Configuring Home Assistant</h3>
<h4>2.4.1 Add startup and shutdown scripts for the Minecraft server in Home Assistant:</h4>
<pre><code>
script:
  start_minecraft_server:
    sequence:
      - service: mqtt.publish
        data:
          topic: "minecraft/start"
          payload: "start"

  stop_minecraft_server:
    sequence:
      - service: mqtt.publish
        data:
          topic: "minecraft/stop"
          payload: "stop"
</code></pre>
<h3>2.4.2 Configure the Interface Panel:</h3>
<pre><code>
type: horizontal-stack
cards:
  - type: conditional
    conditions:
      - entity: binary_sensor.minecraft_server_status
        state: 'on'
    card:
      type: vertical-stack
      cards:
        - type: markdown
          content: |
            Connection Status: <font color='green'><ha-icon icon="mdi:minecraft"></ha-icon></font>

            Players Online: {{states('sensor.minecraft_server_players_online') }}

        - type: button
          name: Stop Server
          tap_action:
            action: call-service
            service: script.turn_on
            service_data:
              entity_id: script.stop_minecraft_server
          icon: mdi:server-off

  - type: conditional
    conditions:
      - entity: binary_sensor.minecraft_server_status
        state_not: 'on'
    card:
      type: vertical-stack
      cards:
        - type: markdown
          content: |
            Connection Status: <font color='red'><ha-icon icon="mdi:minecraft"></ha-icon></font>

        - type: button
          name: Start Server
          tap_action:
            action: call-service
            service: script.turn_on
            service_data:
              entity_id: script.start_minecraft_server
          icon: mdi:server
</code></pre>
