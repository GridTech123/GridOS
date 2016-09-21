try:
    import pygame
    from pygame import *
    from pygame.locals import *
except:
     from Tkinter import *
     import tkMessageBox
     root = Tk()
     root.title("Boot error")
     root["padx"] = 20
     root["pady"] = 20

     tkinterLabel = Label(root)
     tkinterLabel["text"] = "There was an error on startup!"
     tkinterLabel.pack()
     tkinterLabel2 = Label(root)
     tkinterLabel2["text"] = "Please install Pygame"
     tkinterLabel2.pack()
                 
     #tkMessageBox.showinfo(title="Tk Info box", \
     #message="This is a Tk Info/Message box used to display output")

     root.mainloop()
from Tkinter import *
import tkMessageBox
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

#

#images
try:
    os.chdir('images')
    gridtech_logo_img = pygame.image.load("logo.png")
    shutdown_img = pygame.image.load("shutdown.png")
    shutdown_img = pygame.transform.scale(shutdown_img,(100, 100))
    calendar_img = pygame.image.load("calendar.png")
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
    warning_img = pygame.image.load("exclamation-mark-inside-a-circle.png")
    question_img = pygame.image.load("question-mark.png")
    os.chdir('..')
except:
     os.chdir('..')
     os.chdir('html')
     os.startfile('bootHelp.html')
     os.chdir('..')
     root = Tk()
     root.title("Boot error")
     root["padx"] = 20
     root["pady"] = 20

     tkinterLabel = Label(root)
     tkinterLabel["text"] = "There was an error on startup!"
     tkinterLabel.pack()
     tkinterLabel2 = Label(root)
     tkinterLabel2["text"] = "There was an issue getting images."
     tkinterLabel2.pack()

     root.mainloop()

#setup
clock = pygame.time.Clock()

#vars
closeApp = False
app = 'home'
menu = 'home'
rendermode = 'welcome 1'
notifications_menu = False
hello = 0
notifications_list = ['','Welcome to Grid OS']
notifications_sub_list = ['','Please remember Grid OS is in alpha']
welcomeColor1 = 0
welcomeColor2 = 255
welcomeColor3 = 255
colorOp = 1
changeHello = True
changeHelloTimer = 50
reminderList = []
reminderTimeList = []
notificationName = ''
notificationName2 = ''
editNotificationName = 0

#pygame start
try:
    from win32api import GetSystemMetrics
except:
     os.chdir('html')
     os.startfile('bootHelp.html')
     os.chdir('..')
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
    if GetSystemMetrics(0) < 200 or GetSystemMetrics(1) < 200:
        os.chdir('html')
        os.startfile('screenError.html')
        os.chdir('..')        
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
     os.chdir('html')
     os.startfile('bootHelp.html')
     os.chdir('..')
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
                
    def window(border, x, y):
        if border == False:
            screen = pygame.display.set_mode([x,y], NOFRAME)
    if rendermode == 'welcome 1': #(40, 181, 166) (0, 0, 255)
        if colorOp == 1:
            if welcomeColor1 == 0 and welcomeColor2 == 0 and welcomeColor3 == 255:
                colorOp = 2
            if welcomeColor1 > 0:
                welcomeColor1 = welcomeColor1 - 1
            if welcomeColor2 > 0:
                welcomeColor2 = welcomeColor2 - 1
            if welcomeColor3 < 255:
                welcomeColor3 = welcomeColor3 + 1
        if colorOp == 2:
            if welcomeColor1 == 40 and welcomeColor2 == 181 and welcomeColor3 == 166:
                colorOp = 1
            if welcomeColor1 < 40:
                welcomeColor1 = welcomeColor1 + 1
            if welcomeColor2 < 181:
                welcomeColor2 = welcomeColor2 + 1
            if welcomeColor3 > 166:
                welcomeColor3 = welcomeColor3 - 1
        screen.fill((welcomeColor1, welcomeColor2, welcomeColor3))
        clock.tick(200)
        mx, my = pygame.mouse.get_pos()

        pygame.draw.rect(screen, blue3, [GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2, GetSystemMetrics(0) / 2, GetSystemMetrics(1) / 2])       

        if changeHelloTimer == 50:
            changeHello = True

        if changeHello == True:
            helloOp = random.randint(1, 10)
            if helloOp == 1:
                text = big_font.render('Hello', True, white)           
                #screen.blit(text, (GetSystemMetrics(0) / 2 - 100, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2))
            if helloOp == 2:
                text = big_font.render('Ciao', True, white)           
                #screen.blit(text, (GetSystemMetrics(0) / 2 - 100, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2))
            if helloOp == 3:
                text = big_font.render('buna', True, white)           
                #screen.blit(text, (GetSystemMetrics(0) / 2 - 100, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2))
            if helloOp == 4:
                text = big_font.render('dobry den', True, white)           
                #screen.blit(text, (GetSystemMetrics(0) / 2 - 100, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2))
            if helloOp == 5:
                text = big_font.render('Hola', True, white)           
                #screen.blit(text, (GetSystemMetrics(0) / 2 - 100, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2))
            if helloOp == 6:
                text = big_font.render('Hej', True, white)           
                #screen.blit(text, (GetSystemMetrics(0) / 2 - 100, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2))
            if helloOp == 7:
                text = big_font.render('Merhaba', True, white)           
                #screen.blit(text, (GetSystemMetrics(0) / 2 - 100, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2))
            if helloOp == 8:
                text = big_font.render('Salut', True, white)           
                #screen.blit(text, (GetSystemMetrics(0) / 2 - 100, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2))
            if helloOp == 9:
                text = big_font.render('Hallo', True, white)           
                #screen.blit(text, (GetSystemMetrics(0) / 2 - 100, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2))
            if helloOp == 10:
                text = big_font.render('labas', True, white)           
                #screen.blit(text, (GetSystemMetrics(0) / 2 - 100, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2))
            changeHelloTimer = 0
            changeHello = False
        screen.blit(text, ((GetSystemMetrics(0) / 2 - len('' +str(text)) * 20), GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2))
        changeHelloTimer = changeHelloTimer + 1

        text2 = menu_font.render('Do you have a Grid OS account?', True, white)       
        screen.blit(text2, ((GetSystemMetrics(0) / 2 - len('' +str(text)) * 20), GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 100))     

        pygame.draw.rect(screen, blue4, [GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 + 500, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 200, 100, 50])  
        pygame.draw.rect(screen, blue4, [GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 + 610, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 200, 100, 50]) 

        text2 = menu_font.render('Yes', True, white)       
        screen.blit(text2, ((GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 + 500, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 200, 100, 50))) 

        text2 = menu_font.render('No', True, white)       
        screen.blit(text2, ((GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 + 610, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 200, 100, 50))) 

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mx > GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 + 500 and mx < GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2 + 500 + 100 and my > GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 200 and my < GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 200 + 50:
                    rendermode = 'welcome 2-1'

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mx > GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 + 610 and mx < GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2 + 610 + 100 and my > GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 200 and my < GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 200 + 50:
                    rendermode = 'welcome 1-1'     

        time_text = app_bar_font.render((time.strftime('%I:%M %p')), True, white)
        pygame.draw.rect(screen, blue3, [GetSystemMetrics(0) - 400, GetSystemMetrics(1) - 50 , 400, 50])
        pygame.draw.circle(screen, blue3, (GetSystemMetrics(0) - 400, GetSystemMetrics(1),), 50, 0)  
        screen.blit(time_text,(GetSystemMetrics(0) - 100, GetSystemMetrics(1) - 30))
        power_img = pygame.transform.scale(power_img, (25, 25))
        screen.blit(power_img, (GetSystemMetrics(0) - 160, GetSystemMetrics(1) - 30))
        question_img = pygame.transform.scale(question_img, (25, 25))
        screen.blit(question_img, (GetSystemMetrics(0) - 200, GetSystemMetrics(1) - 30))
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mx > GetSystemMetrics(0) - 200 and mx < GetSystemMetrics(0) - 175 and my > GetSystemMetrics(1) - 30 and my < GetSystemMetrics(1) - 5:
                     os.chdir('html')
                     os.startfile('accountHelp.html')
                     os.chdir('..')
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mx > GetSystemMetrics(0) - 160 and mx < GetSystemMetrics(0) - 135 and my > GetSystemMetrics(1) - 30 and my < GetSystemMetrics(1) - 5:
                    menu = 'power'
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

        pygame.display.update()

    if rendermode == 'welcome 1-1':
                 if colorOp == 1:
                     if welcomeColor1 == 0 and welcomeColor2 == 0 and welcomeColor3 == 255:
                         colorOp = 2
                     if welcomeColor1 > 0:
                         welcomeColor1 = welcomeColor1 - 1
                     if welcomeColor2 > 0:
                         welcomeColor2 = welcomeColor2 - 1
                     if welcomeColor3 < 255:
                         welcomeColor3 = welcomeColor3 + 1
                 if colorOp == 2:
                     if welcomeColor1 == 40 and welcomeColor2 == 181 and welcomeColor3 == 166:
                         colorOp = 1
                     if welcomeColor1 < 40:
                        welcomeColor1 = welcomeColor1 + 1
                     if welcomeColor2 < 181:
                         welcomeColor2 = welcomeColor2 + 1
                     if welcomeColor3 > 166:
                         welcomeColor3 = welcomeColor3 - 1
                 screen.fill((welcomeColor1, welcomeColor2, welcomeColor3))
                 clock.tick(200)
                 mx, my = pygame.mouse.get_pos() 

                 pygame.draw.rect(screen, blue3, [GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2, GetSystemMetrics(0) / 2, GetSystemMetrics(1) / 2])       

                 text2 = big_font.render('Why Hello!', True, white)       
                 screen.blit(text2, ((GetSystemMetrics(0) / 2 - 480, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 100)))
                 text2 = menu_font.render('Its as easy as setting up an account!', True, white)       
                 screen.blit(text2, ((GetSystemMetrics(0) / 2 - 480, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 200)))
                 text2 = menu_font.render('Username: ', True, white)   
                 screen.blit(text2, ((GetSystemMetrics(0) / 2 - 480, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 250)))
                 pygame.draw.rect(screen, blue2, [GetSystemMetrics(0) / 2 - 480 + 180, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 250, 700, 50])
                 if mx > GetSystemMetrics(0) / 2 - 480 + 180 and mx < GetSystemMetrics(0) / 2 - 480 + 180 + 700 and my > GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 250 and my < GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 250 + 50:
                     if event.type == MOUSEBUTTONDOWN and event.button == 1:
                         editNotificationName = 1
                 if editNotificationName == 1:
                     if event.type == KEYDOWN:
                        if event.key == pygame.K_a:
                            notificationName = notificationName + 'a'
                        if event.key == pygame.K_b:
                            notificationName = notificationName + 'b'
                        if event.key == pygame.K_c:
                            notificationName = notificationName + 'c'
                        if event.key == pygame.K_d:
                            notificationName = notificationName + 'd'
                        if event.key == pygame.K_e:
                            notificationName = notificationName + 'e'
                        if event.key == pygame.K_f:
                            notificationName = notificationName + 'f'
                        if event.key == pygame.K_g:
                            notificationName = notificationName + 'g'
                        if event.key == pygame.K_h:
                            notificationName = notificationName + 'h'
                        if event.key == pygame.K_i:
                            notificationName = notificationName + 'i'
                        if event.key == pygame.K_j:
                            notificationName = notificationName + 'j'
                        if event.key == pygame.K_k:
                            notificationName = notificationName + 'k'
                        if event.key == pygame.K_l:
                            notificationName = notificationName + 'l'
                        if event.key == pygame.K_m:
                            notificationName = notificationName + 'm'
                        if event.key == pygame.K_n:
                            notificationName = notificationName + 'n'
                        if event.key == pygame.K_o:
                            notificationName = notificationName + 'o'
                        if event.key == pygame.K_p:
                            notificationName = notificationName + 'p'
                        if event.key == pygame.K_q:
                            notificationName = notificationName + 'q'
                        if event.key == pygame.K_r:
                            notificationName = notificationName + 'r'
                        if event.key == pygame.K_s:
                            notificationName = notificationName + 's'
                        if event.key == pygame.K_t:
                            notificationName = notificationName + 't'
                        if event.key == pygame.K_u:
                            notificationName = notificationName + 'u'
                        if event.key == pygame.K_v:
                            notificationName = notificationName + 'v'
                        if event.key == pygame.K_w:
                            notificationName = notificationName + 'w'
                        if event.key == pygame.K_x:
                            notificationName = notificationName + 'x'
                        if event.key == pygame.K_y:
                            notificationName = notificationName + 'y'
                        if event.key == pygame.K_z:
                            notificationName = notificationName + 'z'
                        if event.key == pygame.K_SPACE:
                            notificationName = notificationName + ' '
                        if event.key == pygame.K_BACKSPACE:
                            notificationName = notificationName[0:len(notificationName) - 1]
                        pygame.time.delay(65)
                 else:
                    screen.blit(menu_font.render('click me', True, gray),([GetSystemMetrics(0) / 2 - 290, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 250]))                   
                 screen.blit(menu_font.render(''+str(notificationName), True, white),([GetSystemMetrics(0) / 2 - 290, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 250])) 
                 #text2 = menu_font.render('Username', True, white)   
                 #screen.blit(text2, ((GetSystemMetrics(0) / 2 - len('' +str(text)) * 20), GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 250))
                 text2 = menu_font.render('Password', True, white)   
                 screen.blit(text2, ((GetSystemMetrics(0) / 2 - 480, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 310)))
                 pygame.draw.rect(screen, blue2, [GetSystemMetrics(0) / 2 - 480 + 180, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 310, 700, 50])
                 if mx > GetSystemMetrics(0) / 2 - 480 + 180 and mx < GetSystemMetrics(0) / 2 - 480 + 180 + 700 and my > GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 310 and my < GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 310 + 50:
                     if event.type == MOUSEBUTTONDOWN and event.button == 1:
                         editNotificationName = 2
                 if editNotificationName == 2:
                     if event.type == KEYDOWN:
                        if event.key == pygame.K_a:
                            notificationName2 = notificationName2 + 'a'
                        if event.key == pygame.K_b:
                            notificationName2 = notificationName2 + 'b'
                        if event.key == pygame.K_c:
                            notificationName2 = notificationName2 + 'c'
                        if event.key == pygame.K_d:
                            notificationName2 = notificationName2 + 'd'
                        if event.key == pygame.K_e:
                            notificationName2 = notificationName2 + 'e'
                        if event.key == pygame.K_f:
                            notificationName2 = notificationName2 + 'f'
                        if event.key == pygame.K_g:
                            notificationName2 = notificationName2 + 'g'
                        if event.key == pygame.K_h:
                            notificationName2 = notificationName2 + 'h'
                        if event.key == pygame.K_i:
                            notificationName2 = notificationName2 + 'i'
                        if event.key == pygame.K_j:
                            notificationName2 = notificationName2 + 'j'
                        if event.key == pygame.K_k:
                            notificationName2 = notificationName2 + 'k'
                        if event.key == pygame.K_l:
                            notificationName2 = notificationName2 + 'l'
                        if event.key == pygame.K_m:
                            notificationName2 = notificationName2 + 'm'
                        if event.key == pygame.K_n:
                            notificationName2 = notificationName2 + 'n'
                        if event.key == pygame.K_o:
                            notificationName2 = notificationName2 + 'o'
                        if event.key == pygame.K_p:
                            notificationName2 = notificationName2 + 'p'
                        if event.key == pygame.K_q:
                            notificationName2 = notificationName2 + 'q'
                        if event.key == pygame.K_r:
                            notificationName2 = notificationName2 + 'r'
                        if event.key == pygame.K_s:
                            notificationName2 = notificationName2 + 's'
                        if event.key == pygame.K_t:
                            notificationName2 = notificationName2 + 't'
                        if event.key == pygame.K_u:
                            notificationName2 = notificationName2 + 'u'
                        if event.key == pygame.K_v:
                            notificationName2 = notificationName2 + 'v'
                        if event.key == pygame.K_w:
                            notificationName2 = notificationName2 + 'w'
                        if event.key == pygame.K_x:
                            notificationName2 = notificationName2 + 'x'
                        if event.key == pygame.K_y:
                            notificationName2 = notificationName2 + 'y'
                        if event.key == pygame.K_z:
                            notificationName2 = notificationName2 + 'z'
                        if event.key == pygame.K_SPACE:
                            notificationName2 = notificationName2 + ' '
                        if event.key == pygame.K_BACKSPACE:
                            notificationName2 = notificationName2[0:len(notificationName2) - 1]
                        pygame.time.delay(60)
                 else:
                    screen.blit(menu_font.render('click me', True, gray),([GetSystemMetrics(0) / 2 - 290, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 310])) 
                 screen.blit(menu_font.render(''+str(notificationName2), True, white),([GetSystemMetrics(0) / 2 - 290, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 310]))        

                 pygame.draw.rect(screen, blue4, [GetSystemMetrics(0) / 2 - 480, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 400, 210, 50]) 
                 text2 = menu_font.render('Ok lets start!', True, white)       
                 screen.blit(text2, ((GetSystemMetrics(0) / 2 - 480, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 400, 100, 50))) 

                 if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                if mx > GetSystemMetrics(0) / 2 - 480 and mx < GetSystemMetrics(0) / 2 - 480 + 210 and my > GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 400 and my < GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 400 + 50:
                                    username = notificationName
                                    password = notificationName2
                                    pickle_out = open('user.csf', 'w')
                                    pickle.dump(username, pickle_out)
                                    pickle_out = open('pass.csf', 'w')
                                    pickle.dump(password, pickle_out)
                                    pickle_out.close()
                                    rendermode = 'welcome 2-1'     

                 time_text = app_bar_font.render((time.strftime('%I:%M %p')), True, white)
                 pygame.draw.rect(screen, blue3, [GetSystemMetrics(0) - 400, GetSystemMetrics(1) - 50 , 400, 50])
                 pygame.draw.circle(screen, blue3, (GetSystemMetrics(0) - 400, GetSystemMetrics(1),), 50, 0)  
                 screen.blit(time_text,(GetSystemMetrics(0) - 100, GetSystemMetrics(1) - 30))
                 power_img = pygame.transform.scale(power_img, (25, 25))
                 screen.blit(power_img, (GetSystemMetrics(0) - 160, GetSystemMetrics(1) - 30))
                 question_img = pygame.transform.scale(question_img, (25, 25))
                 screen.blit(question_img, (GetSystemMetrics(0) - 200, GetSystemMetrics(1) - 30))
                 if event.type == MOUSEBUTTONDOWN:
                     if event.button == 1:
                         if mx > GetSystemMetrics(0) - 200 and mx < GetSystemMetrics(0) - 175 and my > GetSystemMetrics(1) - 30 and my < GetSystemMetrics(1) - 5:
                              os.chdir('html')
                              os.startfile('accountHelp.html')
                              os.chdir('..')
                 if event.type == MOUSEBUTTONDOWN:
                     if event.button == 1:
                         if mx > GetSystemMetrics(0) - 160 and mx < GetSystemMetrics(0) - 135 and my > GetSystemMetrics(1) - 30 and my < GetSystemMetrics(1) - 5:
                             menu = 'power'
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
                 pygame.display.update()

    if rendermode == 'welcome 2-1':
                 if colorOp == 1:
                     if welcomeColor1 == 0 and welcomeColor2 == 0 and welcomeColor3 == 255:
                         colorOp = 2
                     if welcomeColor1 > 0:
                         welcomeColor1 = welcomeColor1 - 1
                     if welcomeColor2 > 0:
                         welcomeColor2 = welcomeColor2 - 1
                     if welcomeColor3 < 255:
                         welcomeColor3 = welcomeColor3 + 1
                 if colorOp == 2:
                     if welcomeColor1 == 40 and welcomeColor2 == 181 and welcomeColor3 == 166:
                         colorOp = 1
                     if welcomeColor1 < 40:
                        welcomeColor1 = welcomeColor1 + 1
                     if welcomeColor2 < 181:
                         welcomeColor2 = welcomeColor2 + 1
                     if welcomeColor3 > 166:
                         welcomeColor3 = welcomeColor3 - 1
                 screen.fill((welcomeColor1, welcomeColor2, welcomeColor3))
                 clock.tick(200)
                 mx, my = pygame.mouse.get_pos() 

                 pygame.draw.rect(screen, blue3, [GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2, GetSystemMetrics(0) / 2, GetSystemMetrics(1) / 2])       

                 pickle_in = open('user.csf', 'r')
                 username = pickle.load(pickle_in)
                 pickle_in = open('pass.csf', 'r')
                 password = pickle.load(pickle_in)
                 text2 = big_font.render('Welcome back ' +str(username), True, white)       
                 screen.blit(text2, ((GetSystemMetrics(0) / 2 - 480, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 100)))
                 text2 = menu_font.render('Username: ', True, white)   
                 screen.blit(text2, ((GetSystemMetrics(0) / 2 - 480, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 250)))
                 notificationName = username
                 pygame.draw.rect(screen, blue2, [GetSystemMetrics(0) / 2 - 480 + 180, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 250, 700, 50])
                 if mx > GetSystemMetrics(0) / 2 - 480 + 180 and mx < GetSystemMetrics(0) / 2 - 480 + 180 + 700 and my > GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 250 and my < GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 250 + 50:
                     if event.type == MOUSEBUTTONDOWN and event.button == 1:
                         editNotificationName = 1
                 if editNotificationName == 1:
                     if event.type == KEYDOWN:
                        if event.key == pygame.K_a:
                            notificationName = notificationName + 'a'
                        if event.key == pygame.K_b:
                            notificationName = notificationName + 'b'
                        if event.key == pygame.K_c:
                            notificationName = notificationName + 'c'
                        if event.key == pygame.K_d:
                            notificationName = notificationName + 'd'
                        if event.key == pygame.K_e:
                            notificationName = notificationName + 'e'
                        if event.key == pygame.K_f:
                            notificationName = notificationName + 'f'
                        if event.key == pygame.K_g:
                            notificationName = notificationName + 'g'
                        if event.key == pygame.K_h:
                            notificationName = notificationName + 'h'
                        if event.key == pygame.K_i:
                            notificationName = notificationName + 'i'
                        if event.key == pygame.K_j:
                            notificationName = notificationName + 'j'
                        if event.key == pygame.K_k:
                            notificationName = notificationName + 'k'
                        if event.key == pygame.K_l:
                            notificationName = notificationName + 'l'
                        if event.key == pygame.K_m:
                            notificationName = notificationName + 'm'
                        if event.key == pygame.K_n:
                            notificationName = notificationName + 'n'
                        if event.key == pygame.K_o:
                            notificationName = notificationName + 'o'
                        if event.key == pygame.K_p:
                            notificationName = notificationName + 'p'
                        if event.key == pygame.K_q:
                            notificationName = notificationName + 'q'
                        if event.key == pygame.K_r:
                            notificationName = notificationName + 'r'
                        if event.key == pygame.K_s:
                            notificationName = notificationName + 's'
                        if event.key == pygame.K_t:
                            notificationName = notificationName + 't'
                        if event.key == pygame.K_u:
                            notificationName = notificationName + 'u'
                        if event.key == pygame.K_v:
                            notificationName = notificationName + 'v'
                        if event.key == pygame.K_w:
                            notificationName = notificationName + 'w'
                        if event.key == pygame.K_x:
                            notificationName = notificationName + 'x'
                        if event.key == pygame.K_y:
                            notificationName = notificationName + 'y'
                        if event.key == pygame.K_z:
                            notificationName = notificationName + 'z'
                        if event.key == pygame.K_SPACE:
                            notificationName = notificationName + ' '
                        if event.key == pygame.K_BACKSPACE:
                            notificationName = notificationName[0:len(notificationName) - 1]
                        pygame.time.delay(65)
                 else:
                    screen.blit(menu_font.render('click me', True, gray),([GetSystemMetrics(0) / 2 - 290, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 250]))                   
                 screen.blit(menu_font.render(''+str(notificationName), True, white),([GetSystemMetrics(0) / 2 - 290, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 250])) 
                 text2 = menu_font.render('Username', True, white)   
                 screen.blit(text2, ((GetSystemMetrics(0) / 2 - 480), GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 250))
                 text2 = menu_font.render('Password', True, white)   
                 screen.blit(text2, ((GetSystemMetrics(0) / 2 - 480), GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 310))
                 pygame.draw.rect(screen, blue2, [GetSystemMetrics(0) / 2 - 480 + 180, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 310, 700, 50])
                 if mx > GetSystemMetrics(0) / 2 - 480 + 180 and mx < GetSystemMetrics(0) / 2 - 480 + 180 + 700 and my > GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 310 and my < GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 310 + 50:
                     if event.type == MOUSEBUTTONDOWN and event.button == 1:
                         editNotificationName = 2
                 if editNotificationName == 2:
                     if event.type == KEYDOWN:
                        if event.key == pygame.K_a:
                            notificationName2 = notificationName2 + 'a'
                        if event.key == pygame.K_b:
                            notificationName2 = notificationName2 + 'b'
                        if event.key == pygame.K_c:
                            notificationName2 = notificationName2 + 'c'
                        if event.key == pygame.K_d:
                            notificationName2 = notificationName2 + 'd'
                        if event.key == pygame.K_e:
                            notificationName2 = notificationName2 + 'e'
                        if event.key == pygame.K_f:
                            notificationName2 = notificationName2 + 'f'
                        if event.key == pygame.K_g:
                            notificationName2 = notificationName2 + 'g'
                        if event.key == pygame.K_h:
                            notificationName2 = notificationName2 + 'h'
                        if event.key == pygame.K_i:
                            notificationName2 = notificationName2 + 'i'
                        if event.key == pygame.K_j:
                            notificationName2 = notificationName2 + 'j'
                        if event.key == pygame.K_k:
                            notificationName2 = notificationName2 + 'k'
                        if event.key == pygame.K_l:
                            notificationName2 = notificationName2 + 'l'
                        if event.key == pygame.K_m:
                            notificationName2 = notificationName2 + 'm'
                        if event.key == pygame.K_n:
                            notificationName2 = notificationName2 + 'n'
                        if event.key == pygame.K_o:
                            notificationName2 = notificationName2 + 'o'
                        if event.key == pygame.K_p:
                            notificationName2 = notificationName2 + 'p'
                        if event.key == pygame.K_q:
                            notificationName2 = notificationName2 + 'q'
                        if event.key == pygame.K_r:
                            notificationName2 = notificationName2 + 'r'
                        if event.key == pygame.K_s:
                            notificationName2 = notificationName2 + 's'
                        if event.key == pygame.K_t:
                            notificationName2 = notificationName2 + 't'
                        if event.key == pygame.K_u:
                            notificationName2 = notificationName2 + 'u'
                        if event.key == pygame.K_v:
                            notificationName2 = notificationName2 + 'v'
                        if event.key == pygame.K_w:
                            notificationName2 = notificationName2 + 'w'
                        if event.key == pygame.K_x:
                            notificationName2 = notificationName2 + 'x'
                        if event.key == pygame.K_y:
                            notificationName2 = notificationName2 + 'y'
                        if event.key == pygame.K_z:
                            notificationName2 = notificationName2 + 'z'
                        if event.key == pygame.K_SPACE:
                            notificationName2 = notificationName2 + ' '
                        if event.key == pygame.K_BACKSPACE:
                            notificationName2 = notificationName2[0:len(notificationName2) - 1]
                        pygame.time.delay(60)
                 else:
                    screen.blit(menu_font.render('click me', True, gray),([GetSystemMetrics(0) / 2 - 290, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 310])) 
                 screen.blit(menu_font.render(''+str(notificationName2), True, white),([GetSystemMetrics(0) / 2 - 290, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 310]))        

                 pygame.draw.rect(screen, blue4, [GetSystemMetrics(0) / 2 - 480, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 400, 210, 50]) 
                 text2 = menu_font.render('sign in!', True, white)       
                 screen.blit(text2, ((GetSystemMetrics(0) / 2 - 480, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 400, 100, 50))) 

                 if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                if mx > GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2 + 100 and mx < GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2 + 100 + 210 and my > GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 400 and my < GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 400 + 50:
                                    usernameS = notificationName
                                    passwordS = notificationName2
                                    if passwordS == password:
                                        if usernameS == username:
                                            rendermode = 'home'
                                    else:
                                        text2 = menu_font.render('Incorrect', True, red)       
                                        screen.blit(text2, ((GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2 + 100, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 500, 100, 50)))                   

                 time_text = app_bar_font.render((time.strftime('%I:%M %p')), True, white)
                 pygame.draw.rect(screen, blue3, [GetSystemMetrics(0) - 400, GetSystemMetrics(1) - 50 , 400, 50])
                 pygame.draw.circle(screen, blue3, (GetSystemMetrics(0) - 400, GetSystemMetrics(1),), 50, 0)  
                 screen.blit(time_text,(GetSystemMetrics(0) - 100, GetSystemMetrics(1) - 30))
                 power_img = pygame.transform.scale(power_img, (25, 25))
                 screen.blit(power_img, (GetSystemMetrics(0) - 160, GetSystemMetrics(1) - 30))
                 question_img = pygame.transform.scale(question_img, (25, 25))
                 screen.blit(question_img, (GetSystemMetrics(0) - 200, GetSystemMetrics(1) - 30))
                 if event.type == MOUSEBUTTONDOWN:
                     if event.button == 1:
                         if mx > GetSystemMetrics(0) - 200 and mx < GetSystemMetrics(0) - 175 and my > GetSystemMetrics(1) - 30 and my < GetSystemMetrics(1) - 5:
                              os.chdir('html')
                              os.startfile('accountHelp.html')
                              os.chdir('..')
                 if event.type == MOUSEBUTTONDOWN:
                     if event.button == 1:
                         if mx > GetSystemMetrics(0) - 160 and mx < GetSystemMetrics(0) - 135 and my > GetSystemMetrics(1) - 30 and my < GetSystemMetrics(1) - 5:
                             menu = 'power'
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
                 pygame.display.update()

    if rendermode == 'shutdown':
        if colorOp == 1:
            if welcomeColor1 == 0 and welcomeColor2 == 0 and welcomeColor3 == 255:
                colorOp = 2
            if welcomeColor1 > 0:
                welcomeColor1 = welcomeColor1 - 1
            if welcomeColor2 > 0:
                welcomeColor2 = welcomeColor2 - 1
            if welcomeColor3 < 255:
                welcomeColor3 = welcomeColor3 + 1
        if colorOp == 2:
            if welcomeColor1 == 40 and welcomeColor2 == 181 and welcomeColor3 == 166:
                colorOp = 1
            if welcomeColor1 < 40:
                welcomeColor1 = welcomeColor1 + 1
            if welcomeColor2 < 181:
                welcomeColor2 = welcomeColor2 + 1
            if welcomeColor3 > 166:
                welcomeColor3 = welcomeColor3 - 1
        screen.fill((welcomeColor1, welcomeColor2, welcomeColor3))
        clock.tick(200)
        mx, my = pygame.mouse.get_pos()

        pygame.draw.rect(screen, blue3, [GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2, GetSystemMetrics(0) / 2, GetSystemMetrics(1) / 2])       

        text2 = big_font.render('Grid OS is shutting down!', True, white)       
        screen.blit(text2, ((GetSystemMetrics(0) / 2 - len('' +str(text2)) * 20), GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 100))
        text2 = menu_font.render('Be sure you saved all your data!', True, white)       
        screen.blit(text2, ((GetSystemMetrics(0) / 2 - len('' +str(text2)) * 20), GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 200))

        pygame.draw.rect(screen, blue4, [GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2 + 100, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 350, 300, 50]) 
        text2 = menu_font.render('Abort shutdown!', True, white)       
        screen.blit(text2, ((GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2 + 100, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 350, 100, 50))) 

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mx > GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2 + 100 and mx < GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2 + 100 + 300 and my > GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 350 and my < GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 350 + 50:
                    shutdown_a = os.system("shutdown -a")
                    if shutdown_a == 1116:
                        rendermode = 'error 1'
                    else:
                        rendermode = 'home'
                        app = 'abort'  

        pygame.display.update()

    if rendermode == 'error 1':
        if colorOp == 1:
            if welcomeColor1 == 0 and welcomeColor2 == 0 and welcomeColor3 == 255:
                colorOp = 2
            if welcomeColor1 > 0:
                welcomeColor1 = welcomeColor1 - 1
            if welcomeColor2 > 0:
                welcomeColor2 = welcomeColor2 - 1
            if welcomeColor3 < 255:
                welcomeColor3 = welcomeColor3 + 1
        if colorOp == 2:
            if welcomeColor1 == 40 and welcomeColor2 == 181 and welcomeColor3 == 166:
                colorOp = 1
            if welcomeColor1 < 40:
                welcomeColor1 = welcomeColor1 + 1
            if welcomeColor2 < 181:
                welcomeColor2 = welcomeColor2 + 1
            if welcomeColor3 > 166:
                welcomeColor3 = welcomeColor3 - 1
        screen.fill((welcomeColor1, welcomeColor2, welcomeColor3))
        clock.tick(200)
        mx, my = pygame.mouse.get_pos()

        pygame.draw.rect(screen, blue3, [GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2 - 150, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2, GetSystemMetrics(0) / 2 + 300, GetSystemMetrics(1) / 2])       

        text2 = big_font.render('Error 1 (1116) no shutdown in progress', True, white)       
        screen.blit(text2, ((GetSystemMetrics(0) / 2 - len('' +str(text2)) * 20) - 150, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 100))
        text2 = menu_font.render('Thats weird? There was no shutdown in progress.', True, white)       
        screen.blit(text2, ((GetSystemMetrics(0) / 2 - len('' +str(text2)) * 20) - 150, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 200))

        pygame.draw.rect(screen, blue4, [GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2 + 100 - 150, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 350, 300, 50]) 
        text2 = menu_font.render('Go back to Grid OS', True, white)       
        screen.blit(text2, ((GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2 + 100 - 150, GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 350, 100, 50))) 

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mx > GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2 + 100 - 150and mx < GetSystemMetrics(0) / 2 - GetSystemMetrics(0) / 2 / 2 + 100 - 150 + 300 and my > GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 350 and my < GetSystemMetrics(1) / 2 - GetSystemMetrics(1) / 2 / 2 + 350 + 50:
                    rendermode = 'home'

        pygame.display.update()        
        

    if rendermode == 'home':
        #settings
        screen.fill(blue2)
        clock.tick(200)
        mx, my = pygame.mouse.get_pos()
        

        fps_text = menu_font.render('FPS:' +str (clock.get_fps()), True, blue4)
    
        #app bar
        #time = str(time)
        time_text = app_bar_font.render((time.strftime('%I:%M %p')), True, white)
        pygame.draw.rect(screen, blue3, [0, 0 , 100, GetSystemMetrics(1)])
        screen.blit(gridtech_logo_img,(10, 10))
        screen.blit(settings_img, (15, 100))
        music_img = pygame.transform.scale(music_img, (64, 64))
        screen.blit(music_img, (15, 190))
        folder_img = pygame.transform.scale(folder_img, (64, 64))
        screen.blit(folder_img, (15, 280))
        #calendar_img = pygame.transform.scale(calendar_img, (64, 64))
        #screen.blit(calendar_img, (15, 370))
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
        #if my > 370 and my < 460:
            #if mx > 15 and mx < 79:
                #infoMenu(100, 370, 'Reminders   ', blue3, white, True)
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
                if my > 190 and my < 254:
                    if mx > 15 and mx < 79:
                        app = 'music'
                #if my > 370 and my < 460:
                 #   if mx > 15 and mx < 79:
                  #      app = 'reminders'
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 3:
                if my > 100 and my < 164:
                    if mx > 15 and mx < 79:
                        menu = 'settings'
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 3:
                if my > 190 and my < 254:
                    if mx > 15 and mx < 79:
                        menu = 'music'
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 3:
                if my > 280 and my < 344:
                    if mx > 15 and mx < 79:
                        menu = 'file explorer'

        if not app == 'home':
            if app == 'shutdown':
                rendermode = 'shutdown'
                #appOpen(500, 50 , 800, 400, blue3, blue4)     
                #text = menu_font.render('LOOKS LIKE GridOS IS SHUTTING DOWN!', True, blue4)           
                #screen.blit(text, (500, 150))    
                #pygame.draw.rect(screen, blue2, [510, 300, 110, 50]) 
                #text = menu_font.render('ABORT', True, blue4)           
                #screen.blit(text, (510, 300))                        
                #if mx > 510 and mx < 510 + 110 and my > 300 and my < 300 + 50:
                 #   if event.type == MOUSEBUTTONDOWN and event.button == 1:
                  #      shutdown_a = os.system("shutdown -a")
                   #     if shutdown_a == 1116:
                    #        app = 'error 1'
                     #   else:
                      #      app = 'abort'
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
            if app == 'music':
                appOpen(200, 50 , GetSystemMetrics(0) - 250,  GetSystemMetrics(1) - 100, blue3, blue4)
                screen.blit(warning_img,(GetSystemMetrics(0) / 2 - 128 + 50,  GetSystemMetrics(1) / 2 - 128 - 256))
                screen.blit(menu_font.render('There are no songs yet!', True, white), (GetSystemMetrics(0) / 2 - 128,  GetSystemMetrics(1) / 2 - 128 + 130))
                screen.blit(menu_font.render('(for copyright reasons)', True, white), (GetSystemMetrics(0) / 2 - 125,  GetSystemMetrics(1) / 2 - 128 + 175))
            if app == 'reminders':
                 appOpen(200, 50 , GetSystemMetrics(0) - 250,  GetSystemMetrics(1) - 100, blue3, blue4)
                 screen.blit(big_font.render('Current reminders:', True, white), (210,  100))
                 screen.blit(menu_font.render('Reminder:', True, white), (210,  170))
                 render = True
                 render_clock = 0
                 while render == True:
                     try:
                         if not reminderList[render_clock] == '':
                            pygame.draw.rect(screen, blue4, [210, 210 + (render_clock * 75), 300, 60]) 
                         text = menu_font.render('' +str(reminderList[render_clock]), True, white)
                         screen.blit(text, (210, 210 + (render_clock * 75)))
                         text = app_bar_font.render('at: ' +str(reminderTimeList[render_clock]), True, white)
                         screen.blit(text, (210, 210 + ((render_clock * 75) + 40)))
                         render_clock = render_clock + 1
                     except:
                         render_clock = 0
                         render = False                
                 pygame.draw.rect(screen, blue2, [900, 100, 100, 50]) 
                 text = menu_font.render('New', True, blue4)           
                 screen.blit(text, (900, 100))                        
                 if mx > 900 and mx < 900 + 100 and my > 100 and my < 100 + 50:
                     if event.type == MOUSEBUTTONDOWN and event.button == 1:
                         app = 'new reminder'
            if app == 'new reminder':
                 appOpen(200, 50 , GetSystemMetrics(0) - 250,  GetSystemMetrics(1) - 100, blue3, blue4)
                 pygame.draw.rect(screen, blue2, [210, 100, 100, 50]) 
                 text = menu_font.render('Back', True, blue4)           
                 screen.blit(text, (210, 100))                        
                 if mx > 210 and mx < 210 + 100 and my > 100 and my < 100 + 50:
                     if event.type == MOUSEBUTTONDOWN and event.button == 1:
                         app = 'reminders'
                 pygame.draw.rect(screen, blue2, [200, 200, 800, 50])
                 if mx > 200 and mx < 200 + 800 and my > 200 and my < 200 + 50:
                     if event.type == MOUSEBUTTONDOWN and event.button == 1:
                         editNotificationName = True
                 if editNotificationName == True:
                     if event.type == KEYDOWN:
                        if event.key == pygame.K_a:
                            notificationName = notificationName + 'a'
                        if event.key == pygame.K_b:
                            notificationName = notificationName + 'b'
                        if event.key == pygame.K_c:
                            notificationName = notificationName + 'c'
                        if event.key == pygame.K_d:
                            notificationName = notificationName + 'd'
                        if event.key == pygame.K_e:
                            notificationName = notificationName + 'e'
                        if event.key == pygame.K_f:
                            notificationName = notificationName + 'f'
                        if event.key == pygame.K_g:
                            notificationName = notificationName + 'g'
                        if event.key == pygame.K_h:
                            notificationName = notificationName + 'h'
                        if event.key == pygame.K_i:
                            notificationName = notificationName + 'i'
                        if event.key == pygame.K_j:
                            notificationName = notificationName + 'j'
                        if event.key == pygame.K_k:
                            notificationName = notificationName + 'k'
                        if event.key == pygame.K_l:
                            notificationName = notificationName + 'l'
                        if event.key == pygame.K_m:
                            notificationName = notificationName + 'm'
                        if event.key == pygame.K_n:
                            notificationName = notificationName + 'n'
                        if event.key == pygame.K_o:
                            notificationName = notificationName + 'o'
                        if event.key == pygame.K_p:
                            notificationName = notificationName + 'p'
                        if event.key == pygame.K_q:
                            notificationName = notificationName + 'q'
                        if event.key == pygame.K_r:
                            notificationName = notificationName + 'r'
                        if event.key == pygame.K_s:
                            notificationName = notificationName + 's'
                        if event.key == pygame.K_t:
                            notificationName = notificationName + 't'
                        if event.key == pygame.K_u:
                            notificationName = notificationName + 'u'
                        if event.key == pygame.K_v:
                            notificationName = notificationName + 'v'
                        if event.key == pygame.K_w:
                            notificationName = notificationName + 'w'
                        if event.key == pygame.K_x:
                            notificationName = notificationName + 'x'
                        if event.key == pygame.K_y:
                            notificationName = notificationName + 'y'
                        if event.key == pygame.K_z:
                            notificationName = notificationName + 'z'
                        if event.key == pygame.K_SPACE:
                            notificationName = notificationName + ' '
                        if event.key == pygame.K_BACKSPACE:
                            notificationName = ''
                        pygame.time.delay(100)
                 screen.blit(menu_font.render(''+str(notificationName), True, white),(200, 200))
                    

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
                menuOpen(100, 100, 3, blue3, white)
                text = menu_font.render('Open', True, white)           
                screen.blit(text, (100, 100))  
                if app == 'settings':    
                    text = menu_font.render('Force Quit', True, white)      
                    screen.blit(text, (100, 150)) 
                else:
                    text = menu_font.render('Force Quit', True, gray)      
                    screen.blit(text, (100, 150)) 
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if mx > 100 and mx < 300:
                        if my > 100 and my < 150:
                            app = 'settings'
                        if my > 150 and my < 200:
                            if app == 'settings': 
                                closeApp = True
                        menu = 'home'
            if menu == 'music':
                menuOpen(100, 190, 3, blue3, white)
                text = menu_font.render('Open', True, white)           
                screen.blit(text, (100, 190))   
                if app == 'music':    
                    text = menu_font.render('Force Quit', True, white)      
                    screen.blit(text, (100, 240)) 
                else:
                    text = menu_font.render('Force Quit', True, gray)      
                    screen.blit(text, (100, 240)) 
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if mx > 100 and mx < 300:
                        if my > 190 and my < 240:
                            app = 'music'
                        if my > 240 and my < 290:
                            if app == 'music': 
                                closeApp = True
                        menu = 'home'
            if menu == 'file explorer':
                menuOpen(100, 280, 3, blue3, white)
                text = menu_font.render('Open', True, white)           
                screen.blit(text, (100, 280))   
                if app == 'file explorer':    
                    text = menu_font.render('Force Quit', True, white)      
                    screen.blit(text, (100, 330)) 
                else:
                    text = menu_font.render('Force Quit', True, gray)      
                    screen.blit(text, (100, 330)) 
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if mx > 100 and mx < 300:
                        if my > 280 and my < 330:
                            app = 'file explorer'
                        if my > 330 and my < 380:
                            if app == 'file explorer': 
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