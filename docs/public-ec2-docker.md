In 2026 we changed the build to live on a single EC2 instance and run docker.

To do this, we created a new EC2 instance in the public subnet of the VPC with an Ubuntu AMI. We connected to it via the AWS GUI.

We attached the Elastic IP we already had to this instance (13...147) and associated the A record in route 53 for the URL we wanted to use

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
docker compose build
```

If no errors, spin up

```
docker compose up -d
```

To load data from a dump, you'll need to copy it into the docker system from the host machine, we'll put it in the root dir, make the `persist` dir if you haven't got one

```
mkdir persist
docker cp ./persist/prod-dump-060526.json museum_of_dreams-django-1:/
```

From inside the django container, you can then load the data

```
docker exec -it museum_of_dreams-django-1 bash
python manage.py loaddata /prod-dump-060526.json
```

> [!WARNING]
> if there is already data, you will want to flush the db
> `python manage.py flush`

## Updating

Ensure you have env files and an acme file that persist on the EC2 instance

```
mv compose/.env/*.env traefik/certs/acme.json ~/persist
```

When updating from git, you'll need to reapply the env files and acme file after pulling in changes

If the traefik/certs dir doesn't exist

```
mkdir -p traefik/certs
```

```
cp ../persist/*.env compose/.env
cp ../persist/acme.json traefik/certs/
```

and then rebuild and spin up after confirming no errors on the build. This also reduces downtime on the site

```
docker compose build
```

```
docker compose up -d
```

---

### Other commands

if you need to access the django container shell:

```
docker exec -it museum_of_dreams-django-1 bash
```

you can see variables with

```
python -c "import django; import django.conf;  print(django.conf.settings.ALLOWED_HOSTS)"
```

---

### Backups

upload of dumps via VPC into S3 bucket
automated on a cron job
