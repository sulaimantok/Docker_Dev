# Docker_Dev
This is the documentation of my lab results when learning about the docker compose

Docker is one of the tools to use containers, what is containers ?
containers is
```
a lightweight, stand-alone, executable package of a
piece of software that includes everything needed to
run it: code, runtime, system tools, system libraries,
settings.
```
### Why using Docker ?
#### lightweight
- Containers running on a single machine share that machine's operatng system kernel; they start   instantly and use less compute and RAM.
- Images are constructed from flesystem layers and share common fles. his minimizes disk usage and image downloads are much faster.

#### Standard
- Containers are based on open standards and run on all major Linux distributons, Microsof Windows, and on any infrastructure including VMs, bare-metal and in the cloud.

#### Secure
- Docker containers isolate applicatons from one another and from the underlying infrastructure. Docker provides the strongest default isolaton to limit app issues to a single container instead of the entre machine.

For comparison with Virtual machines as we have used, we can see the following picture :
![compare](image/compare.png)

for full documentation, access [this](https://docs.docker.com/)

### Let's Hand on
Requirements:
- [x] Virtual Machine with Linux Or Windows (sample using ubuntu 16.04)
- [x] Internet connection
- [x] Requires enthusiasm and patience

#### Installation
1. Using Ubuntu
```
sudo apt -y install docker.io
sudo systemctl status docker
```
2. Using CentOs
```
yum -y install docker
```
3. Using Windows and Mac
  - Download File installer [this](https://docs.docker.com/docker-for-windows/install/)
4. Verify Docker install
```
docker --version
docker version
docker info
```

#### Simple Lab
1. First Applicatons
```
docker run hello-world
#list images
docker image ls
#show list Container active or inactive
docker container ls -a
```
2. Try another application
```
docker run docker/whalesay cowsay nameapp
#show image list
docker image ls
```
Other images, you can see on [this](https://hub.docker.com)
