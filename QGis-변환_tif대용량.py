import os
from qgis.core import (
    QgsProject,
    QgsRasterLayer,
    QgsMapSettings,
    QgsMapRendererCustomPainterJob
)
from PyQt5.QtGui import QImage, QPainter, QColor
from PyQt5.QtCore import QSize

# 입력 및 출력 디렉터리 설정
input_dir = r"D:\dir"
output_dir = r"D:\dir"

# 출력 폴더가 없으면 생성
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# TIFF 파일 목록 순회
for filename in os.listdir(input_dir):
    if filename.endswith(".tif") or filename.endswith(".tiff"):
        input_file_path = os.path.join(input_dir, filename)
        output_file_name = os.path.splitext(filename)[0] + ".png"
        output_file_path = os.path.join(output_dir, output_file_name)

        # 레이어 불러오기
        layer = QgsRasterLayer(input_file_path, filename)
        if not layer.isValid():
            print(f"Failed to load {input_file_path}")
            continue

        # QgsMapSettings 설정
        map_settings = QgsMapSettings()
        map_settings.setLayers([layer])
        map_settings.setExtent(layer.extent())
        map_settings.setOutputSize(QSize(layer.width(), layer.height()))

        # 이미지 생성 및 렌더링
        image = QImage(QSize(layer.width(), layer.height()), QImage.Format_ARGB32)
        image.fill(QColor(255, 255, 255, 0))  # 투명 배경
        painter = QPainter(image)
        render = QgsMapRendererCustomPainterJob(map_settings, painter)
        render.start()
        render.waitForFinished()

        painter.end()

        # 이미지 저장
        image.save(output_file_path)
        print(f"Saved image: {output_file_path}")

        # 레이어 제거
        QgsProject.instance().removeMapLayer(layer)
