import pygame

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((480,270))
pygame.display.set_caption("Player")
run = True
songs = ["Despacito.mp3","Faded.mp3","The_hills.mp3"]
num = 0
pygame.mixer.music.load(songs[num])
pygame.mixer.music.play()

while run:
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and num < 2:
        num+=1
        pygame.mixer.music.load(songs[num])
        pygame.mixer.music.play()
    elif keys[pygame.K_LEFT] and num > 0:
        num-=1
        pygame.mixer.music.load(songs[num]) 
        pygame.mixer.music.play()
    
    if keys[pygame.K_s]:
        pygame.mixer.music.pause()
    elif keys[pygame.K_p]:
        pygame.mixer.music.unpause()

    clock.tick(10)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit