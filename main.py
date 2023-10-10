from pygame import*#підключвємо модуль pygame

WIDTH,HEIGHT = 700,500#створюємо зміну з шириною вікна для подальшого використання
FPS = 60#задаємо кількісь кадряв за 1сек
clock = time.Clock()#підключаємо час
window = display.set_mode((WIDTH,HEIGHT ))#створюємо вікно, розмір вікна
display.set_caption("Доганялки")#назва вікна


class Player(sprite.Sprite):#створюємо клас
    def __init__(self,sprite_image,x,y):#створюємо конструктор класу
        super().__init__()#робимо його глобальним
        self.image = transform.scale(image.load(sprite_image),(65,65))#обрізаємо зображеня
        self.rect = self.image.get_rect()#дістаємо кординати обє'кта
        self.rect.x = x#кординати х
        self.rect.y = y#кординати y
        self.speed = 5#встановлюємо майбутню швикість спрайта
    
    def draw(self,window):#створюємо функцію draw
        window.blit(self.image,self.rect)#створюємо хітбокс персонажа


bg_image = image.load("background.png")#завантажуємо картинку"ФОН"
bg = transform.scale(bg_image,(WIDTH,HEIGHT ))#змінюємо його під розмір екрану

player_1 = Player("sprite1.png",100,100)#створюємо спрайта 1
player_2 = Player("sprite2.png",200,200)#створюємо спрайта 2

player_1.draw(window)


while True:#ігровий цикл
    for e in event.get():#перевірка чи ми закриваємо вікно
        if e.type == QUIT:
            quit()


    keys = key.get_pressed()#створюємо зміну в яку буде записуватись ключі від кнопок
    if keys[K_UP] and player_2.rect.y > 0:#підключаємо рух до другого спрайта
        player_2.rect.y -= 5
    
    if keys[K_DOWN] and player_2.rect.bottom < HEIGHT:#підключаємо рух до другого спрайта
        player_2.rect.y += 5

    if keys[K_LEFT] and player_2.rect.x > 0:#підключаємо рух до другого спрайта
        player_2.rect.x -= 5

    if keys[K_RIGHT] and player_2.rect.right < WIDTH:#підключаємо рух до другого спрайта
        player_2.rect.x += 5
#перший гравець синій
    if keys[K_w] and player_1.rect.y > 0:#підключаємо рух до другого спрайта
        player_1.rect.y -= 5
    
    if keys[K_s] and player_1.rect.bottom < HEIGHT:#підключаємо рух до другого спрайта
        player_1.rect.y += 5

    if keys[K_a] and player_1.rect.x > 0:#підключаємо рух до другого спрайта
        player_1.rect.x -= 5

    if keys[K_d] and player_1.rect.right < WIDTH:#підключаємо рух до другого спрайта
        player_1.rect.x += 5


    window.blit(bg,(0,0))
    player_1.draw(window)
    player_2.draw(window)



    display.update()#оновленя екрану
    clock.tick(FPS)#частота оновленя екрану в секундах

    




