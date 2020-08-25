# Flaskapp for minikube

Running python flask app which shows the POD-ID where application is running

#### Getting Started

##### First we will use some other image for deployment than we will update that deployment to use this image.

###### Make Deployment with docker image-
```
kubectl create deployment myflaskapp-forminikube --image=docker.io/mjindal/myflaskapp-forminikube:latest
```
###### Expose Deployment
```
kubectl expose deployment myflaskapp-forminikube --type="LoadBalancer" --port 5000
```

###### View Deployment from host system (this will give the url where it is running)
```
minikube.exe service myflaskapp-forminikube --url
```
you should see the container id where app is running .

###### Now scale application to use 5 containers
```
kubectl.exe scale deployment myflaskapp-forminikube --replicas 5
```
Refresh the browser you should see different-different container id.

###### There should be exactly 5 pods running -
```
kubectl.exe get pods
```

###### Scale down replica to 1 - 4 pods should die immediately !
```
kubectl.exe scale deployment myflaskapp-forminikube --replicas 1
```

###### Rebuild the image
```
eval $(minikube docker-env)
#this will cause docker to build with the docker deaemon of minikube 
docker build -t mjindal/myflaskapp-forminikube:latest .
```
###### Now change the image
```
 kubectl set image deployment/myflask-app-forminikube *="mjindal/myflaskapp-forminikube:latest"
```
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
