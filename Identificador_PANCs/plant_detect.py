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
    pass

  def detectar(self, image_rgb: np.ndarray) -> List[Tuple[int, Tuple[int, int, int, int], float]]:
    pass

  def __load_model__(self):
      self.model = YOLO(self.checkpoint_path, task="detect")
