import pygame
import time
import math

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước màn hình
screen_width = 1000
screen_height = 751
screen = pygame.display.set_mode((screen_width, screen_height))

GREY = (120,120,120)
WHITE = (255,255, 255)
BLACK = (0,0,0)
BLUE = (135,206,250)
PINK = (255,192,203)
GREEN = (175,238,238)
KIM = (0,100,0)
WORD= (0,128,128)
BLUEE = (173,216,230)
TEAL = (0,128,128)
PINKK =(255,0,255)
# Load ảnh nền
background = pygame.image.load("111.jpg").convert()

font = pygame.font.SysFont('sans',35)
text_1 = font.render(' +', True, PINKK)
text_2 = font.render(' -', True, PINKK)
text_3 = font.render(' Start', True, PINKK)
text_4 = font.render(' Reset', True, PINKK)
text_5 = font.render('-------Wake up, my friend------',True, WORD)
text_6 = font.render('Turn off' , True, PINKK)

running = True

total = 0

start = False

total_secs = 0

alpha = 0.0

sound = pygame.mixer.Sound("chuong.mp3")

# Chống tốn bộ nhớ 
clock = pygame.time.Clock()

# Vòng lap game loop
while running:
    clock.tick(60)
    pygame.display.set_caption("Alarm")
    # ảnh backgroud
    screen.blit(background, (0, 0))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Đồng hồ
    pygame.draw.circle(screen, BLACK, (750,270),200,2)
    #pygame.draw.circle(screen, GREEN, (750,270),198)
    pygame.draw.circle(screen, BLACK, (750,270),5)


    # Cộng Cộng Start
    pygame.draw.rect(screen, BLUE, (100,70,70,50))
    screen.blit(text_1, (120,70))
    pygame.draw.rect(screen, BLUE, (200,70,70,50))
    screen.blit(text_1, (220,70))
    pygame.draw.rect(screen, BLUE, (350,70,100,50))
    screen.blit(text_3, (350,70))

    # Thời gian ở giữa
    pygame.draw.rect(screen, BLUE, (100,135,70,50))
    pygame.draw.rect(screen, BLUE, (200,135,70,50))
    pygame.draw.rect(screen , BLUE, (350,135,100,50))
    screen.blit(text_6, (350,135))

    # Trừ Trừ resert
    pygame.draw.rect(screen, BLUE, (100,200,70,50))
    screen.blit(text_2, (120,200))
    pygame.draw.rect(screen, BLUE, (200,200,70,50))
    screen.blit(text_2, (220,200))
    pygame.draw.rect(screen, BLUE, (350,200,100,50))
    screen.blit(text_4, (350,200))

    # Thanh dưới
    pygame.draw.rect(screen, BLUE, (50,280,400,50))
    screen.blit(text_5, (50,280))

    # Kiểm tra sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Nhấn chuột cộng cộng start
            if (100 < mouse_x < 170) and (70 < mouse_y < 120):
                total_secs += 60
            if (200 < mouse_x < 270) and (70 < mouse_y < 120):
                total_secs += 1
            if (350 < mouse_x < 450) and (70 < mouse_y < 120):
                start = True
                total = total_secs
            # Nhâns chuột trừ trừ resert
            if (100 < mouse_x < 170) and (200 < mouse_y < 250):
                total_secs -= 60
            if (200 < mouse_x < 270) and (200 < mouse_y < 250):
                total_secs -=1
            if (350 < mouse_x < 450) and (200 < mouse_y < 250):
                total = 0
                total_secs =0
                start = False
            # Nhấn chuột dừng âm báo thức
            if (350 < mouse_x < 450) and (135 < mouse_y < 185):
                pygame.mixer.pause()
                total = 0
                total_secs =0
                start = False


    if start:
        total_secs -= 1
        if total_secs == 0:
            start = False
            pygame.mixer.Sound.play(sound)
        time.sleep(1)
    
    if total_secs < 0 and start == True:
        total_secs = 0
    mins = int(total_secs/60)
    secs = total_secs - mins*60
    minss = ' ' + str(mins)
    secss = ' ' + str(secs)
    text_mins = font.render(minss, True, TEAL)
    if total_secs >= 0:
        text_sexs = font.render(secss , True ,TEAL)
    screen.blit(text_mins, (110,138))
    screen.blit(text_sexs, (210,138))
    
    if total != 0 and start == True:
        # In thanh cuối thụt dần
        n = int(400*(total_secs/total))
        pygame.draw.rect(screen , BLUEE  ,(50,280,n,50))
        if (total > 0) and (total_secs > 0):
            # Kim đồng hồ quay
            anpha = math.pi*(total_secs/total)*2
            if alpha > 0:
                x = int(750 + 200*(math.sin(anpha)))
                y = int(270 + 200*(math.cos(anpha)))
                pygame.draw.line(screen,KIM,(750,270), (x,y))
            else:
                x = int(750 - 200*(math.sin(anpha)))
                y = int(270 - 200*(math.cos(anpha)))
                pygame.draw.line(screen,KIM,(750,270), (x,y))
    
    # Cập nhật màn hình
    pygame.display.update()

pygame.quit()