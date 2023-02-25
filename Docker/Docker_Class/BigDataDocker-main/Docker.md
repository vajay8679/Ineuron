# Docker

![Untitled](Docker%20e4f5d5d142eb4d3c89bb61faa4dcd65d/Untitled.png)

![Untitled](Docker%20e4f5d5d142eb4d3c89bb61faa4dcd65d/Untitled%201.png)

![Untitled](Docker%20e4f5d5d142eb4d3c89bb61faa4dcd65d/Untitled%202.png)

![Untitled](Docker%20e4f5d5d142eb4d3c89bb61faa4dcd65d/Untitled%203.png)

### Microservices

Microservices are an architectural and organizational approach to software development where software is composed of small independent services that communicate over well-defined APIs. These services are owned by small, self-contained teams.

Microservices architectures make applications easier to scale and faster to develop, enabling innovation and accelerating time-to-market for new features.

**Monolithic vs. Microservices Architecture**

With monolithic architectures, all processes are tightly coupled and run as a single service. This means that if one process of the application experiences a spike in demand, the entire architecture must be scaled. Adding or improving a monolithic application’s features becomes more complex as the code base grows. This complexity limits experimentation and makes it difficult to implement new ideas. Monolithic architectures add risk for application availability because many dependent and tightly coupled processes increase the impact of a single process failure.

With a microservices architecture, an application is built as independent components that run each application process as a service. These services communicate via a well-defined interface using lightweight APIs. Services are built for business capabilities and each service performs a single function. Because they are independently run, each service can be updated, deployed, and scaled to meet demand for specific functions of an application.

![monolith_1-monolith-microservices.70b547e30e30b013051d58a93a6e35e77408a2a8.png](Docker%20e4f5d5d142eb4d3c89bb61faa4dcd65d/monolith_1-monolith-microservices.70b547e30e30b013051d58a93a6e35e77408a2a8.png)

### **Characteristics of Microservices**

**Autonomous**

Each component service in a microservices architecture can be developed, deployed, operated, and scaled without affecting the functioning of other services. Services do not need to share any of their code or implementation with other services. Any communication between individual components happens via well-defined APIs.

**Specialized**

Each service is designed for a set of capabilities and focuses on solving a specific problem. If developers contribute more code to a service over time and the service becomes complex, it can be broken into smaller services.

### **Advantages of Microservices**

### **Lower Costs & Increased Efficiency**

Microservices are typically simpler and more efficient than monolithic applications, which can result in lower costs overall. In addition, because microservices are self-contained, they don’t require the same level of coordination and communication that is needed for monolithic applications. By allowing organizations to use the right technology for the task at hand, microservices can improve efficiency and a reduction in the number of errors. For example, you might choose a different technology stack for each microservice, which can lead to increased performance and scalability.

### **Increased Agility and Scalability**

Microservices can be scaled horizontally very easily, which makes them ideal for situations where scalability is a must. Additionally, because microservices are small and modular, they can be deployed much more quickly than traditional monolithic applications. This increased agility can be a major advantage for organizations that need to respond quickly to changes in the market.

### **Easier Maintenance and Updating**

Since microservices are small and self-contained, it’s much easier to update them than it is to update a monolithic application. In addition, since each microservice is responsible for a specific task, there is less chance of errors occurring when updates are made. This makes maintenance and updating much less risky and time-consuming.

### **Faster Time to Market**

Microservices can also help organizations get their products to market faster. By breaking an application down into smaller, more manageable pieces, it’s often possible to get a product to market more quickly than if a monolithic approach was used.

### **Improved Fault Tolerance**

Microservices are more fault-tolerant than monolithic applications because if one microservice fails, it doesn’t bring down the entire application. This is because microservices are small and modular, which means that they can be independently deployed and managed. Fault isolation can be a major advantage for organizations that cannot afford to have their applications go down.

### **Increased Modularity**

Microservices also offer increased modularity, which can be a major advantage for organizations that need to make changes to their applications quickly. By breaking an application down into smaller pieces, it’s often possible to make changes more quickly and with less risk. Additionally, because microservices are self-contained, it’s easier to understand how they work and how they fit into the overall application.

### **Deployed Independently**

Microservices are independently deployable, which gives organizations more control over their applications. This increased control can be a major advantage for organizations that need to be able to quickly respond to changes in the market. Additionally, by using microservices, organizations can avoid the “monolithic blues” that can occur when a monolithic application becomes too large and unwieldy.

### **Disadvantages of Microservices**

### **Higher Complexity**

Although microservices offer many advantages, they also come with a higher degree of complexity. This complexity can be a major challenge for organizations that are not used to working with microservices. Additionally, because microservices are so independent, it can be difficult to track down errors and resolve them.

### **Increased Network Traffic**

Since microservices are designed to be self-contained, they rely heavily on the network to communicate with each other. This can result in slower response times (network latency) and increased network traffic. In addition, it can be difficult to track down errors that occur when multiple microservices are communicating with each other.

### **Increased Development Time**

Microservices also require more development time than monolithic applications since microservices are more complicated and require more coordination. Additionally, because microservices are deployed independently, it can take longer to get them all up and running. Also, developers need to be familiar with multiple technologies in order to work on a microservice-based application.

### **Limited Reuse of Code**

Microservices also have a limited ability to reuse code, which can lead to increased development time and costs because microservices are typically written in multiple programming languages and use different technology stacks. Therefore, it can be challenging to share code between microservices.

### **Dependency on DevOps**

In order to be successful with microservices, organizations need to have a strong DevOps team in place. This is due to the fact DevOps is responsible for deploying and managing microservices. Without a good DevOps team, it can be difficult to successfully implement and manage a microservice-based application.

### **Difficult in Global Testing and Debugging**

Testing and debugging a microservice-based application can be difficult because the application is spread out across multiple servers and devices. In order to effectively test and debug an application, you need to have access to all of the servers and devices that are part of the system. This can be difficult to do in a large, distributed system.

### What is Docker?

Docker is a software platform that allows you to build, test, and deploy applications quickly. Docker packages software into standardized units called [containers](https://aws.amazon.com/containers/) that have everything the software needs to run including libraries, system tools, code, and runtime. Using Docker, you can quickly deploy and scale applications into any environment and know your code will run.

### Docker vs Virtual Machines

![Docker-and-Virtual-Machine-architecture.webp](Docker%20e4f5d5d142eb4d3c89bb61faa4dcd65d/Docker-and-Virtual-Machine-architecture.webp)

### What is a Container?

A **Docker container** is a virtualized run-time environment where users can isolate applications from the underlying system. These containers are compact, portable units in which you can start up an application quickly and easily.

A valuable feature is the **standardization** of the computing environment running inside the container. Not only does it ensure your application is working in identical circumstances, but it also simplifies sharing with other teammates.

As containers are autonomous, they provide strong isolation, ensuring they do not interrupt other running containers, as well as the server that supports them. Docker claims that these units “provide the strongest isolation capabilities in the industry”. Therefore, you won’t have to worry about keeping your machine **secure** while developing an application.

Unlike virtual machines (VMs) where virtualization happens at the hardware level, containers virtualize at the app layer. They can utilize one machine, share its kernel, and virtualize the operating system to run isolated processes. This makes containers extremely **lightweight**, allowing you to retain valuable resources.

### Where do containers live?

- Container Repo - Amazon ECR, Azure Container Registry
- Private Repos
- DockerHub

### Difference Image and Container

It all starts with a script of instructions that define how to build a specific Docker image. This script is called a [Dockerfile](https://phoenixnap.com/kb/create-docker-images-with-dockerfile). The file automatically executes the outlined commands and creates a **Docker image**.

The command for creating an image from a Dockerfile is **`docker build`**.

The image is then used as a template (or base), which a developer can copy and use it to run an application. The application needs an isolated environment in which to run – a **container**.

This environment is not just a virtual “space”. It entirely relies on the image that created it. The source code, files, dependencies, and binary libraries, which are all found in the Docker image, are the ones that make up a container.

To create a container layer from an image, use the command **`docker create`**.

Finally, after you have launched a container from an existing image, you start its service and run the application.

![crating-a-docker-container.png](Docker%20e4f5d5d142eb4d3c89bb61faa4dcd65d/crating-a-docker-container.png)

 If go on to the docker hub we can see the images of more than 100k apps. 

```bash
docker pull bitnami/nginx:latest -> pulls nginx image
docker pull bitnami/nginx:[TAG] -> image with some specific tag
docker run --name nginx -P bitnami/nginx:latest -> randomly assigns port
docker port nginx -> get the port of container
docker stop nginx -> stop the container
docker run -p 9000:8080 bitnami/nginx:latest -> manually port mapped to 9000
docker images -> gives list of all images
docker ps -a -> gives list all containers
docker ps -> gives list of all running containers
docker rm <container id> -> deletes container
docker image ls -> lists all the images
docker rmi <image name> -> deletes image

```

- You can run container in attached mode (in the foreground) or in detached mode (in the background).
- By default, Docker runs the container in attached mode. In the attached mode, Docker can start the process in the container and attach the console to the process’s standard input, standard output, and standard error.
- Detached mode, started by the option --detach or –d flag in docker run command, means that a Docker container runs in the background of your terminal. It does not receive input or display output. Using detached mode also allows you to close the opened terminal session without stopping the container.

```bash
docker run -d <image name>
docker rm $ (docker ps -a -q) -> delete all container together
```

### Using same image with different tags(versions)

```bash
docker run -d -p 9000:8080 bitnami/nginx:latest
docker run -d -p 9000:8080 bitnami/nginx:1.23
```

docker: Error response from daemon: driver failed programming external connectivity on endpoint compassionate_borg (fd538ba763a62965e6c442dbbdeeb2f97e15cefbc905f065fec615f9ebfcff8a): Bind for 0.0.0.0:9000 failed: port is already allocated.

![Untitled](Docker%20e4f5d5d142eb4d3c89bb61faa4dcd65d/Untitled%204.png)

To overcome this error we have to do something called as port binding.

```bash
docker run -d -p 9000:8080 bitnami/nginx:1.23
docker run -d -p 9001:8080 bitnami/nginx:latest
```

### Debugging containers

```bash
docker logs <container id> -> gives the logs
docker logs <container name> -> gives the logs
docker run --name nginx_latest -d -p 9001:8000 bitnami/nginx:latest -> give custom name to container
docker exec -it <container id> bash -> get inside container through iteractive terminal
env -> all the env variables
pwd -> present working dir
cd -> change dir
cat -> get inside file
exit -> exit the terminal

```

### Hello world app using python

```python
#!/usr/bin/python

import time
from flask import Flask
app = Flask(__name__)

START = time.time()

def elapsed():
    running = time.time() - START
    minutes, seconds = divmod(running, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

@app.route('/')
def root():
    return "Hello World (Python)! (up %s)\n" % elapsed()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8070)
```

### Dockerfile

```python
FROM python:3-alpine
WORKDIR /service
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 8082
ENTRYPOINT [ "python3", "main.py" ]
```

commands to run

```python
docker build -t helloworldpython:latest .
docker images
docker run -p 8082:8070 <img id>
```

### Pushing Image to DockerHub

The ability to build a Docker image and upload that image to a Docker repository.

The reason I say this has led to Docker's success is because the ability to share container images on Docker Hub (Docker's public/private registry) is what allows users to quickly share and build upon preexisting images.

In today's article, we are going to use this feature while learning the `docker push` command and using it to upload our Docker container image to Docker Hub.

## **Creating a Repository on Docker Hub**

Before we can push an image to Docker Hub, we will first need an account on Docker Hub. The signup process is simple and available on the front page of [Docker Hub](https://hub.docker.com/).

Once we have an account, our next step will be to create a new repository for this article. This process is fairly self-explanatory, however the following screenshot shows the type of information we need to provide.

![https://images.ctfassets.net/vtn4rfaw6n2j/2QKeDqLp4dX9v4UEbWKAZ2/fe3b3eb1ff2803f8c6905dde4ed391af/https___blog.codeship.com_wp-content_uploads_2017_07_create-repo.png](https://images.ctfassets.net/vtn4rfaw6n2j/2QKeDqLp4dX9v4UEbWKAZ2/fe3b3eb1ff2803f8c6905dde4ed391af/https___blog.codeship.com_wp-content_uploads_2017_07_create-repo.png)

Once the repository is created, we can start creating our Docker image and upload that image to Docker Hub.

## **Building a New Image**

For this article, we will be creating an image named **push-example**. Typically, if we were building this image for local deployment, we would simply run the following `docker build` command.

```
$ docker build -t push-example .
```

The above command will create a new image tagged as `push-example`. In local deployments, we would simply just issue a `docker run`, specifying this image by its tag name.

While this works for local deployment, this naming convention doesn't work when creating a image for Docker Hub.

### Using your Docker Hub name when building an image

When pushing an image to Docker Hub, we must specify our Docker Hub username as part of the image name. For the example above, I will need to create the image with the tag name of `madflojo/push-example`.

The `madflojo` part of the name is my personal user name for Docker Hub. In order for my image to be uploaded to the **push-example** repository under my user, I must include this username in the image name with the format of (`username/image_name`).

The reason for this is because Docker Hub organizes repositories by user name. Any repository created under my account includes my username in the Docker image name. For example, [in an earlier article](https://blog.codeship.com/using-honcho-create-multi-process-docker-container/), we created a `redis-tls` Docker container that was also made available on Docker Hub. If we wanted to use that same image, we would need to reference that image as `madflojo/redis-tls`.

### Building images for organizations

This same approach is used when building images for an organization's repository. For example, Codeship has an `alpine-docker` repository underneath its organization account. If we wanted to use this image, we would reference this image as `codeship/alpine-docker`. Organization-account names replace the username in the Docker image tag name.

Now that we understand how to name our container, let's go ahead and build the container again with the appropriate tag name.

```
$ docker build -t vishal17/push-example .
```

## **Logging in to Docker Hub**

Before we push and upload our container to Docker Hub, we will first need to log in to Docker Hub from our command-line interface. To do this, we will use the `docker login` command.

```
$ docker login
Username: vishal17
Password:
Login Succeeded
```

Once we have logged in, we can now push our container to Docker Hub.

## **Pushing Our Container**

With the most complicated steps already completed, our next step is fairly simple. All we need to do is issue the `docker push` command specifying our image tag name.

```
$ docker push vishal17/push-example
The push refers to a repository [docker.io/madflojo/push-example]
4393194860cb: Pushed
0011f6346dc8: Pushed
340dc52ed535: Pushed
72073bf3dbb2: Pushed
627a5019997b: Pushed
62924cac48de: Pushed
33f1a94ed7fc: Pushed
b27287a6dbce: Pushed
47c2386f248c: Pushed
2be95f0d8a0c: Pushed
2df9b8def18a: Pushed
latest: digest: sha256:f483e14a1c6b7a13bb7ec0ab1c69f4588da2c253e87652329e615d2f8c439abe size: 2606
```

With the above command complete, our image is now pushed and available on Docker Hub. To see it, we can simply navigate to our newly created [repository](https://hub.docker.com/r/madflojo/push-example/).

### Docker Network

One of the reasons Docker containers and services are so powerful is that you can connect them together, or connect them to non-Docker workloads. Docker containers and services do not even need to be aware that they are deployed on Docker, or whether their peers are also Docker workloads or not. Whether your Docker hosts run Linux, Windows, or a mix of the two, you can use Docker to manage them in a platform-agnostic way.

Docker takes care of the networking aspects so that the containers can communicate with the other containers and also the Docker Host. If you do an **ifconfig** on the Docker Host, you will see the Docker Ethernet adapter. This adapter is created when docker is installed on the Docker Host.

![Untitled](Docker%20e4f5d5d142eb4d3c89bb61faa4dcd65d/Untitled%205.png)

### Advantages of Docker Networking

- They share a single operating system and maintain containers in an isolated environment.
- It requires fewer OS instances to run the workload.
- It helps in the fast delivery of software.
- It helps in application portability.

### Types of Docker network

- Bridge → • **User-defined bridge networks** are best when you need multiple containers to communicate on the same Docker host.
- Host → • **Host networks** are best when the network stack should not be isolated from the Docker host, but you want other aspects of the container to be isolated.
- Overlay → • **Overlay networks** are best when you need containers running on different Docker hosts to communicate, or when multiple applications work together using swarm services.
- IPvlan
- MACvlan → **Macvlan networks** are best when you are migrating from a VM setup or need your containers to look like physical hosts on your network, each with a unique MAC address.
- none

### [Cheatsheet Link](https://dockerlabs.collabnix.com/docker/cheatsheet/)
