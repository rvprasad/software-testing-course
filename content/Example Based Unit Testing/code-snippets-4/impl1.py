class PhysicalInfo(object):

    def set_height(self, height):
        if not isinstance(height, int):
            raise TypeError("height should be an integer")
        if height < 17 or height > 84:
            raise ValueError("height should be an integer between 17 and 84")
        self.height = height
