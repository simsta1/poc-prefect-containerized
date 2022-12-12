![MIT License](https://img.shields.io/badge/Organization-Mitwelten-green)

# easy-flow-containerized
Proof of concept for easy containerized flow with prefect


## Build steps

Use this repo structure as template and copy your data flow repository inside this structure.

### Clone flows and applications
```bash
git clone <dataflow-repo>
git clone <another-dataflow-repo>
```

### Build Flow Images from Dockerfiles
Build images from Dockerfiles for each repo or application containing a prefect flow. The Dockerfile need prefect as base image or as pip installation in the requirements.

```bash
docker build . -f <your-Dockerfile> --tag custom-worker-image
```
**Remark:** Make sure that the named tag corresponds with the one given in the `docker-compose.yaml`

### Build orion UI with 
```bash
docker compose --profile orion up
```
The Orion UI should no be accessible witin your localhost `127.0.0.1:4200`

### Prefect deployments
Now, the prefect deployments will be made with the cli
```bash
docker compose --profile cli up
```
within the cli-container 
```bash
prefect deployment build <script-name>:<flow-function> -n <deployment-name> -q <working-queue-name>
```
then, apply the created deployment yaml
```bash
prefect deployment apply <flow-function>-deployment.yaml
```
Check the if the deployments are available in the orion UI. If they are, everything worked fine.

### Start Agents
```bash
docker compose --profile agent up
```
Check the working queues in the Orion UI. If the queues are marked as healthy, than the agents are listening to the UI.

## Sources

https://github.com/rpeden/prefect-docker-compose
https://github.com/rpeden/prefect-docker-compose/issues/1