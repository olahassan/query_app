O# Name: Olatunji Hassan


## Application to query http://www.boredapi.com/api/  based on configuration of number of participants

**Contents**
- [1. Getting Started](#getting-started)
- [2. Local requirements](#local-requirements)
- [3. Issues](#issues-and-improvement)
- [4. LifeCycle Diagram](#lifecycle)
- [5. Infrastructure Diagram](#infrastructure-diagram)


## Getting Started
There is a docker-compose file that allows you to run the application locally. Copy 
docker-compose.yml.tmpl to docker-compose.yml, fill out the neccessary environmental variables, use "docker-compose up -d" and postman for testing.

Once the application is up and running, test the index i.e. http://127.0.0.1:9000/, URL to get the current environment and version.

Use "/participants" to get a reply based on the value of PARTICIPANTS set in the environmental variable.

## Local requirements
Ensure you have docker version >= 20.10.12 and docker-compose version >= 1.29.2.

## Issues and Improvement
- There is currently no https configured. This can be acchieved by adding a proxy service that will terminate the https connection and pass the traffic to the upstream application.
- For administering the deployment, there should be consideration for a bastion host on the network that allows for remote connection for troubleshooting, monitoring etc.
- The branches responsible for deploying to staging/production should be protected, hence, only authourised users/ a succesfull unit test etc. will enable deployment to the respective environment. 


## Diagram
To deploy to production, I will be inclined to use a containerised solution such as kubernetes. This will require detailing kubernetes manifests and a cloud platform such as AWS to run the cluster. I will then go ahead to describe the stages of building and deploying the application in a CI/CD pipeline (yml file). Once a commit has been merged to main/master branch or tagged, it will get deployed to production.

As this is a small application, I will consider using docker-compose on a small ec2 instance using terraform for orchestration. The environmental variables will be set on gitlab and as the deployment passes from staging to prodution, the respective env variables will be injected into the app before it is deployed.


## lifecycle
![lifecycle](/images/app_deployment_life.PNG)

## Infrastructure diagram
As there is no database / private resource to consider, there will only be two public facing subnests, each in different Availability zones to allow for redundancy. The

![infra](/images/infra.PNG)