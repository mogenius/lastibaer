import os
import time
import random
import subprocess
from threading import Thread

# Get environment variables
traffic_rate = int(os.getenv('TRAFFIC_RATE', 100))  # Number of requests per minute
cpu_load = int(os.getenv('CPU_LOAD', 50))  # CPU load percentage
ram_load = int(os.getenv('RAM_LOAD', 500))  # RAM load in MB
interval_minutes = int(os.getenv('INTERVAL_MINUTES', 1))  # Interval in minutes
download_size_limit = os.getenv('DOWNLOAD_SIZE_LIMIT', '2m')  # Download size limit

def generate_traffic(rate, size_limit):
    while True:
        print(f"Generating traffic at rate of {rate} requests per minute with download size limit {size_limit}...")
        for _ in range(rate):
            subprocess.run(["wget", "-q", "-m", "--limit-rate", size_limit, "-P", "/dev/null", "http://mogenius.com"])
        time.sleep(60)

def generate_cpu_load(load):
    while True:
        load_value = random.uniform(0, load)
        print(f"Generating CPU load at {load_value}%...")
        subprocess.run(["stress-ng", "--cpu", "1", "--cpu-load", str(load_value), "--timeout", "60s"])
        time.sleep(60)

def generate_ram_load(load):
    while True:
        load_value = random.uniform(0, load)
        print(f"Generating RAM load of {int(load_value)} MB...")
        subprocess.run(["stress-ng", "--vm", "1", "--vm-bytes", f"{int(load_value)}M", "--vm-keep", "--timeout", "60s"])
        time.sleep(60)

# Create threads for generating traffic, CPU, and RAM load
traffic_thread = Thread(target=generate_traffic, args=(traffic_rate, download_size_limit))
cpu_thread = Thread(target=generate_cpu_load, args=(cpu_load,))
ram_thread = Thread(target=generate_ram_load, args=(ram_load,))

# Start the threads
traffic_thread.start()
cpu_thread.start()
ram_thread.start()

# Change load periodically within the specified interval
while True:
    traffic_rate = random.randint(0, traffic_rate)
    cpu_load = random.randint(0, cpu_load)
    ram_load = random.randint(0, ram_load)
    print(f"Changing load: traffic_rate={traffic_rate}, cpu_load={cpu_load}%, ram_load={ram_load}MB")
    time.sleep(interval_minutes * 60)
