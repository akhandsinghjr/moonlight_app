import moondream as md
from PIL import Image

class mdHelper:
    def __init__(self, api_key = None):
        # Initialize for Moondream Cloud
        self.model = md.vl(api_key=api_key)
        
    def describe(self, image: Union[Image.Image, str], detail: str = "normal") -> str:
        img = self._load_image{image}
        caption = self.model.caption(img, length= detail)["caption"]
        return caption
    
    def query(self, image: Union[Image.Image, str], question: str) -> str:
        img = self._load_image{image}
        answer = self.model.query(img, question)["answer"]
        return answer
    
    def detect(self, image: Union[Image.Image, str], objects: str)->str:
        img = self._load_image{image}
        answer = self.model.detect(img, objects)["objects"]
        return answer
    