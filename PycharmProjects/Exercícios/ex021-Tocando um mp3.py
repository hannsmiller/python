# faça um programa em python que abra e reproduza o áudio de um arquivo mp3.
import pygame
pygame.init()
pygame.mixer.music.load('ex021-Tocando um mp3.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
