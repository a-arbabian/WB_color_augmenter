from . import WBEmulator as wbAug
import numpy as np 
import random
from PIL import Image

class WB_Aug_Transform(object):
    """Randomly change the WB & finishing style of input img.
    - There are 10 styles in total (see self.wb_photo_finishing)     
    """
    def __init__(self):
        self.wb_photo_finishing =  ['_F_AS', '_F_CS', '_S_AS', '_S_CS',
                                    '_T_AS', '_T_CS', '_C_AS', '_C_CS',
                                    '_D_AS', '_D_CS']
        self.style = random.choice(self.wb_photo_finishing)
        self.wbAug = wbAug.WBEmulator(self.style)
        self.out_num = 1

    def __call__(self, img):
        """
        Args:
            img (PIL Image): Input RGB image. Must be uint8 [0, 255]

        Returns:
            PIL Image: WB augmented RGB image as uint8 [0, 255] 
        """
        img = np.asarray(img)
        out_img, _ = self.wbAug.generateWbsRGB(img, self.out_num)
        out_img = out_img.squeeze(-1) * 255
        out_img = Image.fromarray(out_img.astype(np.uint8))
        return out_img
    
    def __repr__(self):
        format_string = self.__class__.__name__ 
        return format_string