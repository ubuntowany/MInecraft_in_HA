#!/bin/bash
echo "Zatrzymywanie serwera Minecraft..."
screen -S "Minecraft Server Screen" -p 0 -X stuff "stop\n"
