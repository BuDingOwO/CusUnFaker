from PIL import Image
import os


def BuildImg():
    BasePath = os.path.dirname(os.path.abspath(__file__))
    InPut = BasePath + "/源文件/"
    OutPut = BasePath + "/成品/"
    files = os.listdir(BasePath + "/" + "源文件")
    WaterMark = Image.open(BasePath + "/src/logo.png")

    print(files)
    if len(files) > 1:
        for FileName in files:
            Img = Image.open(InPut + FileName)
            Height = Img.height
            Width = Img.width
            Img.paste(WaterMark, (Height - 50, Width - 50, Height, Width))
            Img.save(OutPut + FileName)
            print("Good x 2")
    if len(files) == 1:
        Img = Image.open(InPut + files[0])
        Height = Img.height
        Width = Img.width
        print(f"Height: {Height},Width: {Width}")
        Img.paste(WaterMark, (Height - 250, Width - 150))
        Img.save(OutPut + files[0])
        print("Good")


BuildImg()
