# solar-exporter


## deploy container
```shell
docker run -d \
    --name enphase_exporter \
    -p 8000:8000 \
    -e USER=<enphase_username> \
    -e PASSWORD=<enphase_password> \
    -e SERIAL=<enpahse_gateway_serial_number> \
    -e GATEWAY=<gateway_address> \
    anthonymolinari/solar-eporter:latest
```

## pometheus config
```
```

## docker-compose
```yaml
```

