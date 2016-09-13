import pygame 
from pygame import *
from pygame.locals import *
import random
import sys
import pickle
import time
import os

pygame.init()
screen_x = 1000
screen_y = 1000
screen = pygame.display.set_mode([screen_x,screen_y])
loading_img = pygame.image.load('booting.png')
screen.blit(loading_img,(0,0))
pygame.display.update()

#colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
blue2 = (44, 157, 201)
blue3 = (8, 140, 196)
blue4 = (40, 181, 166)
red = (255, 0, 0)
green = (0, 255, 0)
green2 = (0, 153, 0)
green3 = (0,100,0)
gray = (158, 156, 166)
gray2 = (69, 67, 68)

#images
os.chdir('images')
gridtech_logo_img = pygame.image.load("logo.png")
shutdown_img = pygame.image.load("shutdown.png")
shutdown_img = pygame.transform.scale(shutdown_img,(100, 100))
calendar_img = pygame.image.load("calendar3.png")
calendar_img = pygame.transform.scale(calendar_img,(80, 80))
web_img = pygame.image.load("web66.png")
web_img = pygame.transform.scale(web_img,(80, 80))
x_img = pygame.image.load("cross31 (1).png")
settings_img = pygame.image.load("settings.png")
os.chdir('..')

#setup
clock = pygame.time.Clock()

#vars
closeApp = False
app = 'home'
menu = 'home'
rendermode = 'home'

#pygame start
from win32api import GetSystemMetrics
print "Width =", GetSystemMetrics(0)
print "Height =", GetSystemMetrics(1)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ( GetSystemMetrics(0) / 4, 1)
pygame.init()
screen_x = GetSystemMetrics(0)
screen_y = GetSystemMetrics(1)
screen = pygame.display.set_mode([screen_x,screen_y], FULLSCREEN)

#fonts
big_font = pygame.font.SysFont('Calibri', 80)
menu_font = pygame.font.SysFont('Calibri', 40)
menu_font = pygame.font.SysFont('Calibri', 40)
app_bar_font = pygame.font.SysFont('Calibri', 25)

#window settings
#pygame.display.set_icon(logo_img)
pygame.display.set_caption("Company Sim")

#program
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    def appOpen(x, y, sx, sy, color1, color2):
        pygame.draw.rect(screen, color1, [x, y , sx, sy])
        pygame.draw.rect(screen, color2, [x, y , sx, 50])
        x_text = menu_font.render('x', True, color1)           
        screen.blit(x_text, (x + sx - 30, y + 10))  

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if mx > x + sx - 30 and mx < x + sx - 30 + 40 and my > y + 10 and my < y + 10 + 40:
                global app
                app = 'home'

    def menuOpen(x, y, menus, color1, color2):
        pygame.draw.rect(screen, color1, [x, y , 300, menus * 50])   
        x_text = menu_font.render('close menu', True, color2)           
        screen.blit(x_text, (x, y + menus * 50 - 50))  
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if mx > x and mx < x + 300 and my > y + menus * 50 - 50 and my < y + menus * 50:   
                global menu   
                menu = 'home' 

    def infoMenu(x, y, text, color1, color2):
        pygame.draw.rect(screen, color1, [x, y , len(text)*16, 55])   
        x_text = menu_font.render(text, True, color2)           
        screen.blit(x_text, (x, y + 5))

    def crash(type):
        global rendermode
        if type == 1:
            rendermode = 'crash1'
        
    if rendermode == 'home':
        #settings
        screen.fill(blue2)
        clock.tick(200)
        mx, my = pygame.mouse.get_pos()

        fps_text = menu_font.render('FPS:' +str (clock.get_fps()), True, blue4)
    
        #app bar
        #time = str(time)
        time_text = app_bar_font.render((time.strftime('%I:%M %p')), True, white)
        pygame.draw.rect(screen, blue3, [0, 0 , 100, 1080])
        screen.blit(time_text,(0, 1060))
        screen.blit(gridtech_logo_img,(10, 10))
        screen.blit(settings_img, (15, 100))
        #screen.blit(calendar_img,(10, 135))
        #screen.blit(web_img,(10, 230))
        #click(app bar)
        #sys control panel
        if my > 10 and my < 90:
            if mx > 10 and mx < 90:
                infoMenu(100, 10, 'system panel  ', blue3, white)
        if my > 100 and my < 164:
            if mx > 15 and mx < 79:
                infoMenu(100, 100, 'settings', blue3, white)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if my > 10 and my < 90:
                    if mx > 10 and mx < 90:
                        menu = 'sys panel'
                if my > 100 and my < 164:
                    if mx > 15 and mx < 79:
                        app = 'settings'
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 3:
                if my > 100 and my < 164:
                    if mx > 15 and mx < 79:
                        menu = 'settings'

        if not app == 'home':
            if app == 'shutdown':
                appOpen(500, 50 , 800, 400, blue3, blue4)     
                text = menu_font.render('LOOKS LIKE GridOS IS SHUTTING DOWN!', True, blue4)           
                screen.blit(text, (500, 150))    
                pygame.draw.rect(screen, blue2, [510, 300, 110, 50]) 
                text = menu_font.render('ABORT', True, blue4)           
                screen.blit(text, (510, 300))                        
                if mx > 510 and mx < 510 + 110 and my > 300 and my < 300 + 50:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        shutdown_a = os.system("shutdown -a")
                        if shutdown_a == 1116:
                            app = 'error 1'
                        else:
                            app = 'abort'
            if app == 'error 1':
                appOpen(500, 50 , 800, 400, blue3, blue4)     
                text = menu_font.render('OH NO! We could not abort (error 1)', True, blue4)           
                screen.blit(text, (500, 150))    
            if app == 'error 2':
                appOpen(500, 50 , 850, 400, blue3, blue4)     
                text = menu_font.render('OH NO! The app was force quit (error 2)', True, blue4)           
                screen.blit(text, (500, 150))    
                text = menu_font.render('The app may of crashed or it was force quit manually', True, blue4)           
                screen.blit(text, (500, 200)) 
            if app == 'abort':
                appOpen(500, 50 , 800, 400, blue3, blue4)     
                text = menu_font.render('abort successful!', True, blue4)           
                screen.blit(text, (500, 150))             
            if app == 'sysinfo':
                appOpen(200, 50 , GetSystemMetrics(0) - 250,  GetSystemMetrics(1) - 100, blue3, blue4)    
                text = big_font.render('Grid OS info:', True, blue4)           
                screen.blit(text, (210, 100))    
                text = menu_font.render('version 1.0.0', True, blue4)           
                screen.blit(text, (210, 200))      
                screen.blit(fps_text, (210, 250))
                pygame.draw.rect(screen, blue2, [210, 300, 200, 50]) 
                text = menu_font.render('Error List', True, blue4)           
                screen.blit(text, (210, 300))                        
                if mx > 210 and mx < 210 + 200 and my > 300 and my < 300 + 50:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        app = 'error list'
                pygame.draw.rect(screen, blue2, [210, 360, 200, 50]) 
                text = menu_font.render('Change Log', True, blue4)           
                screen.blit(text, (210, 360))                        
                if mx > 210 and mx < 210 + 200 and my > 360 and my < 360 + 50:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        app = 'change log'
            if app == 'error list':
                appOpen(200, 50 , GetSystemMetrics(0) - 250,  GetSystemMetrics(1) - 100, blue3, blue4)      
                text = big_font.render('Errors:', True, blue4)           
                screen.blit(text, (210, 100))   
                text = menu_font.render('Error 1: OH NO! We could not abort (shutdown)', True, blue4)           
                screen.blit(text, (210, 200))   
                text = menu_font.render('Error 2: OH NO! The app was force quit', True, blue4)           
                screen.blit(text, (210, 250))   
            if app == 'change log':
                appOpen(200, 50 , GetSystemMetrics(0) - 250,  GetSystemMetrics(1) - 100, blue3, blue4)      
                text = big_font.render('Changes:', True, blue4)           
                screen.blit(text, (210, 100))   
                text = menu_font.render('1.0.0(Alpha) (9/10/16 - now):', True, blue4)           
                screen.blit(text, (210, 200))   
                text = menu_font.render('Release', True, blue4)           
                screen.blit(text, (210, 250))   
            if app == 'settings':
                appOpen(200, 50 , GetSystemMetrics(0) - 250,  GetSystemMetrics(1) - 100, blue3, blue4)      
                text = big_font.render('Color Settings', True, blue4)           
                screen.blit(text, (210, 100))   

            #appOpen(200, 50 , GetSystemMetrics(0) - 250,  GetSystemMetrics(1) - 100, blue3, blue4)


        if not menu == 'home':
            if menu == 'sys panel':
                menuOpen(100, 10, 5, blue3, white)
                sd_text = menu_font.render('Shut Down', True, white)           
                screen.blit(sd_text, (100, 10))  
                sd_text = menu_font.render('Restart', True, white)           
                screen.blit(sd_text, (100, 60))  
                close_text = menu_font.render('Close GridOS', True, white)           
                screen.blit(close_text, (100, 110))  
                close_text = menu_font.render('System Info', True, white)           
                screen.blit(close_text, (100, 160))  
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if mx > 100 and mx < 300:
                        if my > 110 and my < 160:
                            sys.exit()
                        if my > 160 and my < 210:
                            app = 'sysinfo'
                        if my > 10 and my < 60:
                            os.system("shutdown -s")
                            app = 'shutdown'
                        if my > 60 and my < 110:
                            os.system("shutdown -r")
                            app = 'shutdown'
                        menu = 'home'
            if menu == 'settings':
                menuOpen(100, 100, 3, gray, blue3)
                text = menu_font.render('Open', True, blue3)           
                screen.blit(text, (100, 100))  
                text = menu_font.render('Force Quit', True, blue3)           
                screen.blit(text, (100, 150)) 
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if mx > 100 and mx < 300:
                        if my > 100 and my < 150:
                            app = 'settings'
                        if my > 150 and my < 200:
                            closeApp = True
                        menu = 'home'

        if closeApp == True:
            app = 'error 2'
            closeApp = False

    pygame.display.update()