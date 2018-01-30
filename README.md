# Screwdriver in a Box

This handy feature will bring up an entire Screwdriver instance (ui, api, and log store) locally
for you to play with.  All data written to a database will be stored in `data` directory.

Requires:
 - Python 2.7
 - Mac OSX 10.10+
 - [Docker for Mac][docker]
 - [Docker Compose 1.8.1+][docker-compose]

```bash
$ python <(curl -L https://git.io/screwdriver-box)
```

[docker-compose]: https://www.docker.com/products/docker-compose
[docker]: https://www.docker.com/products/docker
