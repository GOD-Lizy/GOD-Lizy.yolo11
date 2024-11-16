from ultralytics import YOLO
if __name__ == '__main__':
  model = YOLO("C:\\Users\\lzy\\PycharmProjects\\YOLO11（lunwen）\\ultralytics-main\\ultralytics\\cfg\\models\\11\\myyolo11.yaml")
# Load a COCO-pretrained YOLO11n model
  model = YOLO("C:\\Users\\lzy\\PycharmProjects\\YOLO11（lunwen）\\yolo11n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
  results = model.train(data="C:\\Users\\lzy\\PycharmProjects\\YOLO11（lunwen）\\ultralytics-main\\ultralytics\\cfg\\datasets\\mycoco128.yaml", epochs=200, imgsz=640)
# Run inference with the YOLO11n model on the 'bus.jpg' image
  results = model.val()
