## Docker installation on
* [1. Ubuntu 20.04](#ubuntu-20-04)
* [2. Ubuntu 20.04](#ubuntu-18-04)
* [3. CentOS 7](#centos-7)
* [4. Amazon linux](#amazon-linux)


<a id='ubuntu-20-04'></a>
### 1. Install docker on Ubuntu 20.04

1. First, update your existing list of packages:

```sudo apt update```

2. Next, install a few prerequisite packages which let apt use packages over HTTPS:

```sudo apt install apt-transport-https ca-certificates curl software-properties-common```

3. Then add the GPG key for the official Docker repository to your system:

```curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -```

4. Add the Docker repository to APT sources:

```sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"```

5. Next, update the package database with the Docker packages from the newly added repo:

```sudo apt update```

6. Make sure you are about to install from the Docker repo instead of the default Ubuntu repo:

```apt-cache policy docker-ce```

7. Finally, install Docker:

```sudo apt install docker-ce```

8. Docker should now be installed, the daemon started, and the process enabled to start on boot. Check that it's running:

```sudo systemctl status docker```

9. If you want to avoid typing sudo whenever you run the docker command, add your username to the docker group:

```sudo usermod -aG docker ${USER}```

10. Logout and login again. Now you will be able to run docker commands as the user

<a id='ubuntu-18-04'></a>
### 2. Install docker on Ubuntu 18.04

1. First, update your existing list of packages:

```sudo apt update```

2. Next, install a few prerequisite packages which let apt use packages over HTTPS:

```sudo apt install apt-transport-https ca-certificates curl software-properties-common```

3. Then add the GPG key for the official Docker repository to your system:

```curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -```

4. Add the Docker repository to APT sources:

```sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"```

5. Next, update the package database with the Docker packages from the newly added repo:

```sudo apt update```

6. Make sure you are about to install from the Docker repo instead of the default Ubuntu repo:

```apt-cache policy docker-ce```

7. Finally, install Docker:

```sudo apt install docker-ce```

8. Docker should now be installed, the daemon started, and the process enabled to start on boot. Check that it's running:

```sudo systemctl status docker```

9. If you want to avoid typing sudo whenever you run the docker command, add your username to the docker group:

```sudo usermod -aG docker ${USER}```



<a id='centos-7'></a>
### 3. Install docker on CentOS 7


1. Run update

```yum update -y```

2. Add the yum repo

```sudo tee /etc/yum.repos.d/docker.repo <<-'EOF'
[dockerrepo]
name=Docker Repository
baseurl=https://yum.dockerproject.org/repo/main/centos/7/
enabled=1
gpgcheck=1
gpgkey=https://yum.dockerproject.org/gpg
EOF
```


3. Install the Docker package.

```sudo yum install -y docker-engine```

4. Enable the service.

```sudo systemctl enable docker.service```

5. Start the Docker daemon.

```sudo systemctl start docker```

6. If you want to be able to use docker from a non root user run below command from that user (note that this user needs sudo privilege)

```sudo usermod -aG docker $(whoami)```

7. Logout and login again

8. Now you can start using docker as the user



<a id='amazon-linux'></a>
### 4. Install docker on Amazon linux
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html

1. Run update

```yum update -y```

2. Install the most recent Docker Engine package.

If using Amazon Linux 2 run below command

```sudo amazon-linux-extras install docker```

If using Amazon Linux run below command

```sudo yum install docker```

3. Install Docker

```sudo yum install docker```

4. Start the docker service

```sudo service docker start```

5. Set permissions for user to use docker commands

```sudo usermod -a -G docker ec2-user```
