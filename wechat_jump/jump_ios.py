from PIL import ImageGrab


def screen_shot():
    path = 'img/1.png'
    img = ImageGrab.grab()
    img.save(path, 'png')

