import pygame 
from pygame import *
from pygame.locals import *
from Tkinter import *
import tkMessageBox
import random
import sys
import pickle
import time
import os
import win32api

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
music_img = pygame.image.load("cd-player.png")
notifications1_img = pygame.image.load("notifications-button.png")
notifications2_img = pygame.image.load("turn-notifications-on-button.png")
folder_img = pygame.image.load("open-folder-icon.png")
file_img = pygame.image.load("file.png")
power_img = pygame.image.load("power-button-outline.png")
os.chdir('..')

#setup
clock = pygame.time.Clock()

#vars
closeApp = False
app = 'home'
menu = 'home'
rendermode = 'home'
notifications_menu = False
hello = 0
notifications_list = ['','Welcome to Grid OS']
notifications_sub_list = ['','Please remember Grid OS is in alpha']

#pygame start
try:
    from win32api import GetSystemMetrics
except:
     root = Tk()
     root.title("Boot error")
     root["padx"] = 20
     root["pady"] = 20

     tkinterLabel = Label(root)
     tkinterLabel["text"] = "There was an error on startup!"
     tkinterLabel.pack()
     tkinterLabel2 = Label(root)
     tkinterLabel2["text"] = "Please install win32api(pywin32)"
     tkinterLabel2.pack()
                 
     #tkMessageBox.showinfo(title="Tk Info box", \
     #message="This is a Tk Info/Message box used to display output")

     root.mainloop()

try:  
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
    pygame.display.set_caption("Grid OS")
except:
     root = Tk()
     root.title("Boot error")
     root["padx"] = 20
     root["pady"] = 20

     tkinterLabel = Label(root)
     tkinterLabel["text"] = "an unkown error occured on startup!"
     tkinterLabel.pack()
     tkinterLabel2 = Label(root)
     tkinterLabel2["text"] = "Please be sure to use python 2.7"
     tkinterLabel2.pack()
                 
     #tkMessageBox.showinfo(title="Tk Info box", \
     #message="This is a Tk Info/Message box used to display output")

     root.mainloop()

#program
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    def appOpen(x, y, sx, sy, color1, color2):
        pygame.draw.rect(screen, color1, [x, y , sx, sy - 10])
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

    def infoMenu(x, y, text, color1, color2, rightCircle):
        pygame.draw.rect(screen, color1, [x, y , len(text)*16 + 10, 55])   
        x_text = menu_font.render(text, True, color2)           
        screen.blit(x_text, (x, y + 5))
        if rightCircle == True:
            pygame.draw.circle(screen, color1, (x + len(text) * 16 + 10, y + 27), 27, 0)              

    def crash(type):
        global rendermode
        if type == 1:
            rendermode = 'crash1'

    def newNotification(number, time):
        pygame.draw.rect(screen, blue3, [GetSystemMetrics(0) - 300, GetSystemMetrics(1) - 105 , 300, 55]) 
        screen.blit(app_bar_font.render('There is a new notification!', True, white), (GetSystemMetrics(0) - 300, GetSystemMetrics(1) - 105))
        text = app_bar_font.render('' +str(notifications_list[number]), True, blue4)
        screen.blit(text, (GetSystemMetrics(0) - 300, GetSystemMetrics(1) - 75))
        pygame.display.update()
        pygame.time.delay(time)
                
        
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
        screen.blit(gridtech_logo_img,(10, 10))
        screen.blit(settings_img, (15, 100))
        music_img = pygame.transform.scale(music_img, (64, 64))
        screen.blit(music_img, (15, 190))
        folder_img = pygame.transform.scale(folder_img, (64, 64))
        screen.blit(folder_img, (15, 280))
        pygame.draw.rect(screen, blue3, [GetSystemMetrics(0) - 400, GetSystemMetrics(1) - 50 , 400, 50])
        pygame.draw.circle(screen, blue3, (GetSystemMetrics(0) - 400, GetSystemMetrics(1),), 50, 0)  
        screen.blit(time_text,(GetSystemMetrics(0) - 100, GetSystemMetrics(1) - 30))
        notifications = len(notifications_list)
        if notifications < 2:
            notifications1_img = pygame.transform.scale(notifications1_img, (25, 25))
            screen.blit(notifications1_img, (GetSystemMetrics(0) - 130, GetSystemMetrics(1) - 30))
        else:
            notifications2_img = pygame.transform.scale(notifications2_img, (25, 25))
            screen.blit(notifications2_img, (GetSystemMetrics(0) - 130, GetSystemMetrics(1) - 30))    
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mx > GetSystemMetrics(0) - 130 and mx < GetSystemMetrics(0) - 105 and my > GetSystemMetrics(1) - 30 and my < GetSystemMetrics(1) - 5:
                    notifications_menu = True
        power_img = pygame.transform.scale(power_img, (25, 25))
        screen.blit(power_img, (GetSystemMetrics(0) - 160, GetSystemMetrics(1) - 30))
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mx > GetSystemMetrics(0) - 160 and mx < GetSystemMetrics(0) - 135 and my > GetSystemMetrics(1) - 30 and my < GetSystemMetrics(1) - 5:
                    menu = 'power'
        #screen.blit(calendar_img,(10, 135))
        #screen.blit(web_img,(10, 230))
        #click(app bar)
        #sys control panel
        if my > 10 and my < 90:
            if mx > 10 and mx < 90:
                infoMenu(100, 10, 'system panel  ', blue3, white, True)
        if my > 100 and my < 164:
            if mx > 15 and mx < 79:
                infoMenu(100, 100, 'settings  ', blue3, white, True)
        if my > 190 and my < 254:
            if mx > 15 and mx < 79:
                infoMenu(100, 190, 'music  ', blue3, white, True)
        if my > 280 and my < 370:
            if mx > 15 and mx < 79:
                infoMenu(100, 280, 'File Explorer ', blue3, white, True)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if my > 10 and my < 90:
                    if mx > 10 and mx < 90:
                        menu = 'sys panel'
                if my > 100 and my < 164:
                    if mx > 15 and mx < 79:
                        app = 'settings'
                if my > 280 and my < 370:
                    if mx > 15 and mx < 79:
                        app = 'file explorer'
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
                notifications_list.append('An app crashed!')
                notifications_sub_list.append('The app may of crashed (error 2)')
                newNotification(-1, 1000)
                app = 'home'
                #appOpen(500, 50 , 850, 400, blue3, blue4)     
                #text = menu_font.render('OH NO! The app was force quit (error 2)', True, blue4)           
                #screen.blit(text, (500, 150))    
                #text = menu_font.render('The app may of crashed or it was force quit manually', True, blue4)           
                #screen.blit(text, (500, 200)) 
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
            if app == 'notificationsfordays':
                notifications_list.append('An app crashed!')
                notifications_sub_list.append('The app may of crashed (error 2)')
            if app == 'file explorer':
                appOpen(200, 50 , GetSystemMetrics(0) - 250,  GetSystemMetrics(1) - 100, blue3, blue4)   
                text = menu_font.render('Notification Crasher', True, blue4)           
                screen.blit(text, (280, 110)) 
                screen.blit(file_img, (210, 100))
                if mx > 210 and mx < 274 and my > 100 and my < 164:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        app = 'notificationsfordays' 

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
            if menu == 'power':
                menuOpen(GetSystemMetrics(0) - 300, GetSystemMetrics(1) - 250, 4, blue3, white)
                sd_text = menu_font.render('Shut Down', True, white)           
                screen.blit(sd_text, (GetSystemMetrics(0) - 300, GetSystemMetrics(1) - 250))  
                sd_text = menu_font.render('Restart', True, white)           
                screen.blit(sd_text, (GetSystemMetrics(0) - 300, GetSystemMetrics(1) - 200))  
                sd_text = menu_font.render('Close Grid OS', True, white)           
                screen.blit(sd_text, (GetSystemMetrics(0) - 300, GetSystemMetrics(1) - 150))  
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if mx > GetSystemMetrics(0) - 300 and mx < GetSystemMetrics(0):
                        if my > GetSystemMetrics(1) - 150 and my < GetSystemMetrics(1) - 100:
                            sys.exit()
                        if my > GetSystemMetrics(1) - 250 and my < GetSystemMetrics(1) - 200:
                            os.system("shutdown -s")
                            app = 'shutdown'
                        if my > GetSystemMetrics(1) - 200 and my < GetSystemMetrics(1) - 150:
                            os.system("shutdown -r")
                            app = 'shutdown'

        if notifications_menu == True:
            pygame.draw.rect(screen, blue3, [GetSystemMetrics(0) - 400, 0 , 500, GetSystemMetrics(1) - 50])    
            notifications = len(notifications_list)  
            if notifications < 2:
                screen.blit(menu_font.render('No notifications', True, white), (GetSystemMetrics(0) - 320, 10))
            else:
                screen.blit(app_bar_font.render('Clear', True, white), (GetSystemMetrics(0) - 60, 10)) 
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if mx > GetSystemMetrics(0) - 60 and mx < GetSystemMetrics(0):
                        if my > 10 and my < 40:        
                            notifications_list = ['']
                            notifications_sub_list = ['']
                render = True
                render_clock = 0
                while render == True:
                    try:
                        text = menu_font.render('' +str(notifications_list[render_clock]), True, white)
                        screen.blit(text, (GetSystemMetrics(0) - 400, render_clock * 75))
                        text = app_bar_font.render('' +str(notifications_sub_list[render_clock]), True, white)
                        screen.blit(text, (GetSystemMetrics(0) - 400, (render_clock * 75) + 40))
                        render_clock = render_clock + 1
                    except:
                        render_clock = 0
                        render = False                
                         
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if mx < GetSystemMetrics(0) - 400:
                    if my > 0 and my < GetSystemMetrics(1):         
                        notifications_menu = False        

        if closeApp == True:
            app = 'error 2'
            closeApp = False

        if hello == 1:
            newNotification(1, 1000)

    hello = hello + 1

    pygame.display.update()