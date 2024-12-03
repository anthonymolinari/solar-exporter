# solar-exporter


## deploy container
```shell
docker run -d \
    --name enphase_exporter \
    -p 8000:8000 \
    -e user=<enphase_username> \
    -e password=<enphase_password> \
    -e gateway=<gateway_address> \
    anthonymolinari/solar-eporter:latest
```

## pometheus config
```
```

## docker-compose
```yaml
```

