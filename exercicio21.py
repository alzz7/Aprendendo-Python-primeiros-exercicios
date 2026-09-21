import pygame

# Inicializa o mixer de áudio
pygame.mixer.init()

# Carrega o arquivo MP3 (certifique-se de que o arquivo está na pasta 'Exercicios Python')
pygame.mixer.music.load('audio.ogg')

# Toca a música
pygame.mixer.music.play()

# Mantém o programa aberto para a música tocar
input('Pressione Enter para parar a música...')