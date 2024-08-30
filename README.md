# Minecraft_in_HA
<h1>Integration of Minecraft Server with Home Assistant</h1>
<h2>1. Introduction</h2>
   This tutorial will show you how to integrate a Minecraft server with Home Assistant, enabling server management from the HA panel. We will use MQTT for communication and Bash and Python scripts for server management.
<h2>2. Steps to Follow</h2>
<h3>2.1. Configuring the Python Script</h3>
     Create a Python script named mqtt_minecraft_launcher.py to listen for MQTT messages and manage the Minecraft server.
<h3>2.2. Bash Scripts for Server Management</h3>
<h4>2.2.1 Server Startup Script (start_minecraft.sh)</h4>
<h4>2.2.2 Server Shutdown Script (stop_minecraft.sh)</h4>
<h4>2.2.3 Make sure both scripts have execution permissions:</h4>

  chmod +x /path/to/start_minecraft.sh <br>
  chmod +x /path/to/stop_minecraft.sh </br>
  <h3>2.3 Configuring the Systemd Service</h3>
  <h4>2.3.1 Create a bash script (start_mqtt_listener.sh) that will wait for the availability of the MQTT port</h4>
