import moondream as md
from typing import Union
from PIL import Image

class mdHelper:
    def __init__(self, api_key = None):
        # Initialize for Moondream Cloud
        self.model = md.vl(api_key=api_key)
        
    def _load_image(self, image: Union[Image.Image, str]) -> Image.Image:
        """
    Load an image from a file path or use a PIL Image directly.
    
    Args:
        image: Either a PIL Image object or a string path to an image file
        
    Returns:
        A PIL Image object
        """
        if isinstance(image, str):
        # If image is a file path, open it with PIL
            return Image.open(image)
        elif isinstance(image, Image.Image):
        # If image is already a PIL Image, return it
            return image
        else:
            raise TypeError("Expected image to be a PIL Image or a file path string")
        
    def describe(self, image: Union[Image.Image, str], detail: str = "normal") -> str:
        img = self._load_image(image)
        caption = self.model.caption(img, length= detail)["caption"]
        return caption
    
    def query(self, image: Union[Image.Image, str], question: str) -> str:
        img = self._load_image(image)
        answer = self.model.query(img, question)["answer"]
        return answer
    
    def detect(self, image: Union[Image.Image, str], objects: str)->str:
        img = self._load_imag(image)
        answer = self.model.detect(img, objects)["objects"]
        return answer
    