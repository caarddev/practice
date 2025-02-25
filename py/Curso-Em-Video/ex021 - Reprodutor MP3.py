import pygame
pygame.init()
pygame.mixer.music.load('Its Going Down Now.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2)
print(f'Tocando {'Its Going Down Now.mp3'}...')
pygame.event.wait()