import socket
import time
from concurrent.futures import ThreadPoolExecutor

# Funktio, joka tarkistaa, onko portti auki
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)  # Pidennetään timeoutia
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Portti {port} on AUKI")
        s.close()
        time.sleep(0.1)  # Pieni viive palvelimen ylikuormituksen välttämiseksi
    except:
        pass

# Käyttäjän syötteet
target = input("Anna skannattava IP-osoite tai domain: ")

# Kysy, haluaako käyttäjä skannata yleisimmät portit
mode = input("Haluatko skannata yleisimmät portit? (k/e): ").strip().lower()
if mode == 'k':
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995, 3306, 3389]
else:
    port_start = int(input("Anna aloitusportti: "))
    port_end = int(input("Anna lopetusportti: "))
    ports = list(range(port_start, port_end + 1))

print(f"Skannataan {target} {len(ports)} porttia...\n")

# Käytetään säikeitä nopeuttamaan skannausta mutta rajoitetaan määrää
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(lambda port: scan_port(target, port), ports)

print("\nSkannaus valmis!")

