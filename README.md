# LicenseRecognition
A license plate recognition system powered by YOLO. 


##### About this project

This project uses YOLO v5 combined with a video stream to identify vehicle license plates on the move. 


##### How to use

1. Install the packages

<code>pip install numpy opencv-python torch torchvision matplotlib</code>


2. I am using YOLO, we need to clone YOLO.
~~~
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
~~~


Dataset used is from: https://www.kaggle.com/datasets/andrewmvd/car-plate-detection/data

Dataset is stored under /dataset 

/dataset has two folders: annotations and images. Annotations contains the bounding box files for each image, the images folder contains all images. 



~~~
### BibTeX

[@misc](https://www.kaggle.com/misc){make ml,  
title={Car License Plates Dataset},  
url={[https://makeml.app/datasets/cars-license-plates}](https://makeml.app/datasets/cars-license-plates%7D),  
journal={Make ML}}

### License

Public domain

### Splash banner

Photo by  [Gunnar Bjarki](https://unsplash.com/@gunnarbjarkiii?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)  on  [Unsplash](https://unsplash.com/photos/wwt1jjX1OdM)
~~~

