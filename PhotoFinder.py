print("⭕️开始")
from deepface import DeepFace

# 比较两张图片是否是同一个人
result = DeepFace.verify("test_photos/111.jpg", "test_photos/b3.jpg", model_name="Facenet",distance_metric="cosine")#threshold=0.4
print(result)  # 输出 {'verified': True/False, 'distance': 距离, 'model': 模型名称, 等}
# 分析图片中的面部信息
# analysis = DeepFace.analyze(img_path="test_photos/v3.jpg", actions=[ 'gender', 'race'],detector_backend="mtcnn")
# print(analysis)  # 输出各项分析结果

print("✅完成!")