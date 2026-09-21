import pygame

# Inicializa o mixer de áudio
pygame.mixer.init()

# Carrega o ficheiro de áudio usando o caminho relativo
pygame.mixer.music.load('audio.ogg')

# Toca a música
pygame.mixer.music.play()

# Mantém o programa aberto para conseguir ouvir
input('Pressione Enter para parar a música...')