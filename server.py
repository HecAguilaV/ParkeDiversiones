import http.server
import socketserver
import json
import subprocess
import os
import re

# SEGURIDAD: Escuchar solo en localhost (127.0.0.1) para evitar acceso externo
PORT = 8080
HOST = "127.0.0.1"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/stats':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            try:
                # Memoria avanzada en macOS
                mem_cmd = "top -l 1 -n 0 | grep PhysMem"
                mem_output = subprocess.check_output(mem_cmd, shell=True).decode()
                unused = re.search(r'(\d+[MG]) unused', mem_output)
                used = re.search(r'(\d+[MG]) used', mem_output)
                
                # CPU
                cpu_cmd = "top -l 1 -n 0 | grep 'CPU usage'"
                cpu_output = subprocess.check_output(cpu_cmd, shell=True).decode()
                cpu_match = re.search(r'(\d+\.\d+)% user', cpu_output)
                cpu_val = float(cpu_match.group(1)) if cpu_match else 0.0

                # SSD (Disco Principal)
                ssd_cmd = "df -h / | tail -1"
                ssd_output = subprocess.check_output(ssd_cmd, shell=True).decode().split()
                ssd_total = ssd_output[1]
                ssd_free = ssd_output[3]
                ssd_percent = ssd_output[4].replace('%', '')

                # SWAP
                swap_cmd = "sysctl vm.swapusage"
                swap_output = subprocess.check_output(swap_cmd, shell=True).decode()
                swap_total = re.search(r'total = (\d+\.\d+M)', swap_output)
                swap_used = re.search(r'used = (\d+\.\d+M)', swap_output)
                swap_total_val = float(swap_total.group(1)[:-1]) if swap_total else 1.0
                swap_used_val = float(swap_used.group(1)[:-1]) if swap_used else 0.0
                swap_percent = (swap_used_val / swap_total_val) * 100

                # Temperatura Estimada
                temp_val = 38 + (cpu_val * 0.45)
                
                stats = {
                    "used_mem": used.group(1) if used else "0G",
                    "free_mem": unused.group(1) if unused else "0G",
                    "cpu_usage": cpu_val,
                    "ssd_free": ssd_free,
                    "ssd_total": ssd_total,
                    "ssd_usage": ssd_percent,
                    "swap_used": swap_used.group(1) if swap_used else "0M",
                    "swap_total": swap_total.group(1) if swap_total else "0M",
                    "swap_usage": swap_percent,
                    "temp": round(temp_val, 1),
                    "status": "HOT" if temp_val > 65 else ("STABLE" if temp_val > 45 else "COOL")
                }
            except Exception as e:
                stats = {"used_mem": "Err", "free_mem": "Err", "cpu_usage": 0, "status": "OFFLINE"}
                
            self.wfile.write(json.dumps(stats).encode())
        else:
            super().do_GET()

# Detectar la carpeta donde está el script para servir archivos desde ahí
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer((HOST, PORT), MyHandler) as httpd:
    print(f"🚀 SymbiOSis Engine activo en {HOST}:{PORT}")
    print(f"📁 Sirviendo archivos desde: {BASE_DIR}")
    httpd.serve_forever()
