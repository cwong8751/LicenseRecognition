# LicenseRecognition
A license plate recognition system powered by YOLO. 

### Current state
Trained YOLO v8 model via Ultralytics and a dataset from roboflow. The model knows a license plate is a license plate but still doesn't know the text quite well. 


``` yolo_training ``` contains training code for the yolo model 
``` recognition.ipynb``` contains the code use to actually perform the license recognition
``` best.pt ``` contains the trained model ready to be used by ```recognition.ipynb```
