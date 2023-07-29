import pygame

file_path = r"D:\youxi\IDM_downlaod\南征北战 - Happy扭腰.mp3"  #这里放音乐文件的地址

# 初始化pygame
pygame.init()

# 加载音乐文件
pygame.mixer.music.load(file_path)

# 播放音乐
pygame.mixer.music.play()

# 等待音乐播放完成
while pygame.mixer.music.get_busy():
    continue

# 关闭pygame
pygame.quit()