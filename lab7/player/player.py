import time
import pygame as pg
pg.init()

breakstuffPath = "/Users/Nurbek/Desktop/pp2/lab7/player/breakstuff.mp3"
casinPath = "/Users/Nurbek/Desktop/pp2/lab7/player/casin.mp3"
nggyuPath = "/Users/Nurbek/Desktop/pp2/lab7/player/nggyu.mp3"
sc = pg.display.set_mode((480, 360))
pg.display.set_caption("MP3Player")
clock = pg.time.Clock()
casin = pg.mixer.music.load(casinPath)
nggyu = pg.mixer.music.load(nggyuPath)
breakstuff = pg.mixer.music.load(breakstuffPath)
musicList = [breakstuffPath, casinPath, nggyuPath]
pg.mixer.music.play(-1)
monkey = pg.image.load("/Users/Nurbek/Desktop/pp2/lab7/player/trumpmog.png")

sc.blit(monkey, (0, 0))
flPlay = False
run = True
index = 0
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                flPlay = not flPlay
                if flPlay:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif event.key == pg.K_RIGHT:
                
                index += 1
                if index == len(musicList):
                    index = 0
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()
            elif event.key == pg.K_LEFT:
                index -= 1
                if index == -1:
                    index = len(musicList)-1
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()


    pg.display.flip()
    clock.tick(60)