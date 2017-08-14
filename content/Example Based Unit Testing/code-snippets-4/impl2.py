class PhysicalInfo(object):

    def set_height(self, height):
        assert isinstance(height, int), "height should be an integer"
        assert height >= 17 and height <= 84, "height should be an integer between 17 and 84"
        self.height = height

