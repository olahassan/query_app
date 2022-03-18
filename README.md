# Name: Olatunji Hassan


## Application to query http://www.boredapi.com/api/  based on configuration of number of participants

**Contents**
- [1. Getting Started](#getting-started)
- [2. Local requirements](#local-requirements)
- [3. Issues](#issues)
- [4. LifeCycle Diagram](#lifecycle)
- [5. Infrastructure Diagram](#infrastructure-diagram)


## Getting Started
There is a docker-compose file that allows you to run the application locally. Copy 
docker-compose.yml.tmpl to docker-compose.yml, use "docker-compose up -d" and fill out neccessary environmental variables and postman for testing.

once the applicationis up and running,test the index ie http://127.0.0.1/, url to get the environment and version.

Use "/participants" to get a reply based on the value of PARTICIPANTS set in the environmental variable.

## local requirements
Ensure you have docker version >= 20.10.12 and docker-compose version >= 1.29.2

## Issues
There is currently no https configures. This can be acchieved by adding a proxy service that will terminate the https connection and the pass the traffic to the upstream application.


## Diagram
To deploy to production, I will be inclined to use a containerised solution such as kubernetes. This will require detailing kubernetes manifests and a cloud platform such as AWS to run the cluster. I will then go ahead to describe the stages of building and deploying the application in a ci/cd pipeline (yml file). Once a commit has been merged to main/master branch and it is tagged, it will get deployed to production.

As this is a small application, I will consider using docker-compose on a small ec2 instance using terraform for orchestration. The environmental variables will be set on gitlab and as the deployment passes from staging to prodution, the respective env variables will be injected into the app before it is deployed.


## lifecycle
![lifecycle](/images/app_deployment_life.PNG)

## infrastructure diagram
As there is no database / private resource to consider, there wil only be two public facing subnests, each in different Availability zones to allow for redundancy. The

![infra](/images/infra.PNG)