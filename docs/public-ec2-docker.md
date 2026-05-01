In 2026 we changed the build to live on a single EC2 instance and run docker.

To do this, we created a new EC2 instance in the public subnet of the VPC with an Ubuntu AMI. We connected to it via the AWS GUI.

We attached the Elastic IP we already had to this instance. (13...147)

We had to install Docker on the machine following [Docker's instructions](https://docs.docker.com/engine/install/ubuntu/), it should install v29. We then added docker to the user group to avoid using sudo

```
sudo groupadd docker
sudo userMod -aG docker $USER
newgrp docker
```

We also had to clone the repo

```
git clone https://github.com/UCL-ARC/museum_of_dreams.git
```

Then fill out the variables in compose/.env

And create an acme.json file for letsencrypt & traefik

```
touch traefik/certs/acme.json
chmod 600 traefik/certs/acme.json
```

Ensure the IP is in the list of ALLOWED_HOSTS

Then build

```
sudo docker compose build
```
