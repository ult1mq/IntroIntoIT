import sys
import os
import torch
from PIL import Image
import numpy as np
from facenet_pytorch import MTCNN, InceptionResnetV1

# Пути к фотографиям
KNOWN_PATH   = "known.jpg"
UNKNOWN_PATH = "unknown.jpg"

# Проверка наличия
for path in (KNOWN_PATH, UNKNOWN_PATH):
    if not os.path.isfile(path):
        print(f"❌ Файл не найден: {path}")
        sys.exit(1)

# Инициализация детектора лиц и модели эмбеддингов
mtcnn = MTCNN(keep_all=False, device="cpu")
resnet = InceptionResnetV1(pretrained="vggface2").eval().to("cpu")

def get_embedding(path: str):
    """Возвращает эмбеддинг 512-размерного вектора для одного лица."""
    img = Image.open(path).convert("RGB")
    # Детектим и вырезаем лицо (размер 160×160)
    face = mtcnn(img)
    if face is None:
        print(f"❌ Лицо на {path} не обнаружено.")
        sys.exit(1)
    # Получаем эмбеддинг (1×512)
    with torch.no_grad():
        emb = resnet(face.unsqueeze(0))
    return emb[0].cpu().numpy()

# Получаем эмбеддинги двух фото
emb1 = get_embedding(KNOWN_PATH)
emb2 = get_embedding(UNKNOWN_PATH)

# Считаем Евклидово расстояние
distance = np.linalg.norm(emb1 - emb2)

# Порог для FaceNet обычно ~1.0
match = distance < 1.0

# Выводим результат
print("\n🔍 Результат сравнения через FaceNet:")
print(f"  ➤ Совпадение: {'✅ Да' if match else '❌ Нет'}")
print(f"  ➤ Расстояние: {distance:.4f} (меньше 1.0 → совпадение)\n")
