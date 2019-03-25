import pygame
import random
import sys

# 根据背景图大小,设置游戏屏幕大小
WIDTH, HEIGHT = 1024, 576
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('dinner invitation')


# 添加文本信息
def title(text, screen, scale, color=(255, 153, 51)):
    font = pygame.font.SysFont('SimHei', 27)
    textRender = font.render(text, True, color)
    # 初始化文字的坐标
    screen.blit(textRender, (WIDTH / scale[0], HEIGHT / scale[1]))


# 按钮
def button(text, x, y, w, h, color, screen, color_text):
        pygame.draw.rect(screen, color, (x, y, w, h))
        font = pygame.font.SysFont('SimHei', 20)
        textRender = font.render(text, True, color_text)
        textRect = textRender.get_rect()
        textRect.center = ((x+w/2), (y+h/2))
        screen.blit(textRender, textRect)


# 生成随机的位置坐标
def get_random_pos():
        x, y = random.randint(20, 620), random.randint(20, 460)
        return x, y


# 点击答应后显示的页面
def show_like_interface(screen):
    screen.fill((255, 255, 255))
    background1 = pygame.image.load('dinner.png').convert()
    screen.blit(background1, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


# 点击不答应按钮后显示的页面
def show_unlike_interface(screen):
    screen.fill((255, 255, 255))
    background_1 = pygame.image.load('thanos.jpg').convert()
    screen.blit(background_1, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


def main():
    num = 0
    pygame.init()
    clock = pygame.time.Clock()
    # 添加背景音乐
    # pygame.mixer.music.load('214_2.mp3')
    # pygame.mixer.music.play(-1, 40)
    # pygame.mixer.music.set_volume(0.5)
    # 设置不同意按钮属性
    unlike_pos_x = 130
    unlike_pos_y = 375
    unlike_pos_width = 450
    unlike_pos_height = 55
    unlike_color = (115, 76, 243)
    # 设置同意按钮属性
    like_pos_x = 130
    like_pos_y = 280
    like_pos_width = 450
    like_pos_height = 55
    like_color = (115, 76, 243)

    running = True
    while running:
        # 填充窗口
        screen.fill((255, 255, 255))
        # 添加背景图
        background = pygame.image.load('dinner2.jpeg').convert()
        screen.blit(background, (0, 0))

        # 获取鼠标坐标
        pos = pygame.mouse.get_pos()
        if pos[0] < unlike_pos_x + unlike_pos_width + 5 and pos[0] > unlike_pos_x - 5 and pos[1] < unlike_pos_y + unlike_pos_height + 5 and pos[1] > unlike_pos_y - 5:
            while True:
                if num > 5:
                    break
                num += 1
                unlike_pos_x, unlike_pos_y = get_random_pos()
                if pos[0] < unlike_pos_x + unlike_pos_width + 5 and pos[0] > unlike_pos_x - 5 and pos[1] < unlike_pos_y + unlike_pos_height + 5 and pos[1] > unlike_pos_y - 5:
                    continue
                break

        # 设置标题及按钮文本信息
        title('1.Will you go for dinner on Friday at 9 pm', screen, scale=[8, 3])
        button('A.Yes, I will.', like_pos_x, like_pos_y, like_pos_width, like_pos_height, like_color, screen, (255, 255, 255))
        # 设置小套路文本
        if num < 6:
            button('B.Sorry, I cant', unlike_pos_x, unlike_pos_y, unlike_pos_width, unlike_pos_height, unlike_color, screen, (255, 255, 255))
        if num > 5:
            button('B.Yes, I will.', unlike_pos_x, unlike_pos_y, unlike_pos_width, unlike_pos_height, unlike_color, screen, (255, 255, 255))
        # 设置套路文本
        if num == 1:
            button('Hint: just click on the button', unlike_pos_x, unlike_pos_y - 50, unlike_pos_width, unlike_pos_height, (255, 255, 255), screen, (192, 0, 0))
        if num == 2:
            button('Are you not coming?', unlike_pos_x, unlike_pos_y - 50, unlike_pos_width, unlike_pos_height, (255, 255, 255), screen, (192, 0, 0))
        if num == 3:
            button('Are you sure about this?', unlike_pos_x, unlike_pos_y - 50, unlike_pos_width, unlike_pos_height, (255, 255, 255), screen, (192, 0, 0))
        if num == 4:
            button('You really dont want to go for dinner', unlike_pos_x, unlike_pos_y - 50, unlike_pos_width, unlike_pos_height, (255, 255, 255), screen, (192, 0, 0))
        if num == 5:
            button('Ah, you almost made it', unlike_pos_x, unlike_pos_y - 50, unlike_pos_width, unlike_pos_height, (255, 255, 255), screen, (192, 0, 0))
        if num == 6:
            button('Just give up', unlike_pos_x, unlike_pos_y - 50, unlike_pos_width, unlike_pos_height, (255, 255, 255), screen, (192, 0, 0))

        # 点击套路按钮
        if num > 5:
            if pos[0] < unlike_pos_x + unlike_pos_width + 5 and pos[0] > unlike_pos_x - 5 and pos[1] < unlike_pos_y + unlike_pos_height + 5 and pos[1] > unlike_pos_y - 5:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    show_unlike_interface(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 点击同意按钮
        if pos[0] < like_pos_x + like_pos_width + 5 and pos[0] > like_pos_x - 5 and pos[1] < like_pos_y + like_pos_height + 5 and pos[1] > like_pos_y - 5:
            if event.type == pygame.MOUSEBUTTONDOWN:
                show_like_interface(screen)

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


main()