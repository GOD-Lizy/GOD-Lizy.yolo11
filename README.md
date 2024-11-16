👋 Hi, I’m @GOD-Lizy
👀 I’m interested in Deep Learning
🌱 I’m currently learning using of YOLO SSD DETR LSTM and various models
💞️ I’m looking to collaborate on all people who are intrested in how to use AI but not its Underlying code
📫 How to reach me Email 3312553683@qq.com Tel 15631887855 From TianJin Uniiversity Welcome to contact with me
😄 Pronouns: GOD-Lizy
⚡ Fun fact: ...
Description: This project contains a total of 6591 images and YOLO format annotation files. You can use my dataset (roboflow website: http://app.roboflow.com/godlizy/arrester-external-defect-dataset/1 ）Of course, you can also use your own dataset (YOLO format with images and annotated files, can be converted to GPT or Claud if not converted).
This project uses your own dataset for YOLO11 training steps:
1. Import your dataset
2. Ultralytics/cfg/defaulty.yaml. Modify your training parameters, I suggest you modify the epochs batch imgsz device workers optimizer dropout
3... ltralytics/cfg/models/11/myyolo11.yaml (create a new YAML file modeled after yolo11.yaml) Modify nc (number of dataset categories)
4. Establish myyolo128 (path (dataset type), train (sub path), val (sub path), test (sub path), and add category after names.
5. Pay attention to downloading pre trained weights from the ultralytics official website,
6. Create a train.exe
from ultralytics import YOLO
if name == '__main__':
model = YOLO("C:\\Users\\lzy\\PycharmProjects\\YOLO11（lunwen）\\ultralytics-main\\ultralytics\\cfg\\models\\11\\myyolo11.yaml")
# Load a COCO-pretrained YOLO11n model
model = YOLO("C:\\Users\\lzy\\PycharmProjects\\YOLO11（lunwen）\\yolo11n.pt")
# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="C:\\Users\\lzy\\PycharmProjects\\YOLO11（lunwen）\\ultralytics-main\\ultralytics\\cfg\\datasets\\mycoco128.yaml", epochs=200, imgsz=640)
# Run inference with the YOLO11n model on the 'bus.jpg' image
results = model.val()
As mentioned above, you need to input the absolute path of myyolo11.yaml in the third line of the code and the absolute path of yolo11n.pt with pre trained weights in the fifth line. On the eighth line, enter the absolute path of mycoc128, followed by the number of rounds and image size
more......
if you want to learn more about process of model please feel free to contact with me 
I am looking forward to replying quetions about AI
