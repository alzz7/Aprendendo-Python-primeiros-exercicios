import pygame

pygame.init()

# Carrega e toca a música
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()

# Segura a execução do programa para dar tempo de ouvir
input('Tocando áudio... Pressione ENTER para parar.')