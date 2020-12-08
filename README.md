# person_detection_logistic_regression

Project to detect pedestrian from a video using logistic regression with neural networks

## Prerequisites

you have to have previously installed

[Python 3.7](www.python.org)

[Pip 3](https://pip.pypa.io/en/stable/installing/)

## Requierements

[Virtual Enviroment](https://docs.python.org/3/tutorial/venv.html)

## Installation

```bash
git clone https://github.com/DavidBanda/person_detection_logistic_regression
```

```bash
python3 -m venv person_detection_logistic_regression
```

```bash
person_detection_logistic_regression\Scripts\activate.bat
```

```bash
cd person_detection_logistic_regression
```

```bash
pip3 install -r requirements.txt
```

## Run project

```bash
python run.py
```

You can access it opening in your browser [index.html](https://github.com/DavidBanda/person_detection_logistic_regression/blob/main/index.html)

You need to write down in the text field an absolute path to a video to your local machine, you can use the videos that are in the project: person_detection_logistic_regression/ai_backend/static/video

![alt text](https://github.com/DavidBanda/person_detection_logistic_regression/blob/main/prevs/path2.png)

## Create you own dataset to detect objects/animals/persons

### Image dataset

You need images of the object you want to detect and images in which the object is not. You can use this site [Kaggle](kaggle.com/) to download datasets.
Once you download images with the object you want to detect, you need to tag the images with their respective name, for example we tag our images with the name 'person' next to a number and 'obj' next to a number for images that do not appear a pedestrian. You can check it in the project at the route `person_detection_logistic_regression/ai_backend/static/images`
To facilitate this, we create a file to rename all files in a folder, the file its in `/Users/davidbanda/Coding/person_detection_logistic_regression/ai_backend/utils/rename_files` inside we only need to change the variable `path` to the path where we have the images that we want to change the name. We also need change the variable `name` for the name that we will use plus the number we gonna add to each image, but this number is adding automatically.
