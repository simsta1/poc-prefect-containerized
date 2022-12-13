# poc-prefect-containerized
>Proof of concept for simple containerized flows with prefect in a local environment. The repo structure can be used as a template and the flow* folders removed respectively.

## Pre-Requisites
- Docker installed, if run with cuda -> nvidia-docker installed
- Each flow repository consists of a working Dockerfile
- Flow tested locally and it is running

## Build steps

Use this repo structure as template and copy your data flow repository inside this structure.

1. Clone Repos with prefect flows inside root
2. Build Images from Repo Dockerfiles
    - Make sure naming of images is equal to image names in `docker-compose.yaml`
3. Run Images in container and build prefect deployments
4. Start prefect orion UI
5. Start docker compose cli and apply prefect deployments
6. Start agents

### 1. Clone flows and applications
```bash
git clone <dataflow-repo>
git clone <another-dataflow-repo>
```

### 2. Build Flow Images from Dockerfiles
Build images from Dockerfiles for each repo or application containing a prefect flow. The Dockerfile need prefect as base image or as pip installation in the requirements.

```bash
docker build . -f <your-Dockerfile> --tag custom-worker-image
```
**Remark:** Make sure that the named tag corresponds with the ones given in the `docker-compose.yaml` for each agent.

### 3. Build Prefect deployments

Now, the prefect deployments will be made within each container as the correct dependencies for the prefect builds are available.

```bash
docker run -it -v $PWD:/root/ <your-flow-image>
```

within the flow-container 
```bash
prefect deployment build <script-name>:<flow-function> -n <deployment-name> -q <working-queue-name>
```
**Remark**: The working queue names need to be consistent with the queue names in the `docker-compose.yaml`


### 4. Start orion UI with 
```bash
docker compose --profile orion up
```
The Orion UI should no be accessible witin your localhost `127.0.0.1:4200`

### 5. Run compose cli and apply builds
```bash
docker compose run cli
```
then, apply the created deployment yaml
```bash
prefect deployment apply <flow-function>-deployment.yaml
```
Check the if the deployments are available in the orion UI under deployments. If they are, everything worked fine.

### 6. Start Agents
```bash
docker compose --profile <agent> up
```
Check the working queues in the Orion UI. If the queues are marked as <span style="color:green">Healthy</span>, than the agents are listening to the UI.


## Sources

https://github.com/rpeden/prefect-docker-compose

https://github.com/rpeden/prefect-docker-compose/issues/1

https://docs.prefect.io/
