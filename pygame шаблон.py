from pygame import*
WIDTH,HEIGHT = 700,500
FPS = 60
clock = time.Clock()
window = display.set_mode((WIDTH,HEIGHT ))
display.set_caption("Доганьлки")

bg_image = image.load("background.png")
bg = transform.scale(bg_image,(WIDTH,HEIGHT ))


while True:
    for e in event.get():
        if e.type == QUIT:
            quit()

    window.blit(bg,(0,0))
    display.update()
    clock.tick(FPS)




