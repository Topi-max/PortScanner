import socket
import threading

# Funktio, joka tarkistaa, onko portti auki
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Portti {port} on AUKI")
        s.close()
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

# Käynnistetään säikeet nopeuttamaan skannausta
threads = []
for port in ports:
    thread = threading.Thread(target=scan_port, args=(target, port))
    threads.append(thread)
    thread.start()

# Odotetaan kaikkien säikeiden valmistumista
for thread in threads:
    thread.join()

print("\nSkannaus valmis!")
