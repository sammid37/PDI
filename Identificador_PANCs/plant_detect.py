# Script para Detecção das classes de plantas

import os
import sys
import torch
import numpy as np

from ultralytics import YOLO
from typing import List, Tuple, Optional, Union
from ultralytics.engine.results import Results

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

class detectorPlantas:
  def __init__(
      self,
      path_dir: Optional[str] = None,
      device: Union[str, torch.device, None] = None
    ) -> None:
      if path_dir is None:
        self.path_dir = ""
      else:
        self.path_dir = path_dir

      if self.path_dir.endswith(".pt"):
        self.checkpoint_path = self.path_dir
      else:
        self.checkpoint_path = os.path.join(
          self.path_dir, "yolov8n_plant_detection.pt"
        )

      if isinstance(device, torch.device):
        self.device = device
      elif device in ["gpu", "cuda", None] and torch.cuda.is_available():
        self.device = torch.device("cuda")
      else:
        self.device = torch.device("cpu")

      self.__load_model__()

  def detect(self, image_rgb: np.ndarray) -> List[Tuple[int, Tuple[int, int, int, int], float]]:
    h, w = image_rgb.shape[:2]

    results: Results = self.model.predict(
      image_rgb, device=self.device, imgsz=640, rect=True
    )[0]  # Pegue o primeiro item da lista, que é o objeto Results
    
    detections = []
    
    # results.boxes.xyxy contém as coordenadas das caixas delimitadoras
    # results.boxes.cls contém as classes
    # results.boxes.conf contém as confianças
    for det, cls, conf in zip(results.boxes.xyxy, results.boxes.cls, results.boxes.conf):
      # Move o tensor para a CPU e o converte para um array numpy
      det = det.cpu().numpy()

      # Convertendo para o formato normalizado (x_centro, y_centro, largura, altura)
      x_centro = (det[0] + det[2]) / (2 * w)
      y_centro = (det[1] + det[3]) / (2 * h)
      largura = (det[2] - det[0]) / w
      altura = (det[3] - det[1]) / h

      # Adicionando à lista de detecções
      det_norm = np.array([x_centro, y_centro, largura, altura], dtype=np.float32)
      
      detections.append((int(cls), tuple(det_norm), float(conf)))
      # detections.append((int(cls), tuple(det_norm), float(conf)))

    return detections

  def __load_model__(self):
    self.model = YOLO(self.checkpoint_path, task="detect")
