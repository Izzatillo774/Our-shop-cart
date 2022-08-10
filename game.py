from turtle import *
import pygame

pygame.init()
fon = pygame.display.set_mode((1600, 1043))

pygame.display.set_caption("Center")

bg = pygame.image.load('zed.jpg')

walkRight = [pygame.image.load('right1.png'), pygame.image.load('right2.png'), pygame.image.load('right3.png'),
             pygame.image.load('right4.png'), pygame.image.load('right5.png'), pygame.image.load('right6.png')]

walkLeft = [pygame.image.load('left1.png'), pygame.image.load('left2.png'), pygame.image.load('left3.png'),
            pygame.image.load('left4.png'), pygame.image.load('left5.png'), pygame.image.load('left6.png')]

zombie_R = [pygame.image.load('z_right1.png'), pygame.image.load('z_right2.png'),
            pygame.image.load('z_right3.png')]

zombie_L = [pygame.image.load('z_left1.png'), pygame.image.load('z_left2.png'),
            pygame.image.load('z_left3.png')]

clock = pygame.time.Clock()

x = -180
y = 325
width = 590
height = 842
speed = 10

x_z = 1150
y_z = 310
width_z = 596
height_z = 842

isJump = False
jumpCount = 10

left = False
left_z = False
right = False
right_z = False
animCount = 0
lastMove = "right"
zombie_count = 0
speed_zombie = 10


class Gun():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def drawWindow():
    global animCount
    global zombie_count
    fon.blit(bg, (0, 0))

    if animCount + 1 >= 30:
        animCount = 0

    if zombie_count + 1 >= 30:
        zombie_count = 0

    if left:
        fon.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        fon.blit(walkRight[animCount // 5], (x, y))
        animCount += 1

    if left_z:
        fon.blit(zombie_L[zombie_count // 10], (x_z, y_z))
        zombie_count += 1

    if right_z:
        fon.blit(zombie_R[zombie_count // 10], (x_z, y_z))
        zombie_count += 1

    for bullet in bullets:
        bullet.draw(fon)

    pygame.display.update()


run = True
bullets = []
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 1780 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_KP4] and x_z > 5:
        lastMove = "left"
        x_z -= speed_zombie
        left_z = True
        right_z = False

    if keys[pygame.K_KP6] and x_z < 2800 - width_z - 5:
        lastMove = "right"
        x_z += speed_zombie
        left_z = False
        right_z = True

    if keys[pygame.K_f]:
        if lastMove == "right":
            facing = 2
        else:
            facing = -2

        if len(bullets) < 10 and lastMove == "right":
            bullets.append(Gun(round(x + width // 1.2),
                                 round(y + height // 2),
                                 5, (255, 0, 0), facing))
        else:
            bullets.append(Gun(round(x + width // -100),
                                 round(y + height // 2),
                                 5, (255, 0, 0), facing))

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] and x < 1780 - width - 5:
        x += speed
        left = False
        right = True
        lastMove = "right"
    else:
        left = False
        right = True
        animCount = 0

    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    drawWindow()

pygame.quit()
