# Screwdriver in a Box

This handy feature will bring up an entire Screwdriver instance (ui, api, and log store) locally
for you to play with.  All data written to a database will be stored in `data` directory.

Requires:
 - Python 3.6+
 - [Docker][docker]
 - [Docker Compose 1.8.1+][docker-compose]


Run the below command in your terminal to bring up a Screwdriver cluster locally.

```bash
$ python3 <(curl -L https://git.io/screwdriver-box)
```
You will be prompted to enter your desired SCM provider as well as your Client ID and Client Secret. Afterwards, type `y` to launch Screwdriver!


For further documentation please see: https://docs.screwdriver.cd/cluster-management/running-locally
To set up your own cluster, see: https://docs.screwdriver.cd/cluster-management/kubernetes

[docker-compose]: https://www.docker.com/products/docker-compose
[docker]: https://www.docker.com/products/docker
