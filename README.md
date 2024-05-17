# Build
```bash
docker buildx create --name mybuilder --use                                                                                                                                                                                ✔ │ 1m 24s  │ 09:25:07  
docker buildx inspect --bootstrap
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t biltisberger/lastibaer:latest --push .

docker build -t biltisberger/lastibaer:latest .
docker push biltisberger/lastibaer:latest
```

# Run
```bash
docker run -e TRAFFIC_RATE=20 -e CPU_LOAD=70 -e RAM_LOAD=100 -e INTERVAL_MINUTES=1 -e DOWNLOAD_SIZE_LIMIT=5m biltisberger/lastibaer:latest
```

# Environment Variables
- TRAFFIC_RATE: The rate of traffic in Mbps. Default: 20
- CPU_LOAD: The percentage of CPU load. Default: 70
- RAM_LOAD: The of RAM load in MB. Default: 500
- INTERVAL_MINUTES: The interval in minutes to run the test. Default: 1
- DOWNLOAD_SIZE_LIMIT: The download size limit. Default: 2m

# run python script
```bash
python3 workload_generator.py
```

# links
- [https://github.com/mogenius/lastibaer](https://github.com/mogenius/lastibaer)
- [https://hub.docker.com/r/biltisberger/lastibaer](https://hub.docker.com/r/biltisberger/lastibaer)
