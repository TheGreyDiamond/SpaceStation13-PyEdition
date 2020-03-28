from PIL import Image

class GIFplayer():
    def __init__(self, filename):
        self.filename = filename
        self.image = Image.open(filename)
        self.frames = []

    def extractFrames(self):
        image = self.image
        pal = image.getpalette()
        base_palette = []
        for i in range(0, len(pal), 3):
            rgb = pal[i:i+3]
            base_palette.append(rgb)

        print(base_palette)
test = GIFplayer(".\\opening.gif")
test.extractFrames()