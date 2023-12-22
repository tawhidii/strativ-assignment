# Starativ Assignment

### Setup

The following steps will walk you through installation on a Linux. Mac should be similar.
It's also possible to up and running on a Windows machine.

#### Dependencies

###### Prerequisites

- Docker version >= 20.0.0

Clone repository using following command :

`git clone https://github.com/tawhidii/strativ-assignment.git`

After successfully cloning of the repository , spin up docker containers by following:
`docker compose up -d`

> It will take time to build and startup the containers.

After that please check `Make` installed on your machine by typing `make -v`. If not installed please install by typing `sudo apt-get -y install make`.

Finally execute these command one by one given below:

```bash
make migrate
make collectstatic
make createsuperuser
make seed
```

## API lists:

- Get Coolest District endpoint:

  - endpoint :`http://localhost:8005/tasks/coolest-districts/`

- Travel recommendation endpoint:
  - endpoint :`http://localhost:8005/tasks/tarvel-recomendation/`
    payload :
    {
    "location":"Gaibandha",
    "destination":"Rangpur",
    "travel_date":"2023-12-24"
    }
