# loblaw-digital

## Instructions

The project is built to be cross-platform application with frontend and backend written in React and python respectively. The frontend and backend needs to be run separately. 

checkout the project from github: `git clone https://github.com/stamzid/loblaw-digital.git`

### Backend

Backend is written in Python and takes advantage of python virtual environment setup. For this project `pipenv` environment has been used. Please refer to relevant instructions for operating system specific installation of `python 3.7` and `pipenv` environment.

Once installation complate, `cd` to `loblaw-digital/backend` folder and run the following chronologically:

- `pipenv shell`

- `pipenv install`

Once the python dependencies are installed change directory to root of this repo (loblaw-digital) and run the following command:

`uvicorn backend.app.main:app --host 0.0.0.0 --port 8000`

This will load the backend server.

### Frontend

Frontend is written in React.js and takes advantage of node package manager for maintaining and installing all necessary libraries. Please refer to the relevant official instructions for os specific installation of `node`, `npm` and `serve`.

Once the installation is completed then `cd` to frontend folder and run the following commands chronologically:

- `npm install`

- `npm run start` 

This will load a basic webpage that can be accessible from a webbrowser localhost at port `5000`.

User will have have to choose a file to upload and then click `upload` button to invoke the workflow. The output file will be stored in the following folder: `backend/outputs` and the filename would be the same as the input file.

## Assumptions & Design Decisions

- Only csv files are expected

- All the input rows under image columns must contain the absolute path of the file, as per task requirement documentation

- Structural Similarity Index is mainly used for comparing the images and score ranges from -1 to 1 with 1 being similar. At this point it doesn't make sense to force the score to `0` however since this was the business requirement what I decided to is add another comparison using Mean Square Error calculation and if that yielded `0` then for that specific comparison the program outputs `0` score.

- For any latest updates, pull the latest changes from github and reset frontend and backend.

- `Containerization` with docker was purposefully avoided to keep this program lightweight and keep the output file in the host machine easily.

- The problem was divided into multiple segments and individual segments were implemented first and then unittested. For example, as it can be seen from the structure there are separate modules for image comparing and file processing with corresponding unittests. 

- Python was chosen as the backend language because of the libraries it offers for image processing. The latest python libraries such as `FastAPI` is used in the project. The benchmark tests for this library matches the performance speed of NodeJS APIs.

- It is meant to deal with one file at a time but this project can be expanded to include multiple file. Someone else taking over this project should not have any problem maintaining this as long as they have basic understanding of React and are experienced in Python.
