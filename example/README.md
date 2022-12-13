# Example 
This implementation implements a working example with 3 flows flow1, flow2, flow3 built with prefect.

## Pre-Requisites
- Docker installed, if run with cuda -> nvidia-docker installed
- Each flow repository consists of a working Dockerfile

## Build steps

### Build Flow Images from Dockerfiles
Build images from Dockerfiles for each repo or application containing a prefect flow. The Dockerfile need prefect as base image or as pip installation in the requirements.

```bash
# 1s flow
cd flow1
docker build . -f flow1.Dockerfile --tag flow1-image
# 2nd flow
cd ../flow2
docker build . -f flow2.Dockerfile --tag flow2-image
# 3rd flow
cd ../flow3
docker build . -f gpu.Dockerfile --tag flow3-image
```
**Remark:** Make sure that the named tag corresponds with the ones given in the `docker-compose.yaml` for each agent.

### 3. Build Prefect deployments

Now, the prefect deployments will be made within each container as the correct package dependencies for the prefect builds are available.

```bash
# flow1
# run container
docker run -it --rm -v $PWD:/root/ flow1-image 
# inside container
cd flow1
prefect deployment build pipeline:integer_pipeline -n flow1-deployment -q flow1-queue
```
```bash
# flow2
# run container
docker run -it --rm -v $PWD:/root/ flow2-image 
# inside container
cd flow2
prefect deployment build pipeline:string_pipeline -n flow2-deployment -q flow2-queue
```

```bash
# flow3
# run container
docker run -it --rm -v $PWD:/root/ flow3-image 
# inside container
cd flow3
prefect deployment build pipeline:cuda_pipeline -n flow3-deployment -q flow3-queue
```
**Remark**: The working queue names need to be consistent with the queue names in the `docker-compose.yaml`


### Start orion UI with 
```bash
docker compose --profile orion up
```
The Orion UI should no be accessible witin your localhost http://127.0.0.1:4200

### Run compose cli and apply builds
```bash
docker compose run cli
```
then, apply the created deployment yaml

```bash
prefect deployment apply flow1/integer_pipeline-deployment.yaml
prefect deployment apply flow2/string_pipeline-deployment.yaml
prefect deployment apply flow3/cuda_pipeline-deployment.yaml
```
Check the if the deployments are available in the orion UI under deployments (http://127.0.0.1:4200/deployments). If they are, everything worked fine.

### 6. Start Agents
```bash
docker compose --profile flow1-agent up
docker compose --profile flow2-agent up
docker compose --profile flow3-agent up
```
Check the working queues in the Orion UI. If the queues are marked as <span style="color:green">Healthy</span>, than the agents are listening to the UI.


## Sources

https://github.com/rpeden/prefect-docker-compose

https://github.com/rpeden/prefect-docker-compose/issues/1

https://docs.prefect.io/
