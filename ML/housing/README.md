# Serve a Machine Learning Model as a Webservice
Serving a simple machine learning model as a webservice using [flask](http://flask.pocoo.org/) and [docker](https://www.docker.com/).

## Getting Started
1. Use app.py to wrap the inference logic in a flask server to serve the model as a REST webservice:
    * Execute the command `python app.py` to run the flask app.
    * Go to the browser and hit the url `0.0.0.0:80` to get a message `Hello World!` displayed. **NOTE**: A permission error may be received at this point. In this case, change the port number to 5000 in `app.run()` command in `app.py`. 
    (Port 80 is a privileged port, so change it to some port that isn't, eg: 5000)
    * Next, run the below command in terminal to query the flask server to get a reply ```2``` for the model file provided in this repo:
     ```
        curl -X POST \
        0.0.0.0:80/predict \
        -H 'Content-Type: application/json' \
        -d '[0.00632,18.0,2.31,0,0.538,6.575,65.2,4.0900,1,296.0,15.3,396.90,4.98]'
     ```
 2. Run ```docker build -t app-iris .``` to  build the docker image using ```Dockerfile```. (Pay attention to the period in the docker build command)
 3. Run ```docker run -p 80:80 app-iris``` to run the docker container that got generated using the `app-iris` docker image. (This assumes that the port in app.py is set to 80)
 4. Use the below command in terminal to query the flask server to get a reply ```2``` for the model file provided in this repo:
    ```
        curl -X POST \
        0.0.0.0:80/predict \
        -H 'Content-Type: application/json' \
        -d '[0.00632,18.0,2.31,0,0.538,6.575,65.2,4.0900,1,296.0,15.3,396.90,4.98]'
    ```


