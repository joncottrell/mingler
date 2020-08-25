# Mingler #

### A web app to help you schedule weekly 1:1 meetings for all personnel to get to know each other. ###

## Deployments ##

### Setup ###
* Install gcloud CLI.
* Run `gcloud init` and use project `mingler-286419`

### Deploy ###
* Any time code in `frontend/mingler-app` is changed, run `./build.sh`
* Navigate to `mingler/backend`
* Run `gcloud app deploy app.yaml`