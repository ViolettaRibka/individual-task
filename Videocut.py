import cv2
import os

# 1. Запрашиваем путь к видеофайлу
video_path = input("Введите путь к видеофайлу: ").strip()

# Проверяем существование файла
if not os.path.isfile(video_path):
    print("Файл не найден. Проверьте путь.")
    exit()

# 2. Получаем директорию и имя файла
folder = os.path.dirname(video_path)
filename = os.path.basename(video_path)
name_without_ext = os.path.splitext(filename)[0]

# 3. Открываем видео
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Не удалось открыть видеофайл.")
    exit()

frame_number = 0

# 4. Считываем видео покадрово
while True:
    success, frame = cap.read()
    if not success:
        break  # видео закончилось

    frame_number += 1

    # Формируем имя файла
    output_filename = f"{name_without_ext}-кадр-{frame_number}.png"
    output_path = os.path.join(folder, output_filename)

    # Сохраняем кадр
    cv2.imwrite(output_path, frame)

    print(f"Сохранён кадр: {output_filename}")

cap.release()
print("Готово! Все кадры нарезаны и сохранены успешно.")