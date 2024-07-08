# FastAPI Application for Stable Diffusion Model

FastAPI application with docker and Kubernett

## Run 
To run your app on server, use uvicorn

    uvicorn main:app --reload # Reload to make the server automatically refreshed if the file changes

Then click on the link with /docs like http://127.0.0.1:8000/docs. We get an iterative UI page

Test with POST, click on try it out - execute

Get the Curl command that we could run in terminalas well 

Other UI can also go for http://127.0.0.1:8000/redoc - which ever docs or redoc is preferred

Click on openapi.json - all information about your fastapi server as in json file

## Build Docker Image

Build the Docker Image

    docker build -t myimage .

Test on your local

    docker run -p 8000:80 myimage

    Then check on http://localhost:8000/docs

Start the Docker Container¶

    docker run -d --name mycontainer -p 80:80 myimage
    
    Now you can go to http://localhost:80/docs

## Push the image to Docker Hub:

    docker login
    
    docker push your-username/your-app-name:tag

## To use the uploaded image

    docker pull your-username/your-app-name:tag

    docker run -p 80:80 your-username/your-app-name:tag

## Add __init__.py 

Adding __init__.py file to add modules stable_diffusion_app.ml