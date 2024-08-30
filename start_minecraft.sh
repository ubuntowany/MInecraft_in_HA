#!/bin/bash
cd /ścieżka/do/katalogu/minecraft/
screen -dmS "Minecraft Server Screen" sudo java -Xmx1024M -Xms1024M -jar server.jar nogui
