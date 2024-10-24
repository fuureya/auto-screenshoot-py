import os
import time
from datetime import datetime
from PIL import ImageGrab

# Direktori penyimpanan screenshot
output_dir = "/home/kuecoklat/Documents/agil_test/screenshoot/"  # Ganti dengan direktori yang diinginkan

# Buat direktori jika belum ada
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Fungsi untuk mengambil screenshot
def take_screenshot():
    # Ambil waktu saat ini
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Buat nama file berdasarkan waktu
    screenshot_name = f"screenshot_{current_time}.png"
    
    # Tentukan path lengkap untuk menyimpan screenshot
    screenshot_path = os.path.join(output_dir, screenshot_name)
    
    # Ambil screenshot
    screenshot = ImageGrab.grab()
    
    # Simpan screenshot sebagai file PNG
    screenshot.save(screenshot_path)
    
    print(f"Screenshot saved to {screenshot_path}")

# Interval waktu antar screenshot (dalam detik)
interval = 10  # Ubah sesuai kebutuhan

try:
    while True:
        take_screenshot()
        time.sleep(interval)
except KeyboardInterrupt:
    print("Autoscreenshot stopped.")
