### How to use Heroku to host your python web app for free

<a id='toc'></a>
<a id='toc'></a>
## Table of Contents
* [1. Background](#background)
* [2. Preparation](#preparation)
* [3. Deploy your Web app to Heroku](#deploy-app)
  * [3.1 Deploy as a docker container to Heroku](#deploy-app-docker)
  * [3.2 Deploy without docker container to Heroku](#deploy-app-nodocker)

----

<a id='background'></a>
[back to TOC](#toc)
### 1. Background:
In the Machine Learning Zoomcamp course conducted by Alexey Grigorev (https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp) in Week/Session #5, it is required to deploy a web service which can accept user provided customer data and using a trained ML model, predict whether the customer will churn or not.

For this, participants can either deploy the web service locally on their machine, inside a docker container on their machine, or in Cloud (AWS, Azure. Google etc.).

There was one more option that was suggested, which is to use Heroku to host python based web application for free. This option will especially be useful when working on the Project 1 as part of this course, and hence I thought of exploring this option and preparing this reference for others to follow if they wish to use this option.

Following are the steps to use Heroku. These have been explained with an example web app that was used for the homework of week5 of the course.

*Thanks to Harshit for his video https://www.youtube.com/watch?v=1Z7nt0Fyits from where I learned the steps, and then some more reading from Heroku documentation.*

----
<a id='preparation'></a>
[back to TOC](#toc)
### 2. Preparation
#### 2.1 Create account in Heroku

Go to https://www.heroku.com/ and Signup

![Signup1](images/1-heroku-signup-1.png)

![Signup2](images/2-heroku-signup-2.png)

You can also setup Google authenticator app on your mobile to get a token (OTP) and use it for Multi-factor authentication when logging in to Heroku.

Once logged in, you can deploy web app in any of the languages - Python, Ruby, PHP, Node.js, Java, Go, Closure, Scala

![Heroku dashboard](images/3-heroku-dashboard.png)

#### 2.2. Install Heroku command line interface (cli) on your machine

There are multiple ways to deploy a web app on Heroku (via the Heroku Dashboard, using CLI from your machine), of which I used the CLI option.

There are multiple options availabe to install Heroku cli - which can be found here - https://devcenter.heroku.com/articles/heroku-cli. I chose downloading the tarball, since it does not need any installation. 

**a. Download tarball**

To install from tarball, go to https://devcenter.heroku.com/articles/heroku-cli#tarballs and download the tarball for the Operating system of your machine. I downloaded for Ubuntu.

**b. Extract tarball**

Extract the tarball (Step fo Ubuntu shown below. For Windows simply use the WinZip or equivalent to extract/unzip from tarball).

![Extract tarball1](images/5-heroku-extract-tarball-ubuntu-1.png)

![Extract tarball2](images/6-heroku-extract-tarball-ubuntu-2.png)

**c. Add heroku/bin to your PATH**

To add the heroku/bin path on a Linux machine, execute the below command. For Windows refer to https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/

![Add heroko to path](images/7-add-heroku-path.png)

----
[back to TOC](#toc)
<a id='deploy-app'></a>
### 3. Deploy your Web app to Heroku
When using Heroku, you can deploy your Web app as a docker container to heroku, or you can deploy it without using docker. Following section explains both these options.

[back to TOC](#toc)
<a id='deploy-app-docker'></a>
#### 3.1 Deploy as a docker container to Heroku

To be able to deploy to Heroku as a docker container, you need to first have docker installed and running. For this, you have 2 options:
* 1. Use docker installed on your local machine
* 2. Use Google Cloud shell which has docker pre-installed. Google Cloud shell provides a free machine if you have a Gmail account. 

Steps to deploy your app to heroku as a docker container are explained below (including the slight difference for the 2 options mentioned above)

**a. Prepare code base for docker deployment**

Create a directory for your deployment and copy your code for the Web app, any ML model files (if/as appropriate), python package dependencies (this example shows use of pipenv and hence Pipfile and Pipfile.lock, however you can requirements.txt or files as applicable for you).

> If you are using Google Cloud shell refer to guide in this [link](./how-to-use-google-cloud-shell-for-docker.md) to understand how to upload your files to Google Cloud shell

![Create directory and copy code](images/hd-1-code-base.png)

**b. Create Dockerfile**

Create Dockerfile (filename should be exactly this) in the same directory with appropriate lines for your docker image.

Below example shows, python:3.8.12-slim being used as base image, installing pipenv, then copying the Pipfile and Pipfile.lock that specify python dependency packages, installing the dependency packages using pipenv, then copying the python code for the web app, followed by defining port to be exposed and entrypoint command that should get run when docker container starts.

**Note:** One very important point I struggled and understood after a long time is that you cannot map to a custom port in Heroku. Thus, for gunicorn, do not use anything like 

```ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "sample_app:app"]```

but something like

```ENTRYPOINT ["gunicorn", "sample_app:app"]```

Although using the first syntax worked when running docker container locally on my machine, it failed when deployed to Heroku - hence suggesting the second syntax. Will try to investigate further and update once I know better.

![Create Dockerfile](images/hd-2-dockerfile.png)

**c. Deploy to Heroku as docker container**

Run the following steps in sequence to deploy your web app as a docker container to Heroku.

If you are executing these steps from your local machine then follow steps in [Option A](#option-a) below. However if you are executing these steps from Google Cloud shell, then follow steps in [Option B](#option-b) below. The difference is due to the fact that the step to login from your local machine will open a web browser where you can login to Heroku providing credentials. Whereas from Google Cloud shell, the web browser tab cannot be opened for you to login. Hence for the Google Cloud shell scenario, we will use API key from Heroku. 

<a id='option-a'></a>
**Option A: Login to heroku from your machine** : Verify heroku command is found (In step 2.2.c. above the path has already been set) in the path. Then using heroku cli, login to heroku.  Press any key when asked to do so.

```which heroku```

```heroku login```

![initial local git repo2](images/15-heroku-webapp-deploy-8.png)
  
This will open a tab in your web browser asking you to login to Heroku. Login to Heroku.

![initial local git repo3](images/16-heroku-webapp-deploy-9.png)

![initial local git repo4](images/17-heroku-webapp-deploy-10.png)

Now you can close this tab and return to the command prompt on your terminal
  
![initial local git repo5](images/18-heroku-webapp-deploy-11.png)

You can skip Option B below and continue with steps provided in [Login to Heroku container](#login-heroku-container)

<a id='option-b'></a>
**Option B: Login to heroku from Google Cloud shell**  : From your web browser, login to Heroko and go to **Account settings**. On the Account setting screen, go to **Applications** tab and under **Authorizations** click **Create authorization**

![Goto heroku auth](images/heroku-1-auth.png)

Provide some name for the authorization and optionally set expiration time and create authorization (This will create an API key which can be used to login to Heroku from Google Cloud shell)

![Create heroku auth](images/heroku-2-create-auth.png)

![Auth token generated](images/heroku-3-auth-token-generated.png)

Copy the generated token (i.e. API key) and go to your Google Cloud shell prompt. Here, define and export a variable named HEROKU_API_KEY with value as the key you copied. Example command shown below (Please note there should not be any space before or after the =, and the key should be enclosed in ")

```export HEROKU_API_KEY="8fb57c22-c44e-4dd5-b5d7-6315705b7bbe"```

![Define API Key var](images/heroku-4-gcp-set-heroku-auth-var.png)

Run the following steps to add Google DNS server entry to a file /etc/resolv.conf (I had to do this to be able to connect to Heroku container registry from within Google cloud shell).

```
$ echo "nameserver 8.8.8.8" > /tmp/1
$ cat /etc/resolv.conf >> /tmp/1
$ sudo cp /tmp/1 /etc/resolv.conf
```

<a id='login-heroku-container'></a>
**Login to Heroku container**  : Login to Heroku container registry.

```heroku container:login```

![Login to Heroku container](images/hd-3-heroku-container-login.png)

**Create app in Heroku**: Create an app in Heroku. Below example shows creating a app with the name ml-zoom-docker.

```heroku create ml-zoom-docker```

![Create app in Heroku](images/hd-4-create-app.png)

**Push docker image to Heroku**: Push docker image to Heroku container registry. When you run the below command, the Dockerfile will be used to build the docker image locally on your machine and then push the image to Heroku container registry. Using the -a flag you specify the application name (e.g. ml-zoom-docker app that you created above).

```heroku container:push web -a ml-zoom-docker```

![Push docker image to Heroku](images/hd-5-push-container-1.png)

![](images/hd-5-push-container-2.png)

**Release container**: Deploy container on Heroku. When you run the below command, a docker container will be launched in Heroku from the docker image that you pushed to Heroku container registry.

```heroku container:release web -a ml-zoom-docker```

![Deploy container](images/hd-6-container-release.png)

**Launch you app**: Open your web app. For this you can go your web browser and open your application URL with appropriate path (e.g. my sample application would run at https://ml-zoom-docker.herokuapp.com/welcome - since ml-zoom-docker is the name of my app and I am serving page /welcome via my sample app)

![Launch app](images/hd-7-launch-app.png)

**Great !!!** You web app is now running in Heroku as a docker container !!!

---

[back to TOC](#toc)
<a id='deploy-app-nodocker'></a>
#### 3.2 Deploy without docker container to Heroku
To deploy your Web app to Heroku, you need to have all your code in one place and create a few configuration files.

**a. Prepare code base**

Create a directory for your deployment and copy your code for the Web app and any ML model files (if/as appropriate)

![Create directory](images/8-heroku-webapp-deploy-1.png)

![Copy code](images/9-heroku-webapp-deploy-2.png)

**b. Create configuration files**

**Specify Python version** : This is an optional step, required only if you want a specific Python version to be used in Heroku to run your web app. Check the Python version (where you have the appropriate version and where you developed/tested your code) using command ```python -V```.

![Check Python version](images/10-heroku-webapp-deploy-3.png)

Specify the version into a file named runtime.txt [Ensure everything is lower case in the file and that you mention the full version]

![Specify python version in runtime.txt](images/11-heroku-webapp-deploy-4.png)

*Refer to https://devcenter.heroku.com/articles/python-runtimes for more details*

**Specify Python dependencies/packages** : Create requirements.txt file and specify the Python packages required for the execution of your Web app.

You could choose to use the command ```pip freeze > requirement.txt``` to populate requirements.txt based on all packages installed in your current active python environment. Or add the package names manually. I added manually.

![Python dependency packages](images/12-heroku-webapp-deploy-5.png)

*Note: As part of the course homework 5, scikit-learn version 1.0 is required since the model was trained using this version. Added gunicorn, to be used as the web server to run the web app in Heroku (there could be other options, for now I know of this)*

**Specify commands to be executed by the app on startup** : Heroku apps include a Procfile that specifies the commands that are executed by the app on startup.

The command for this example would be as below. 

web: gunicorn \<name of your python script without the .py\>:\<instance name of Flask\>

* web: indicates that the web server process can receive external HTTP traffic from Heroku’s routers.
* gunicorn is the web server (software) that will be used
* app is the instance name of Flask when you define something like **app = Flask(somename_foryourapp)**

e.g. I used ```web: gunicorn w5-hw-svc-predict:app``` since my python file name is w5-hw-svc-predict.py and I have defined Flask instance as ```app = Flask('churn')```
  
![Procfile](images/13-heroku-webapp-deploy-6.png)
  
*Find more info on Procfile [here](https://devcenter.heroku.com/articles/procfile)*
  
**c. Deploy web app to Heroku**

Heroku supports multiple methods for deployment - Git (GitHub, Heroku Git), Docker container image, Integrations. So far, I have explored the Git method using Heroku git.
  
*Assuming you have git installed on your machine. If not install it. (On Ubuntu using ```sudo apt install -y git```)*
  
**Initialize local git repository** : After having collected your code and defined necessary configurations files, initialize local git repository
  
```git init```
  
Add all the contents of the directory to git repo
  
```git add .```
  
Commit changes to local git repo
  
```git commit -m "some commit message"```
  
![initial local git repo1](images/14-heroku-webapp-deploy-7.png)

**Login to heroku** : Verify heroku command is found (In step 2.2.c. above the path has already been set) in the path. Then using heroku cli, login to heroku.  Press any key when asked to do so.

```which heroku```

```heroku login```

![initial local git repo2](images/15-heroku-webapp-deploy-8.png)
  
This will open a tab in your web browser asking you to login to Heroku. Login to Heroku.

![initial local git repo3](images/16-heroku-webapp-deploy-9.png)

![initial local git repo4](images/17-heroku-webapp-deploy-10.png)

Now you can close this tab and return to the command prompt on your terminal
  
![initial local git repo5](images/18-heroku-webapp-deploy-11.png)
  
**Create an application** : You need to create a new application in Heroku before deploying the code to it. Create an application
  
![Create application](images/19-heroku-webapp-deploy-12.png)
  
This creates an application and also a Heroku git repo for this application. You can go to the Heroku dashboard to see the application being created with a default web page.
  
![Application](images/20-heroku-webapp-deploy-13.png)
  
![Default web page1](images/21-heroku-webapp-deploy-14.png)

**Push code and configurations to Heroku git for deployment** : You can now push to remote git (Heroku git). Once the contents are pushed to Heroku git, it automatically triggers the deployment.
  
![Default web page2](images/22-heroku-webapp-deploy-15.png)
  
![Default web page3](images/23-heroku-webapp-deploy-16.png)

**Test your Web App**

You can now test whether your Web App is running successfully (now being hosted on Heroku). From your local machine (or from anywhere, where you have python installed, requests package installed and having internet access) execute the code to test your Web App.

Below is sample test scenario for the homework of Week5 of ML Zoomcamp course.
  
![Test Web app](images/24-request.png)

