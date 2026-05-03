import http.server
import socketserver
import json
import os
import re
import threading
import pyaudio
import struct
import subprocess
import time

# Configuración de Audio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
audio_level = 0

def audio_capture_thread():
    global audio_level
    p = pyaudio.PyAudio()
    try:
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            if data:
                count = len(data) // 2
                shorts = struct.unpack("%dh" % count, data)
                sum_squares = sum(s**2 for s in shorts)
                audio_level = int((sum_squares / max(1, count))**0.5)
    except Exception as e:
        pass
    finally:
        p.terminate()

threading.Thread(target=audio_capture_thread, daemon=True).start()

stats_cache = {}
last_update = 0
CACHE_TTL = 2

def get_system_stats():
    global stats_cache, last_update
    current_time = time.time()
    if current_time - last_update < CACHE_TTL and stats_cache:
        return stats_cache

    try:
        # MEMORIA (/usr/bin/vm_stat)
        vm_output = subprocess.check_output("/usr/bin/vm_stat", shell=True).decode()
        vm_dict = {}
        for line in vm_output.split('\n'):
            if ':' in line and not line.startswith('Mach'):
                key, val = line.split(':')
                # Limpiar valor (quitar puntos de miles y espacios)
                clean_val = val.strip().replace('.', '').replace(' ', '')
                if clean_val.isdigit():
                    vm_dict[key.strip()] = int(clean_val)
        
        page_size = 4096
        # Cálculo: (Active + Wired + Compressor Occupied)
        used_pages = vm_dict.get('Pages active', 0) + vm_dict.get('Pages wired down', 0) + vm_dict.get('Pages occupied by compressor', 0)
        free_pages = vm_dict.get('Pages free', 0) + vm_dict.get('Pages speculative', 0)
        
        used_mem_gb = used_pages * page_size / (1024**3)
        free_mem_gb = free_pages * page_size / (1024**3)
        
        # CPU
        load1, _, _ = os.getloadavg()
        cpu_count = os.cpu_count() or 1
        cpu_val = min(100.0, (load1 / cpu_count) * 100.0)

        # SSD (/bin/df)
        ssd_output = subprocess.check_output("/bin/df -h / | tail -1", shell=True).decode().split()
        ssd_total = ssd_output[1]
        ssd_free = ssd_output[3]
        ssd_percent = ssd_output[4].replace('%', '')

        # SWAP (/usr/sbin/sysctl)
        swap_output = subprocess.check_output("/usr/sbin/sysctl vm.swapusage", shell=True).decode()
        swap_total_match = re.search(r'total = (\d+\.\d+M)', swap_output)
        swap_used_match = re.search(r'used = (\d+\.\d+M)', swap_output)
        swap_total_str = swap_total_match.group(1) if swap_total_match else "0M"
        swap_used_str = swap_used_match.group(1) if swap_used_match else "0M"
        
        temp_val = 38 + (cpu_val * 0.45)
        
        stats_cache = {
            "used_mem": f"{used_mem_gb:.1f}G",
            "free_mem": f"{free_mem_gb:.1f}G",
            "cpu_usage": round(cpu_val, 1),
            "ssd_free": ssd_free,
            "ssd_total": ssd_total,
            "ssd_usage": ssd_percent,
            "swap_used": swap_used_str,
            "swap_total": swap_total_str,
            "temp": round(temp_val, 1),
            "audio_level": audio_level,
            "status": "HOT" if temp_val > 65 else ("STABLE" if temp_val > 45 else "COOL")
        }
        last_update = current_time
        return stats_cache
    except Exception as e:
        print(f"❌ Error obteniendo stats: {e}")
        return {"used_mem": "Err", "free_mem": "Err", "cpu_usage": 0, "status": "OFFLINE"}

PORT = 8080
HOST = "127.0.0.1"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/stats':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            stats = get_system_stats()
            self.wfile.write(json.dumps(stats).encode())
        else:
            super().do_GET()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer((HOST, PORT), MyHandler) as httpd:
    print(f"🚀 SymbiOSis Engine OPTIMIZADO activo en {HOST}:{PORT}")
    httpd.serve_forever()
