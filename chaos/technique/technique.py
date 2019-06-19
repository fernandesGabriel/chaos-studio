from abc import ABC, abstractmethod
from PIL import Image as Canvas
from trace import Trace


class Technique(ABC):
    def __init__(self, trace: Trace):
        self.trace = trace

    @abstractmethod
    def draw_on(self, canvas: Canvas):
        pass
