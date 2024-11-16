from ultralytics import YOLO
import cv2

# 1. 加载模型
model = YOLO("C:\\Users\\lzy\\PycharmProjects\\YOLO11（lunwen）\\ultralytics-main\\runs\detect\\train4\\weights\\best.pt")  # 加载训练好的模型

# 2. 预测图片
image_path = "C:\\Users\\lzy\\PycharmProjects\\YOLO11（lunwen）\\dataset\\images\\train\\0b6bf41a6249b217eb5842_jpg.rf.e051c5ed250652bf2e508006978b1b28.jpg"  # 替换为你的图片路径
results = model(image_path)  # 预测

# 3. 在图片上绘制预测结果
for result in results:
    # 获取预测框、置信度和类别
    boxes = result.boxes.xyxy.cpu().numpy()  # 预测框坐标
    confidences = result.boxes.conf.cpu().numpy()  # 置信度
    class_ids = result.boxes.cls.cpu().numpy()  # 类别ID

    # 读取原始图片
    img = cv2.imread(image_path)

    # 遍历每个检测结果并绘制
    for box, confidence, class_id in zip(boxes, confidences, class_ids):
        x1, y1, x2, y2 = map(int, box)  # 转换为整数坐标

        # 绘制边界框
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # 添加类别标签和置信度
        label = f'Class {int(class_id)}: {confidence:.2f}'
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 保存结果图片
    cv2.imwrite('result.jpg', img)

# 4. 打印预测结果
for r in results:
    print("Predictions:", r.boxes)  # 打印预测框信息
    print("Classes:", r.boxes.cls)  # 打印类别
    print("Confidences:", r.boxes.conf)  # 打印置信度
