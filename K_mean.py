import pygame 
import time
import math
from random import randint

def distance(p1,p2):
    return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0])+ (p1[1] - p2[1]) * (p1[1] - p2[1]))


pygame.init()

screen = pygame.display.set_mode((1000, 600))

BACKGROUD = (198, 226, 255)
BLACK = (0,0,0)

BAM = (119 ,136, 153)
CHU = (135, 206, 250)

font = pygame.font.SysFont('sans', 40)
fontt = pygame.font.SysFont('sans', 20)
text_1 = font.render('+', True, CHU)
text_2 = font.render('-', True, CHU )
text_run = font.render('Run', True,CHU)
text_random = font.render('Random', True, CHU)
text_algorithm = font.render('Algorithm',True, CHU)
text_reset = font.render('Reset',True, CHU)
running = True

clock = pygame.time.Clock()

K = 0
points = []
clusters = []
labels = []

COLORS = [(255,0,0), (0,255,0), (0,0,255), (147,153,35), (255,0,255), (0, 255,255), (255,125,25), (100,25,125), (55,155,65)]



while running:
    clock.tick(60)
    screen.fill(BACKGROUD)
    pygame.display.set_caption("Nguyễn Tuấn Thành K-mean")
    pygame.draw.rect(screen, BLACK,(25,25,600,550))
    pygame.draw.rect(screen, (232, 232, 232),(30,30,590,540))

    #cong
    pygame.draw.rect(screen, BAM , (700,25,40,40))
    screen.blit(text_1, (710,22))
    #tru
    pygame.draw.rect(screen , BAM , (800,25,40,40))
    screen.blit(text_2,(810,22))
    #run
    pygame.draw.rect(screen,BAM, (700,100,240,40))
    screen.blit(text_run,(710,98))
    #random
    pygame.draw.rect(screen,BAM, (700,200,240,40))
    screen.blit(text_random, (710,198))
    #errol
    pygame.draw.rect(screen,BAM, (700,300,240,40))
    #algorithm
    pygame.draw.rect(screen,BAM, (700,400,240,40))
    screen.blit(text_algorithm, (710,398))
    #reset
    pygame.draw.rect(screen,BAM, (700,500,240,40))
    screen.blit(text_reset, (710,498))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if 25 < mouse_x < 625 and 25 < mouse_x < 575:
        text_chuot = fontt.render("(" + str(mouse_x-25) + "," + str(mouse_y-25) + ')', True, CHU)
        screen.blit(text_chuot, (mouse_x + 5,mouse_y + 5))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #nut cong
            if 700<mouse_x <740 and 25 < mouse_y < 65:
                K+=1
                if K > 9:
                    K = 9
            #nut tru
            if 800<mouse_x <840 and 25 < mouse_y < 65:
                K-=1
                if K < 0:
                    K = 0
            #nut run
            if 700 < mouse_x < 940 and 100 < mouse_y < 140:
                labels = []
                if clusters == []:
                    continue
                #gán điểm vào cluster gần nhất
                for p in points:
                    distances_to_cluster = []
                    for c in clusters:
                        dis = distance(p,c)
                        distances_to_cluster.append(dis)
                    min_distance = min(distances_to_cluster)
                    label = distances_to_cluster.index(min_distance)
                    labels.append(label)
                #cập nhật cluster
                for i in range(K):
                    sum_x =0
                    sum_y =0
                    count =0
                    for j in range(len(points)):
                        if labels[j] == i:
                            sum_x += points[j][0]
                            sum_y += points[j][1]
                            count +=1
                    if count != 0:
                        new_cluster_x = sum_x / count 
                        new_cluster_y = sum_y / count
                        clusters[i] = [new_cluster_x,new_cluster_y]

            #random
            if 700 < mouse_x < 940 and 200 < mouse_y < 240:
                clusters = []
                labels = []
                for i in range(K):
                    random_point = [randint(0,600), randint(0,550)]
                    clusters.append(random_point)
            #algorithm
            if 700 < mouse_x < 940 and 400 < mouse_y < 440:
                #try:
                    from sklearn.cluster import KMeans

                    kmeans = KMeans(n_clusters=K).fit(points) #dòng đã làm tự động random và run
                    labels = kmeans.predict(points)
                    clusters = kmeans.cluster_centers_
                #except:
                #    print("error")

            #reset
            if 700 < mouse_x < 920 and 500 < mouse_y <540:
                points = []
                error =0
                labels = []
                clusters =[]
                    
            #bam tren bang
            if 25 < mouse_x < 625 and 25 < mouse_y < 575:
                labels = []
                point = [mouse_x -25, mouse_y - 25]
                points.append(point)
                #print (points)

    text_k = font.render("K = " + str(K), True,CHU)
    screen.blit(text_k , (860,25))
    for i in range(len(clusters)):
        pygame.draw.circle(screen, COLORS[i] , (clusters[i][0] + 25, clusters[i][1] + 25), 8)
    for i in range (len(points)):
        if labels == []:
            pygame.draw.circle(screen, BLACK, (points[i][0] + 25, points[i][1] + 25), 5,1)
        else:
            pygame.draw.circle(screen, COLORS[labels[i]],(points[i][0] + 25, points[i][1] + 25), 5,1)
    #error 
    error = 0
    if clusters != [] and labels != []:
        for i in range(len(points)):
            error+= distance(points[i],clusters[labels[i]])
    text_error = font.render("Error = " + str(int(error)), True , CHU)
    screen.blit(text_error, (710,298))

    pygame.display.update()

pygame.quit()
