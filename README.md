# feedback APP
*Simplification is our vision.*<br><br>
We want to revolutionize the way meetings and events are held today! We will create a platform for speech-to-text notes taking and giving feedback to the speaker. We want ours to become the service of choice for taking notes automatically instead of on paper or on laptops, and for giving feedback to advertisers and publishers. <br><br>
We want to mass market it to anyone wishing to receive feedback or take notes, particularly from speech:business professionals, professors, students, event organizers, media publishers and advertisers for real-time feedback: TV shows like presidential and other debates, online feedback to soap operas, TV ads, etc. <br><br>
Think of all business events or University courses you have attended: Forget consolidating meeting minutes or writing down what the speaker says! Taking notes automatically from the speech and giving real-time feedback to a publisher is the next technological evolution. Think also of meetings with specialists like doctors or lawyers where understanding language makes it difficult to follow them: Notes taking becomes a simple task and they are available for later review.

# How to install
The complete web application runs inside of a so called *docker container*. In a simplified way docker container can 
be seen as "lightweight" virtual machines. Follow the steps below to install the feedback app:

1. Make sure you have installed [Docker](http://www.docker.com) :whale: 
2. Navigate into the root directory of this project (where the "Dockerfile") is located and run: <br>
`docker build -t jestherday/feedback:latest .`
3. Get an awesome :coffee:/:beer: or [read some outstanding facts about numbers](http://numbersapi.com/#42) while docker builds the image
4. :tada: CONGRATULATIONS :tada: - you've successfully set up the necessary environment which includes:
  * [Ubuntu LTS (16.04)](https://www.ubuntu.com/) (actual image from [DockerHub](https://hub.docker.com/_/ubuntu/))
  * [PostgreSQL 9.5](https://www.postgresql.org/)
  * [Python 2.7](https://www.python.org/) including the packages:
    * [psycopg2](http://initd.org/psycopg/)
    * [web.py](http://webpy.org/)
  * [Jupyter 1.0](http://jupyter.org/)
  * [VIM 7.4](http://www.vim.org/)
  * [Git 2.7.4](https://git-scm.com/)
  * all source files contained in this repository
5. To start the docker container run `docker run -it -p 8080:8080 jestherday/feedback`
6. To start the webapp (currently placeholder) run `python src/webdummy.py`
7. Open a browser (on your host machine) and open the address `localhost:8080`
8. If everything worked well you should be able to read the line *Hello World - Awesome App will soon be here*
9. To be continued...

# How to develop

## Available Tools

#### VIM (via command line)
*"Vim is a highly configurable text editor built to make creating and changing any kind of text very efficient. It is included as "vi" with most UNIX systems and with Apple OS X."* <sup>[[1]](www.vim.org)</sup> The navigation within VIM requires a bit of training, therefore the following ressources are recommended:
[Interactive VIM tutorial (free)](http://www.openvim.com/), 
[VIM adventures (freemium)](http://vim-adventures.com/)

#### Jupyter (via web browser)
*"The Jupyter Notebook is a web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, machine learning and much more."* <sup>[[2]](http://jupyter.org/#about-notebook)</sup> The docker container is set up in a way, that you can run a Jupyter server within the container that can be accessed through the hosts' web browser. This
requires a slightly different starting procedure (compared to the one stated above):

1. Follow steps 1,2,3 & 4 from the [section above](#how-to-install)
2. Run `docker run -it -p 8080:8080 -p 8889:8888 jestherday/feedback` to start the container
3. Inside the container run `jupyter notebook --no-browser &` to start a Jupyter server (as a deamon)
4. Open a web browser (on your host machine) and open the address `localhost:8889`
5. If everything worked well you should see the typical Juypter page

## Developer Guideline
... to be written

***
[1] - Vim Homepage, www.vim.org<br>
[2] - Jupyter Homepage, jupyter.org
