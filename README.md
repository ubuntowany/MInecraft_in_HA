# Minecraft_in_HA
<h1>Integracja Serwera Minecraft z Home Assistant</h1>
<h2>1. Wprowadzenie</h2>
   Ten tutorial pokaże, jak zintegrować serwer Minecraft z Home Assistant, umożliwiając sterowanie serwerem z poziomu panelu HA. Wykorzystamy MQTT do komunikacji oraz skrypty Bash i Python do zarządzania serwerem.
<h2>2. Kroki do Wykonania</h2>
<h3>2.1. Konfiguracja Skryptu Python</h3>
     Utwórz skrypt Python o nazwie mqtt_minecraft_launcher.py do nasłuchiwania wiadomości MQTT i zarządzania serwerem  Minecraft.
<h3>2.2. Skrypty Bash do Zarządzania Serwerem</h3>
<h4>2.2.1 Skrypt uruchamiający serwer (start_minecraft.sh)</h4>
<h4>2.2.2 Skrypt zatrzymujący serwer (stop_minecraft.sh)</h4>
<h4>2.2.3 Upewnij się, że oba skrypty mają prawa wykonania:</h4>

  chmod +x /ścieżka/do/start_minecraft.sh <br>
  chmod +x /ścieżka/do/stop_minecraft.sh </br>
  <h3>2.3 Konfiguracja Usługi Systemd</h3>
  
