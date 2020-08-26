# Flaskapp for minikube

Running python flask app which shows the POD-ID where application is running

#### Getting Started - git Clone this project

###### Rebuild the image
```
eval $(minikube docker-env)
#this will cause docker to build with the docker deaemon of minikube 
docker build -t myflaskapp-forminikube:latest myflaskapp-forminikube
eval $(minikube docker-env -u)
```
##
###### Make Deployment with local docker image on minikube daemon-
```
cat << YAMLEOF > myflaskapp-forminikube-deployment.yml 
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: myflaskapp-forminikube
  name: myflaskapp-forminikube
spec:
  replicas: 1
  selector:
    matchLabels:
      app: myflaskapp-forminikube
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: myflaskapp-forminikube
    spec:
      containers:
      - image: myflaskapp-forminikube:latest
        name: myflaskapp-forminikube
        resources: {}
        imagePullPolicy: Never

YAMLEOF
kubectl apply -f myflaskapp-forminikube-deployment.yml
```
###### Expose Deployment
```
kubectl expose deployment myflaskapp-forminikube --type="LoadBalancer" --port 5000
```

###### View Deployment from host system (this will give the url where it is running)
```
minikube service myflaskapp-forminikube --url
```
you should see the container id where app is running .

##### Prerequisites

What things you need to install the software and how to install them

```
Download kubectl and minikube.
Extract both and install in /usr/local/bin.

```

##### Installation

A step by step series of examples that tell you have to get a development env running

Install docker

* [docker](https://docker.com)

```
curl -fsSL https://get.docker.com/ | sh
sudo usermod -aG docker $USER
sudo systemctl start docker
```

Install minikube

* [minikube](https://github.com/kubernetes/minikube/releases)


Install Kubectl

* [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

Start docker

* [RedHat|Centos|Amazon Linux etc]
```
$ systemctl start docker
```

* [Debian|Ubuntu etc]
```
$ service docker start
```
Start Minikube with docker driver

```
minikube start --driver=docker

```
