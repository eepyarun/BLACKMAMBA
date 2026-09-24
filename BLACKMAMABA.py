#HEHE WELCOME TO BLACK MAMBA
import pygame,sys
import mysql.connector
import random as ran
import math
mysql = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'tiger',database = 'blackmamba')
cursor = mysql.cursor()
pygame.init()
screen = pygame.display.set_mode((1000,700))
clock = pygame.time.Clock()
main_font = pygame.font.Font('fonts\\nightcore.ttf',150)
ICON = pygame.image.load('graphics\\AKAGAMES.png')
sub_font = pygame.font.Font('fonts\\nightcore.ttf',22)
guest_font = pygame.font.Font('fonts\\nightcore.ttf',32)
bill_font = pygame.font.Font('fonts\\adrip1.ttf',33)
text_input_font = pygame.font.Font('fonts\\adrip1.ttf',66)
total_font = pygame.font.Font('fonts\\adrip1.ttf',56)
number_font = pygame.font.Font('fonts\\adrip1.TTF',16)
finalprice_font = pygame.font.Font('fonts\\adrip1.ttf',92)
global username, cartlist, cartno, merchandise, total, password,username_input,password_input
username = "guest"
cartno = 0
credentials = []
cartlist = {101:0,102:0,201:0,202:0,203:0,301:0,302:0,303:0}
merchandise = {101:["Classic Shirt",30], 102:["Dark Mode Shirt",30], 201:["Classic Mug",10], 202: ["Cotton Candy Mug",10], 203:["Dragon Fruit Mug",10], 301: ["Lemon Lime Energy Drink",6], 302 : ["Tropical Fruit Energy Drink",6], 303: ["BlueBerry Energy Drink",6]}

def mambacredits():
    global username, cartlist, cartno, merchandise
 
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("CHECKOUT")
    background = pygame.image.load('graphics\\credits.png').convert_alpha()
    
    home = pygame.image.load('graphics\\homebutton.png').convert_alpha()
    home_rect = home.get_rect(topleft = (17,8))

    homehov = pygame.image.load('graphics\\homehov.png').convert_alpha()
    homehov_rect = homehov.get_rect(topleft = (11,8))

    home_big = pygame.image.load('graphics\\home.png').convert_alpha()
    home_big_rect = home_big.get_rect(topleft = (368,565))
    
    username_disp = sub_font.render(username,True, "White")
    username_rect = username_disp.get_rect(topright = (872,7))


    while True:

        screen.blit(background,(0,0))
        screen.blit(home,home_rect)
        screen.blit(username_disp,username_rect)
        screen.blit(home_big,home_big_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if home_rect.collidepoint(event.pos):
                    mamba_main
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if home_big_rect.collidepoint(event.pos):
                    mamba_main()


            pygame.display.update()
            clock.tick(60)

def games_main():
    clock = pygame.time.Clock()
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("MAMBA GAMES")
    background = pygame.image.load('graphics\\arcade.png').convert_alpha()
    
    home = pygame.image.load('graphics\\homebutton.png').convert_alpha()
    home_rect = home.get_rect(topleft = (17,8))
    

    homehov = pygame.image.load('graphics\\homehov.png').convert_alpha()
    homehov_rect = homehov.get_rect(topleft = (11,8))

    george = pygame.image.load('graphics\\george.png').convert_alpha()
    george_rect = george.get_rect(topleft = (112,263 ))

    poppeye = pygame.image.load('graphics\\poppeye.png').convert_alpha()
    poppeye_rect = poppeye.get_rect(topleft = (384,263))

    mambaio = pygame.image.load('graphics\\mambaio.png').convert_alpha()
    mambaio_rect = mambaio.get_rect(topleft = (662,263))
    
    username_disp = sub_font.render(username,True, "White")
    username_rect = username_disp.get_rect(topright = (948,8))



    while True:

        screen.blit(background,(0,0))
        screen.blit(home,home_rect)
        screen.blit(username_disp,username_rect)
        screen.blit(george,george_rect)
        screen.blit(poppeye,poppeye_rect)
        screen.blit(mambaio,mambaio_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if home_rect.collidepoint(event.pos):
                    mamba_main()

            if event.type ==pygame.MOUSEBUTTONDOWN:
                if george_rect.collidepoint(event.pos):
                    controls_george()
                    
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if poppeye_rect.collidepoint(event.pos):
                    controls_poppeye()

            if event.type ==pygame.MOUSEBUTTONDOWN:
                if mambaio_rect.collidepoint(event.pos):
                    controls_mambaio()

        pygame.display.update()
        clock.tick(60) 
    
def controls_poppeye():
    clock = pygame.time.Clock()
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("MAMBA GAMES")
    background = pygame.image.load('graphics\\controls_poppeye.png').convert_alpha()
    

    while True:

        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type ==pygame.KEYDOWN:
                    poppeye_game()

        pygame.display.update()
        clock.tick(60)

def controls_george():
    clock = pygame.time.Clock()
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("GOERGE CONTROLS")
    background = pygame.image.load('graphics\\controls_george.png').convert_alpha()
    

    while True:

        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type ==pygame.KEYDOWN:
                    mambarunner()

        pygame.display.update()
        clock.tick(60)

def controls_mambaio():
    clock = pygame.time.Clock()
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("MAMBA GAMES")
    background = pygame.image.load('graphics\\controls_mambaio.png').convert_alpha()
    

    while True:

        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type ==pygame.KEYDOWN:
                    mambaio_game()

        pygame.display.update()
        clock.tick(60) 


def mamba_main():
    global username, cartlist, cartno, merchandise, total, password
                    


    clock = pygame.time.Clock()
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("MAMBA HOME")
    background = pygame.image.load('graphics\\mamba_login.png').convert_alpha()
    
    home = pygame.image.load('graphics\\homebutton.png').convert_alpha()
    home_rect = home.get_rect(topleft = (17,8))
    

    homehov = pygame.image.load('graphics\\homehov.png').convert_alpha()
    homehov_rect = homehov.get_rect(topleft = (11,8))

    games = pygame.image.load('graphics\\games.png').convert_alpha()
    games_rect = games.get_rect(topleft = (387,238))

    shop = pygame.image.load('graphics\\shop.png').convert_alpha()
    shop_rect = shop.get_rect(topleft = (387,349))

    logout = pygame.image.load('graphics\\log_out.png').convert_alpha()
    logout_rect = logout.get_rect(topleft = (464,450))
    
    username_disp = sub_font.render(username,True, "White")
    username_rect = username_disp.get_rect(topright = (948,8))

    mambacreds = sub_font.render('Credits',True, "White")
    mambacreds_rect = mambacreds.get_rect(topright = (915,650))



    while True:

        screen.blit(background,(0,0))
        screen.blit(home,home_rect)
        screen.blit(username_disp,username_rect)
        screen.blit(games,games_rect)
        screen.blit(shop,shop_rect)
        screen.blit(logout,logout_rect)
        screen.blit(mambacreds,mambacreds_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if shop_rect.collidepoint(event.pos):
                    shop_main()

            if event.type ==pygame.MOUSEBUTTONDOWN:
                if games_rect.collidepoint(event.pos):
                    games_main()

            if event.type ==pygame.MOUSEBUTTONDOWN:
                if mambacreds_rect.collidepoint(event.pos):
                    mambacredits()
                    
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if logout_rect.collidepoint(event.pos):
                    username=''
                    password=''
                    startup()
                    


        pygame.display.update()
        clock.tick(60) 

def mamba_login():
    global username, cartlist, cartno, merchandise, total, password
                    
    text_box1 = pygame.Rect(236,305,529,65)
    text_box2 = pygame.Rect(236,457,529,65)

    active1 = active2= False
    color1 = color2  = pygame.Color('black')
    clock = pygame.time.Clock()
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("CHECKOUT")
    background = pygame.image.load('graphics\\mamba_login.png').convert_alpha()
    
    home = pygame.image.load('graphics\\homebutton.png').convert_alpha()
    home_rect = home.get_rect(topleft = (17,8))
    

    homehov = pygame.image.load('graphics\\homehov.png').convert_alpha()
    homehov_rect = homehov.get_rect(topleft = (11,8))

    signup = pygame.image.load('graphics\\signup_button.png').convert_alpha()
    signup_rect = signup.get_rect(topleft = (387,349))

    signin = pygame.image.load('graphics\\signin_button.png').convert_alpha()
    signin_rect = signin.get_rect(topleft = (387,246))

    contguest = pygame.image.load('graphics\\contguest.png').convert_alpha()
    contguest_rect = contguest.get_rect(topleft = (406,445))
    




    while True:

        screen.blit(background,(0,0))
        screen.blit(home,home_rect)
        screen.blit(homehov,homehov_rect)
        screen.blit(contguest,contguest_rect)
        screen.blit(signup,signup_rect)
        screen.blit(signin,signin_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if signup_rect.collidepoint(event.pos):
                    mamba_signup()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if signin_rect.collidepoint(event.pos):
                    mamba_signin()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if contguest_rect.collidepoint(event.pos):
                    username = "guest"
                    mamba_main()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if home_rect.collidepoint(event.pos):
                    startup()


        pygame.display.update()
        clock.tick(60)
        

def mamba_signin():
    global username, cartlist, cartno, merchandise, total, password,credentials
    
    username_input = ''
    password_input = ''
                     
    text_box1 = pygame.Rect(236,305,529,65)
    text_box2 = pygame.Rect(236,457,529,65)

    active1 = active2= False
    color1 = color2  = pygame.Color('black')
    clock = pygame.time.Clock()
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("CHECKOUT")
    background = pygame.image.load('graphics\\signin.png').convert_alpha()
    
    home = pygame.image.load('graphics\\homebutton.png').convert_alpha()
    home_rect = home.get_rect(topleft = (17,8))
    

    homehov = pygame.image.load('graphics\\homehov.png').convert_alpha()
    homehov_rect = homehov.get_rect(topleft = (11,8))

    confirm = pygame.image.load('graphics\\confirm.png').convert_alpha()
    confirm_rect = confirm.get_rect(topleft = (365,549))
    
    unsuccessful = guest_font.render("Username or Password Incorrect",True,"Red")
    unsuccessful_rect = unsuccessful.get_rect(topleft = (280,643))



    while True:

        screen.blit(background,(0,0))
        screen.blit(home,home_rect)
        screen.blit(confirm,confirm_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if home_rect.collidepoint(event.pos):
                    mamba_login

            if event.type ==pygame.MOUSEBUTTONDOWN:
                if homehov_rect.collidepoint(event.pos):
                    mamba_login()

            if event.type ==pygame.MOUSEBUTTONDOWN:
                if confirm_rect.collidepoint(event.pos):
                    username = username_input.lower()
                    password = password_input
                    if username != '' and password != '':
                        cursor.execute("SELECT * FROM CREDENTIALS")
                        usernames = []
                        a = cursor.fetchall()
                        for i in a:
                            if i[0] == username:
                                if i[1] ==password:
                                    credentials.append(i)
                                    mamba_main()
                                else:
                                    screen.blit(unsuccessful,unsuccessful_rect)
                            usernames.append(i[0])
                        if username not in usernames:
                            screen.blit(unsuccessful,unsuccessful_rect)
                    else:
                        screen.blit(unsuccessful,unsuccessful_rect)
                        
                        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    username = username_input.lower()
                    password = password_input
                    if username != '' and password != '':
                        cursor.execute("SELECT * FROM CREDENTIALS")
                        usernames = []
                        a = cursor.fetchall()
                        for i in a:
                            if i[0] == username:
                                if i[1] ==password:
                                    mamba_main()
                                else:
                                    screen.blit(unsuccessful,unsuccessful_rect)
                            usernames.append(i[0])
                        if username not in usernames:
                            screen.blit(unsuccessful,unsuccessful_rect)
                    else:
                        screen.blit(unsuccessful,unsuccessful_rect)
                      
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box1.collidepoint(event.pos):
                    active1 = True
                else:
                    active1 = False
            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_BACKSPACE:
                        username_input = username_input[:-1]
                    else:
                        username_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box2.collidepoint(event.pos):
                    active2 = True
                else:
                    active2 = False
            if event.type == pygame.KEYDOWN:
                if active2:
                    if event.key == pygame.K_BACKSPACE:
                        password_input = password_input[:-1]
                    else:
                        password_input += event.unicode

                    
        if active1 :
            color1 = pygame.Color('white')
        else:
            color1 = pygame.Color('black')

        if active2:
            color2 = pygame.Color('white')
        else:
            color2 = pygame.Color('black')

            
        pygame.draw.rect(screen,color1, text_box1,4)
        pygame.draw.rect(screen,color2, text_box2,4)

        passworddisp = ('*'*len(password_input))
        
        username = text_input_font.render(username_input,True,'white')
        password = text_input_font.render(passworddisp,True,'white')

        

        
        screen.blit(username, (text_box1.x , text_box1.y))
        screen.blit(password, (text_box2.x , text_box2.y))

        pygame.display.update()
        clock.tick(10)

def mamba_signup():
    global username, cartlist, cartno, merchandise, total, password
    
    username_input = ''
    password_input = ''
                     
    text_box1 = pygame.Rect(236,305,529,65)
    text_box2 = pygame.Rect(236,457,529,65)

    active1 = active2= False
    color1 = color2  = pygame.Color('black')
    clock = pygame.time.Clock()
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("CHECKOUT")
    background = pygame.image.load('graphics\\signup.png').convert_alpha()
    
    home = pygame.image.load('graphics\\homebutton.png').convert_alpha()
    home_rect = home.get_rect(topleft = (17,8))
    

    homehov = pygame.image.load('graphics\\homehov.png').convert_alpha()
    homehov_rect = homehov.get_rect(topleft = (11,8))

    confirm = pygame.image.load('graphics\\confirm.png').convert_alpha()
    confirm_rect = confirm.get_rect(topleft = (365,549))
    
    unsuccessful = guest_font.render("Username or Password Incorrect",True,"Red")
    unsuccessful_rect = unsuccessful.get_rect(topleft = (280,643))

    usernametaken = guest_font.render("username already taken",True,"Red")
    usernametaken_rect = usernametaken.get_rect(topleft = (360,643))



    while True:

        screen.blit(background,(0,0))
        screen.blit(home,home_rect)
        screen.blit(confirm,confirm_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if home_rect.collidepoint(event.pos):
                    mamba_login()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if homehov_rect.collidepoint(event.pos):
                    mamba_login()

            if event.type ==pygame.MOUSEBUTTONDOWN:
                if confirm_rect.collidepoint(event.pos):
                    username = username_input.lower()
                    password = password_input
                    if username != '' and password != '':
                        cursor.execute("SELECT * FROM CREDENTIALS")
                        usernames = []
                        a = cursor.fetchall()
                        mysql.commit()
                        if a == []:
                            cursor.execute("INSERT INTO CREDENTIALS(USERNAME,PASSWORD) VALUES(%s,%s)",(username,password))
                            mysql.commit()
                            cursor.execute("INSERT INTO SCORES(USERNAME) VALUES(%s)",(username,))
                            mysql.commit()
                            mamba_main()
                        for i in a:
                            if i[0] == username or username == 'guest':
                                screen.blit(usernametaken,usernametaken_rect)
                            else:
                                cursor.execute("INSERT INTO CREDENTIALS(USERNAME,PASSWORD) VALUES(%s,%s)",(username,password))
                                mysql.commit()
                                cursor.execute("INSERT INTO SCORES(USERNAME) VALUES(%s)",(username,))
                                mysql.commit()
                                mamba_main()
                    else:
                        screen.blit(unsuccessful,unsuccessful_rect)

                    
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box1.collidepoint(event.pos):
                    active1 = True
                else:
                    active1 = False
            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_BACKSPACE:
                        username_input = username_input[:-1]
                    else:
                        username_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box2.collidepoint(event.pos):
                    active2 = True
                else:
                    active2 = False
            if event.type == pygame.KEYDOWN:
                if active2:
                    if event.key == pygame.K_BACKSPACE:
                        password_input = password_input[:-1]
                    else:
                        password_input += event.unicode

                    
        if active1 :
            color1 = pygame.Color('white')
        else:
            color1 = pygame.Color('black')

        if active2:
            color2 = pygame.Color('white')
        else:
            color2 = pygame.Color('black')

        passworddisp = ('*'*len(password_input))
        pygame.draw.rect(screen,color1, text_box1,4)
        pygame.draw.rect(screen,color2, text_box2,4)

        
        username = text_input_font.render(username_input,True,'white')
        password = text_input_font.render(passworddisp,True,'white')

        
        screen.blit(username, (text_box1.x , text_box1.y))
        screen.blit(password, (text_box2.x , text_box2.y))

        pygame.display.update()
        clock.tick(10)

def success():
    global username, cartlist, cartno, merchandise
    cartno = 0
    cartlist = {101:0,102:0,201:0,202:0,203:0,301:0,302:0,303:0}
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("CHECKOUT")
    background = pygame.image.load('graphics\\end_screen.png').convert_alpha()
    
    home = pygame.image.load('graphics\\homebutton.png').convert_alpha()
    home_rect = home.get_rect(topleft = (17,8))
    
    cartmain = pygame.image.load('graphics\\cart.png').convert_alpha()
    cartmain_rect = cartmain.get_rect(topleft = (882,8))

    homehov = pygame.image.load('graphics\\homehov.png').convert_alpha()
    homehov_rect = homehov.get_rect(topleft = (11,8))

    home_big = pygame.image.load('graphics\\home.png').convert_alpha()
    home_big_rect = home_big.get_rect(topleft = (368,565))
    


    username_disp = sub_font.render(username,True, "White")
    username_rect = username_disp.get_rect(topright = (872,7))

    cartnumber = number_font.render(str(cartno),True,"White")
    cartnumber_rect = cartnumber.get_rect(center = (902,26))

    while True:

        screen.blit(background,(0,0))
        screen.blit(home,home_rect)
        screen.blit(cartmain,cartmain_rect)
        screen.blit(username_disp,username_rect)
        screen.blit(cartnumber,cartnumber_rect)
        screen.blit(home_big,home_big_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if home_rect.collidepoint(event.pos):
                    shop_main()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if home_big_rect.collidepoint(event.pos):
                    shop_main()


            pygame.display.update()
            clock.tick(60)

def checkout_address():
    global username, cartlist, cartno, merchandise, total
    
    email_input = ''
    address_input = ''
    phoneno_input = ''
                     
    text_box1 = pygame.Rect(87,302,529,65)
    text_box2 = pygame.Rect(87,423,529,65)
    text_box3 = pygame.Rect(87,547,529,65)

    active1 = active2= active3= False
    color1 = color2 = color3 = pygame.Color('black')
    clock = pygame.time.Clock()
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("CHECKOUT")
    background = pygame.image.load('graphics\\checkout_address.png').convert_alpha()
    
    home = pygame.image.load('graphics\\homebutton.png').convert_alpha()
    home_rect = home.get_rect(topleft = (17,8))
    
    cartmain = pygame.image.load('graphics\\cart.png').convert_alpha()
    cartmain_rect = cartmain.get_rect(topleft = (882,8))

    homehov = pygame.image.load('graphics\\homehov.png').convert_alpha()
    homehov_rect = homehov.get_rect(topleft = (11,8))

    confirm = pygame.image.load('graphics\\confirm.png').convert_alpha()
    confirm_rect = confirm.get_rect(topleft = (686,534))

    savedet = pygame.image.load('graphics\\savedetails.png').convert_alpha()
    savedet_rect = savedet.get_rect(topleft = (686,412))
    

    username_disp = sub_font.render(username,True, "White")
    username_rect = username_disp.get_rect(topright = (872,7))

    cartnumber = number_font.render(str(cartno),True,"White")
    cartnumber_rect = cartnumber.get_rect(center = (902,26))

    price =  finalprice_font.render(str(total),True,"White")
    price_rect = price.get_rect(topleft = (689,292))




    while True:

        screen.blit(background,(0,0))
        screen.blit(home,home_rect)
        screen.blit(cartmain,cartmain_rect)
        screen.blit(username_disp,username_rect)
        screen.blit(cartnumber,cartnumber_rect)
        screen.blit(price,price_rect)
        screen.blit(confirm,confirm_rect)
        if username != 'guest':
            screen.blit(savedet,savedet_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if home_rect.collidepoint(event.pos):
                    shop_main()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if confirm_rect.collidepoint(event.pos):
                    success()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if savedet_rect.collidepoint(event.pos):
                    if username != 'guest':
                        cursor.execute("UPDATE CREDENTIALS SET ADDRESS = %s, EMAIL = %s, PHONENO = %s, CCNO = %s,EXPIRYDATE = %s, CVV = %s WHERE USERNAME = %s ",(address_input,email_input,int(phoneno_input),creditno_input,creditexpiry_input,creditcvv_input,username))
                        mysql.commit()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box1.collidepoint(event.pos):
                    active1 = True
                else:
                    active1 = False
            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_BACKSPACE:
                        address_input = address_input[:-1]
                    else:
                        address_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box2.collidepoint(event.pos):
                    active2 = True
                else:
                    active2 = False
            if event.type == pygame.KEYDOWN:
                if active2:
                    if event.key == pygame.K_BACKSPACE:
                        email_input = email_input[:-1]
                    else:
                        email_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box3.collidepoint(event.pos):
                    active3 = True
                else:
                    active3 = False
            if event.type == pygame.KEYDOWN:
                if active3:
                    if event.key == pygame.K_BACKSPACE:
                        phoneno_input = phoneno_input[:-1]
                    else:
                        phoneno_input += event.unicode

                    
        if active1 :
            color1 = pygame.Color('white')
        else:
            color1 = pygame.Color('black')

        if active2:
            color2 = pygame.Color('white')
        else:
            color2 = pygame.Color('black')

        if active3:
            color3 = pygame.Color('white')
        else:
            color3 = pygame.Color('black')
            
        pygame.draw.rect(screen,color1, text_box1,4)
        pygame.draw.rect(screen,color2, text_box2,4)
        pygame.draw.rect(screen,color3, text_box3,4)
        
        address = text_input_font.render(address_input,True,'white')
        email = text_input_font.render(email_input,True,'white')
        phoneno = text_input_font.render(phoneno_input,True,'white')
        
        screen.blit(address, (text_box1.x , text_box1.y))
        screen.blit(email, (text_box2.x , text_box2.y))
        screen.blit(phoneno, (text_box3.x , text_box3.y))

        pygame.display.update()
        clock.tick(60)



def saved_checkout():
    global username, cartlist, cartno, merchandise, total
    

    clock = pygame.time.Clock()
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("CHECKOUT")
    background = pygame.image.load('graphics\\savecheckout.png').convert_alpha()
    
    home = pygame.image.load('graphics\\homebutton.png').convert_alpha()
    home_rect = home.get_rect(topleft = (17,8))
    
    cartmain = pygame.image.load('graphics\\cart.png').convert_alpha()
    cartmain_rect = cartmain.get_rect(topleft = (882,8))

    homehov = pygame.image.load('graphics\\homehov.png').convert_alpha()
    homehov_rect = homehov.get_rect(topleft = (11,8))

    yes = pygame.image.load('graphics\\saveyes.png').convert_alpha()
    yes_rect = yes.get_rect(topleft = (191,565))

    no = pygame.image.load('graphics\\saveno.png').convert_alpha()
    no_rect = no.get_rect(topleft = (540,567))

    

    username_disp = sub_font.render(username,True, "White")
    username_rect = username_disp.get_rect(topright = (872,7))

    cartnumber = number_font.render(str(cartno),True,"White")
    cartnumber_rect = cartnumber.get_rect(center = (902,26))

    price =  finalprice_font.render(str(total),True,"White")
    price_rect = price.get_rect(topleft = (689,292))




    while True:

        screen.blit(background,(0,0))
        screen.blit(home,home_rect)
        screen.blit(cartmain,cartmain_rect)
        screen.blit(username_disp,username_rect)
        screen.blit(cartnumber,cartnumber_rect)
        screen.blit(price,price_rect)
        screen.blit(yes,yes_rect)
        screen.blit(no,no_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if home_rect.collidepoint(event.pos):
                    shop_main()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if yes_rect.collidepoint(event.pos):
                    success()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if no_rect.collidepoint(event.pos):
                    checkout_credit()
                    

        pygame.display.update()
        clock.tick(60)


def checkout_credit():
    global username, cartlist, cartno, merchandise, total, creditno_input, creditexpiry_input,creditcvv_input
    
    creditno_input = ''
    creditexpiry_input = ''
    creditcvv_input = ''
                     
    text_box1 = pygame.Rect(87,302,529,65)
    text_box2 = pygame.Rect(87,423,529,65)
    text_box3 = pygame.Rect(87,547,529,65)

    active1 = active2= active3= False
    color1 = color2 = color3 = pygame.Color('black')
    clock = pygame.time.Clock()
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("CHECKOUT")
    background = pygame.image.load('graphics\\checkout_credit.png').convert_alpha()
    
    home = pygame.image.load('graphics\\homebutton.png').convert_alpha()
    home_rect = home.get_rect(topleft = (17,8))
    
    cartmain = pygame.image.load('graphics\\cart.png').convert_alpha()
    cartmain_rect = cartmain.get_rect(topleft = (882,8))

    homehov = pygame.image.load('graphics\\homehov.png').convert_alpha()
    homehov_rect = home.get_rect(topleft = (11,8))

    placeorder = pygame.image.load('graphics\\place_order.png').convert_alpha()
    placeorder_rect = placeorder.get_rect(topleft = (686,477))
    

    username_disp = sub_font.render(username,True, "White")
    username_rect = username_disp.get_rect(topright = (872,7))

    cartnumber = number_font.render(str(cartno),True,"White")
    cartnumber_rect = cartnumber.get_rect(center = (902,26))

    price = finalprice_font.render(str(total),True,"White")
    price_rect = price.get_rect(topleft = (689,292))

    creditno = text_input_font.render(str(creditno_input),True,"White")
    creditno_rect = creditno.get_rect(topleft = (119,302))


    while True:

        screen.blit(background,(0,0))
        screen.blit(home,home_rect)
        screen.blit(cartmain,cartmain_rect)
        screen.blit(username_disp,username_rect)
        screen.blit(cartnumber,cartnumber_rect)
        screen.blit(price,price_rect)
        screen.blit(placeorder,placeorder_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if home_rect.collidepoint(event.pos):
                    shop_main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if placeorder_rect.collidepoint(event.pos):
                    checkout_address()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box1.collidepoint(event.pos):
                    active1 = True
                else:
                    active1 = False
            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_BACKSPACE:
                        creditno_input = creditno_input[:-1]
                    else:
                        creditno_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box2.collidepoint(event.pos):
                    active2 = True
                else:
                    active2 = False
            if event.type == pygame.KEYDOWN:
                if active2:
                    if event.key == pygame.K_BACKSPACE:
                        creditexpiry_input = creditexpiry_input[:-1]
                    else:
                        creditexpiry_input += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box3.collidepoint(event.pos):
                    active3 = True
                else:
                    active3 = False
            if event.type == pygame.KEYDOWN:
                if active3:
                    if event.key == pygame.K_BACKSPACE:
                        creditcvv_input = creditcvv_input[:-1]
                    else:
                        creditcvv_input += event.unicode

                    
        if active1 :
            color1 = pygame.Color('white')
        else:
            color1 = pygame.Color('black')

        if active2:
            color2 = pygame.Color('white')
        else:
            color2 = pygame.Color('black')

        if active3:
            color3 = pygame.Color('white')
        else:
            color3 = pygame.Color('black')
            
        pygame.draw.rect(screen,color1, text_box1,4)
        pygame.draw.rect(screen,color2, text_box2,4)
        pygame.draw.rect(screen,color3, text_box3,4)
        
        creditno = text_input_font.render(creditno_input,True,'white')
        creditexpiry = text_input_font.render(creditexpiry_input,True,'white')
        creditcvv = text_input_font.render(creditcvv_input,True,'white')
        
        screen.blit(creditno, (text_box1.x , text_box1.y))
        screen.blit(creditexpiry, (text_box2.x , text_box2.y))
        screen.blit(creditcvv, (text_box3.x , text_box3.y))

        pygame.display.update()
        clock.tick(60)

def emptybill():
    global username, cartlist, cartno, merchandise
    finalbill=[]
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("CHECKOUT")
    background = pygame.image.load('graphics\\checkoutbill.png').convert_alpha()
    
    home = pygame.image.load('graphics\\homebutton.png').convert_alpha()
    home_rect = home.get_rect(topleft = (17,8))
    
    cartmain = pygame.image.load('graphics\\cart.png').convert_alpha()
    cartmain_rect = cartmain.get_rect(topleft = (882,8))

    homehov = pygame.image.load('graphics\\homehov.png').convert_alpha()
    homehov_rect = home.get_rect(topleft = (11,8))
    
    checkout = pygame.image.load('graphics\\checkout.png').convert_alpha()
    checkout_rect = home.get_rect(topleft = (626,635))

    clearcart = pygame.image.load('graphics\\clearcart.png').convert_alpha()
    clearcart_rect = home.get_rect(topleft = (774,203))


    username_disp = sub_font.render(username,True, "White")
    username_rect = username_disp.get_rect(topright = (872,7))

    cartnumber = number_font.render(str(cartno),True,"White")
    cartnumber_rect = cartnumber.get_rect(center = (902,26))

    cartitem_top = 285
    total = 0
    a = x = 0
    


    while True:

        screen.blit(background,(0,0))
        screen.blit(home,home_rect)
        screen.blit(cartmain,cartmain_rect)
        screen.blit(username_disp,username_rect)
        screen.blit(cartnumber,cartnumber_rect)
        screen.blit(checkout,checkout_rect)
        screen.blit(clearcart,clearcart_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if home_rect.collidepoint(event.pos):
                    shop_main()
            if event.type ==pygame.MOUSEMOTION:
                if home_rect.collidepoint(event.pos):
                    screen.blit(homehov,homehov_rect)
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if clearcart_rect.collidepoint(event.pos):
                    cartno = 0
                    for i in cartlist:
                        cartlist[i] = 0
            


            pygame.display.update()
            clock.tick(60)


def checkout_bill():
    global username, cartlist, cartno, merchandise, total, credentials
    finalbill=[]
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("CHECKOUT")
    background = pygame.image.load('graphics\\checkoutbill.png').convert_alpha()
    
    home = pygame.image.load('graphics\\homebutton.png').convert_alpha()
    home_rect = home.get_rect(topleft = (17,8))
    
    cartmain = pygame.image.load('graphics\\cart.png').convert_alpha()
    cartmain_rect = cartmain.get_rect(topleft = (882,8))

    homehov = pygame.image.load('graphics\\homehov.png').convert_alpha()
    homehov_rect = home.get_rect(topleft = (11,8))
    
    checkout = pygame.image.load('graphics\\checkout.png').convert_alpha()
    checkout_rect = home.get_rect(topleft = (626,635))

    clearcart = pygame.image.load('graphics\\clearcart.png').convert_alpha()
    clearcart_rect = home.get_rect(topleft = (774,203))

    username_disp = sub_font.render(username,True, "White")
    username_rect = username_disp.get_rect(topright = (872,7))

    cartnumber = number_font.render(str(cartno),True,"White")
    cartnumber_rect = cartnumber.get_rect(center = (902,26))

    cartitem_top = 285
    total = 0
    w8 = x = 0
    


    while True:

        screen.blit(background,(0,0))
        screen.blit(home,home_rect)
        screen.blit(cartmain,cartmain_rect)
        screen.blit(username_disp,username_rect)
        screen.blit(cartnumber,cartnumber_rect)
        screen.blit(checkout,checkout_rect)
        screen.blit(clearcart,clearcart_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if home_rect.collidepoint(event.pos):
                    shop_main()
            if event.type ==pygame.MOUSEMOTION:
                if home_rect.collidepoint(event.pos):
                    screen.blit(homehov,homehov_rect)
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if clearcart_rect.collidepoint(event.pos):
                    cartno = 0
                    for i in cartlist:
                        cartlist[i] = 0
                    emptybill()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if checkout_rect.collidepoint(event.pos):
                    if username != 'guest':
                        cursor.execute("SELECT * FROM CREDENTIALS WHERE USERNAME = %s",(username,))
                        a =cursor.fetchall()
                        if a[0][2] != None:
                            saved_checkout()
                        else:
                            checkout_credit()
                    else:
                        checkout_credit()
            

        #printing the items in the bill
        while w8 != 8:
            for i in cartlist:
                if cartlist[i] != 0 :

                    cartitemno = i
                    cartitemname = merchandise[i][0]
                    cartitemprice = merchandise[i][1]
                    cartitemqty = cartlist[i]
                    cartitemtotal = merchandise[i][1]*cartlist[i]

                    finalbill.append([cartitemno,cartitemname,cartitemprice,cartitemqty,cartitemtotal])
                    total += cartitemtotal                    
                w8 +=1

                    
        if x != len(finalbill):
            for i in finalbill:   
                cartitemno = bill_font.render(str(i[0]),True,"White")
                cartitemno_rect = cartitemno.get_rect(center = (75,cartitem_top))

                cartitemname = bill_font.render(str(i[1]),True,"White")
                cartitemname_rect = cartitemname.get_rect(topleft = (193,cartitem_top - 20))

                cartitemprice = bill_font.render(str(i[2]),True,"White")
                cartitemprice_rect = cartitemprice.get_rect(center = (516,cartitem_top))

                cartitemqty = bill_font.render(str(i[3]),True,"White")
                cartitemqty_rect = cartitemqty.get_rect(center = (631,cartitem_top))

                cartitemtotal = bill_font.render(str(i[4]),True,"White")
                cartitemtotal_rect = cartitemtotal.get_rect(center = (881,cartitem_top))

                totalprice = total_font.render(str(total),True,"White")
                totalprice_rect = totalprice.get_rect(topleft = (456,627))

                dirhams = total_font.render("AED",True,"White")
                dirhams_rect = totalprice.get_rect(topleft = (538,627))

                
                        
                
                    
                screen.blit(cartitemno,cartitemno_rect)
                screen.blit(cartitemname,cartitemname_rect)
                screen.blit(cartitemprice,cartitemprice_rect)
                screen.blit(cartitemqty,cartitemqty_rect)
                screen.blit(cartitemtotal,cartitemtotal_rect)
                screen.blit(totalprice,totalprice_rect)
                screen.blit(dirhams,dirhams_rect)
                pygame.display.update()

                

                               
                x+=1
                cartitem_top +=45
        
            
        clock.tick(60)



    
    

def shop_shirt():
    global username, cartlist, cartno, merchandise
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("SHIRT SHOP")
    background = pygame.image.load('graphics\\shopshirts.png').convert_alpha()
    
    cart1 = pygame.image.load('graphics\\addtocart.png').convert_alpha()
    cart1_rect = cart1.get_rect(topleft = (278,622))
    
    cart2 = pygame.image.load('graphics\\addtocart.png').convert_alpha()
    cart2_rect = cart2.get_rect(topleft = (566,622))
    
    home = pygame.image.load('graphics\\homebutton.png').convert_alpha()
    home_rect = home.get_rect(topleft = (17,8))
    
    cartmain = pygame.image.load('graphics\\cart.png').convert_alpha()
    cartmain_rect = cartmain.get_rect(topleft = (882,8))

    homehov = pygame.image.load('graphics\\homehov.png').convert_alpha()
    homehov_rect = home.get_rect(topleft = (11,8))

    username_disp = sub_font.render(username,True, "White")
    username_rect = username_disp.get_rect(topright = (872,7))

    cartnumber = number_font.render(str(cartno),True,"White")
    cartnumber_rect = cartnumber.get_rect(center = (902,26))

    


    while True:

        screen.blit(background,(0,0))
        screen.blit(home,home_rect)
        screen.blit(cart1,cart1_rect)
        screen.blit(cart2,cart2_rect)
        screen.blit(cartmain,cartmain_rect)
        screen.blit(username_disp,username_rect)
        screen.blit(cartnumber,cartnumber_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if home_rect.collidepoint(event.pos):
                    shop_main()
            if event.type ==pygame.MOUSEMOTION:
                if home_rect.collidepoint(event.pos):
                    screen.blit(homehov,homehov_rect)
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if cart1_rect.collidepoint(event.pos):
                    cartno+=1
                    cartlist[101]+=1
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if cart2_rect.collidepoint(event.pos):
                    cartno+=1
                    cartlist[102]+=1
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if cartmain_rect.collidepoint(event.pos):
                    checkout_bill()
                    

                    
        

        pygame.display.update()
        clock.tick(60)
    
def shop_energy():
    global username, cartlist, cartno, merchandise
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("ENERGY SHOP")
    background = pygame.image.load('graphics\\shopenergy.png').convert_alpha()
    
    cart1 = pygame.image.load('graphics\\addtocart.png').convert_alpha()
    cart1_rect = cart1.get_rect(topleft = (135,613))
    
    cart2 = pygame.image.load('graphics\\addtocart.png').convert_alpha()
    cart2_rect = cart2.get_rect(topleft = (423,613))
    
    cart3 = pygame.image.load('graphics\\addtocart.png').convert_alpha()
    cart3_rect = cart3.get_rect(topleft = (720,613))
    
    home = pygame.image.load('graphics\\homebutton.png').convert_alpha()
    home_rect = home.get_rect(topleft = (17,8))
    
    homehov = pygame.image.load('graphics\\homehov.png').convert_alpha()
    homehov_rect = home.get_rect(topleft = (11,8))
    
    cartmain = pygame.image.load('graphics\\cart.png').convert_alpha()
    cartmain_rect = cartmain.get_rect(topleft = (882,8))

    username_disp = sub_font.render(username,True, "White")
    username_rect = username_disp.get_rect(topright = (872,7))

    cartnumber = number_font.render(str(cartno),True,"White")
    cartnumber_rect = cartnumber.get_rect(center = (902,26))
    
    while True:

        screen.blit(background,(0,0))
        screen.blit(home,home_rect)
        screen.blit(cart1,cart1_rect)
        screen.blit(cart2,cart2_rect)
        screen.blit(cart3,cart3_rect)
        screen.blit(cartmain,cartmain_rect)
        screen.blit(username_disp,username_rect)
        screen.blit(cartnumber,cartnumber_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if home_rect.collidepoint(event.pos):
                    shop_main()
            if event.type ==pygame.MOUSEMOTION:
                if home_rect.collidepoint(event.pos):
                    screen.blit(homehov,homehov_rect)
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if cart1_rect.collidepoint(event.pos):
                    cartno+=1
                    cartlist[301]+=1
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if cart2_rect.collidepoint(event.pos):
                    cartno+=1
                    cartlist[302]+=1
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if cart3_rect.collidepoint(event.pos):
                    cartno+=1
                    cartlist[303]+=1
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if cartmain_rect.collidepoint(event.pos):
                    checkout_bill()

                    
        

        pygame.display.update()
        clock.tick(60)

def shop_mugs():
    global username, cartlist, cartno, merchandise
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("MUG SHOP")
    background = pygame.image.load('graphics\\shopmugs.png').convert_alpha()
    
    cart1 = pygame.image.load('graphics\\addtocart.png').convert_alpha()
    cart1_rect = cart1.get_rect(topleft = (135,613))
    
    cart2 = pygame.image.load('graphics\\addtocart.png').convert_alpha()
    cart2_rect = cart2.get_rect(topleft = (423,613))
    
    cart3 = pygame.image.load('graphics\\addtocart.png').convert_alpha()
    cart3_rect = cart3.get_rect(topleft = (720,613))
    
    home = pygame.image.load('graphics\\homebutton.png').convert_alpha()
    home_rect = home.get_rect(topleft = (17,8))

    homehov = pygame.image.load('graphics\\homehov.png').convert_alpha()
    homehov_rect = home.get_rect(topleft = (11,8))
    
    cartmain = pygame.image.load('graphics\\cart.png').convert_alpha()
    cartmain_rect = cartmain.get_rect(topleft = (882,8))

    username_disp = sub_font.render(username,True, "White")
    username_rect = username_disp.get_rect(topright = (872,7))

    cartnumber = number_font.render(str(cartno),True,"White")
    cartnumber_rect = cartnumber.get_rect(center = (902,26))
    
    while True:
        
        screen.blit(background,(0,0))
        screen.blit(home,home_rect)
        screen.blit(cart1,cart1_rect)
        screen.blit(cart2,cart2_rect)
        screen.blit(cart3,cart3_rect)
        screen.blit(cartmain,cartmain_rect)
        screen.blit(username_disp,username_rect)
        screen.blit(cartnumber,cartnumber_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if home_rect.collidepoint(event.pos):
                    shop_main()
            if event.type ==pygame.MOUSEMOTION:
                if home_rect.collidepoint(event.pos):
                    screen.blit(homehov,homehov_rect)#ARUN IS SUCH A DUMB GUY AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHAA
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if cart1_rect.collidepoint(event.pos):
                    cartno+=1
                    cartlist[201]+=1
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if cart2_rect.collidepoint(event.pos):
                    cartno+=1
                    cartlist[202]+=1
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if cart3_rect.collidepoint(event.pos):
                    cartno+=1
                    cartlist[203]+=1
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if cartmain_rect.collidepoint(event.pos):
                    checkout_bill()
                    
        

        pygame.display.update()
        clock.tick(60)
    
def warning():
    global username, cartlist, cartno, merchandise,scales,scales_rect
    pygame.display.set_caption("MAMBA ARCADE")
    pygame.display.set_icon(ICON)
    background = pygame.image.load('graphics\\warning.png').convert_alpha()
    a = 0
    while True:
        a+=2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if a==10:
            startup()
            
        screen.blit(background,(0,0))

        pygame.display.update()
        clock.tick(1)
        
def startup():
    global username, cartlist, cartno, merchandise,scales,scales_rect
    pygame.display.set_caption("MAMBA ARCADE")
    pygame.display.set_icon(ICON)
    background = pygame.image.load('graphics\\startup.png').convert_alpha()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                mamba_login()
            if event.type ==pygame.KEYDOWN:
                mamba_login()
            
        screen.blit(background,(0,0))

        pygame.display.update()
        clock.tick(60)


def shop_main():
    global username, cartlist, cartno, merchandise
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("MAMBA SHOP")
    background = pygame.image.load('graphics\\shopmain.png').convert_alpha()
    
    shirt = pygame.image.load('graphics\\shirt.png').convert_alpha()
    shirt_rect = shirt.get_rect(topleft = (112,263))
    
    mugs = pygame.image.load('graphics\\mugs.png').convert_alpha()
    mugs_rect = mugs.get_rect(topleft = (384,263))
    
    energydrinks = pygame.image.load('graphics\\energydrinks.png').convert_alpha()
    energydrinks_rect = energydrinks.get_rect(topleft = (662,263))
    
    home = pygame.image.load('graphics\\homebutton.png').convert_alpha()
    home_rect = home.get_rect(topleft = (17,8))

    homehov = pygame.image.load('graphics\\homehov.png').convert_alpha()
    homehov_rect = home.get_rect(topleft = (11,8))

    cartmain = pygame.image.load('graphics\\cart.png').convert_alpha()
    cartmain_rect = cartmain.get_rect(topleft = (882,8))

    username_disp = sub_font.render(username,True, "White")
    username_rect = username_disp.get_rect(topright = (872,7))
    
    cartnumber = number_font.render(str(cartno),True,"White")
    cartnumber_rect = cartnumber.get_rect(center = (902,26))
    

    while True:
        
        screen.blit(background,(0,0))
        screen.blit(home,home_rect)
        screen.blit(shirt,shirt_rect)
        screen.blit(mugs,mugs_rect)
        screen.blit(energydrinks,energydrinks_rect)
        screen.blit(cartmain,cartmain_rect)
        screen.blit(username_disp,username_rect)
        screen.blit(cartnumber,cartnumber_rect)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if home_rect.collidepoint(event.pos):
                    mamba_main()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if shirt_rect.collidepoint(event.pos):
                    shop_shirt()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if mugs_rect.collidepoint(event.pos):
                    shop_mugs()
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if energydrinks_rect.collidepoint(event.pos):
                    shop_energy()
            if event.type ==pygame.MOUSEMOTION:
                if home_rect.collidepoint(event.pos):
                    screen.blit(homehov,homehov_rect)
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if cartmain_rect.collidepoint(event.pos):
                    checkout_bill()
            mysql.commit()
                    
        

        pygame.display.update()
        clock.tick(60)

def mambarunner():
    global username
    pygame.display.set_icon(ICON)
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('MAMBARUN')
    score_font = pygame.font.Font('fonts\\adrip1.ttf',73)

    run1 = pygame.image.load('graphics/run1.png').convert_alpha()
    run2 = pygame.image.load('graphics/run2.png').convert_alpha()
    jump_image = pygame.image.load('graphics/jump.png').convert_alpha()

    back = pygame.image.load('graphics/backgames.png').convert_alpha()

    playagainrunner = pygame.image.load('graphics/playagain.png').convert_alpha()
    savescore = pygame.image.load('graphics/savescore.png').convert_alpha()
    gamescore = pygame.image.load('graphics/score.png').convert_alpha()
    playagainrunner_rect = playagainrunner.get_rect(topleft = (365,395))
    gamescore_rect = gamescore.get_rect(topleft = (285,230))
    savescore_rect = savescore.get_rect(topleft = (418,152))
    back_rect = back.get_rect(topleft = (428,499))

    runnerendscreen = pygame.image.load('graphics/runnerendscreen.png').convert_alpha()
    runnerendscreen_rect = runnerendscreen.get_rect(topleft = (0,0))

    player_images = [run1, run2]
    player_index = 0
    player_image = player_images[player_index]
    player_rect = player_image.get_rect(midbottom=(150, 580))
    player_y_velocity = 0
    is_jumping = False

    bird = pygame.image.load('graphics/bird.png').convert_alpha()

    spike= pygame.image.load('graphics/spike.png').convert_alpha()

    background_x = 0
    background = pygame.image.load('graphics/download.jpg').convert_alpha()
    background_rect = background.get_rect(topleft = (background_x,0))


    clock = pygame.time.Clock()
    gravity = 1 
    jump_strength = -30
    obstacle_speed = 7
    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer, 1500)  
    obstacles = []
    global score
    score = scoretime = 0
    font = pygame.font.Font(None, 36)

    def endgame():
        global score
        scored = str(score)
        scoredisp = score_font.render(scored,True,'White')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type ==pygame.MOUSEBUTTONDOWN:
                    if back_rect.collidepoint(event.pos):
                        games_main()
                if event.type ==pygame.MOUSEBUTTONDOWN:
                    if playagainrunner_rect.collidepoint(event.pos):
                        mambarunner()
                if event.type ==pygame.MOUSEBUTTONDOWN:
                    if savescore_rect.collidepoint(event.pos):
                        cursor.execute("UPDATE SCORES SET GEORGERUNS = %s WHERE USERNAME = %s", (score, username))
                        mysql.commit()



            screen.blit(runnerendscreen,runnerendscreen_rect)
            screen.blit(playagainrunner,playagainrunner_rect)
            screen.blit(back,back_rect)
            screen.blit(gamescore,gamescore_rect)
            screen.blit(scoredisp,(505,230))
            if username != 'guest':
                screen.blit(savescore,savescore_rect)



            pygame.display.update()
            clock.tick(60)

    def create_obstacle():
        if ran.choice(['bird', 'spike']) == 'bird':
            obstacle_rect = bird.get_rect(midbottom=(ran.randint(1100, 1300), ran.randint(400, 550)))
        else:
            obstacle_rect = spike.get_rect(midbottom=(ran.randint(1100, 1300), 580))
        obstacles.append(obstacle_rect)

    def move_obstacles(obstacles):
        for obstacle in obstacles:
            obstacle.x -= obstacle_speed
        obstacles = [obstacle for obstacle in obstacles if obstacle.x > -50]
        return obstacles

    def draw_obstacles(obstacles):
        for obstacle in obstacles:
            if obstacle.bottom < 580:
                screen.blit(bird, obstacle)
            else:
                screen.blit(spike, obstacle)

    def check_collision(obstacles):
        for obstacle in obstacles:
            if player_rect.colliderect(obstacle):
                return False
        return True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == obstacle_timer:
                create_obstacle()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and player_rect.bottom >= 580:
            is_jumping = True
            player_y_velocity = jump_strength

        if is_jumping:
            player_y_velocity += gravity
            player_rect.y += player_y_velocity
            if player_rect.bottom >= 580:
                player_rect.bottom = 580
                is_jumping = False

        if not is_jumping:
            player_index += 0.1  
            if player_index >= len(player_images):
                player_index = 0
            player_image = player_images[int(player_index)]
        else:
            player_image = jump_image 

        obstacles = move_obstacles(obstacles)
        screen.blit(background,background_rect)
        draw_obstacles(obstacles)

        game_active = check_collision(obstacles)
        if not game_active:
            endgame()

        background_x+=-10


        screen.blit(player_image, player_rect)

        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (850, 10))
        scoretime += 0.16
        score = int(scoretime)

        pygame.display.update()
        clock.tick(60)


def poppeye_game():
    def poppeye_end():
        score_font = pygame.font.Font('fonts\\adrip1.ttf',73)
        back = pygame.image.load('graphics/backgames.png').convert_alpha()
        playagain = pygame.image.load('graphics/playagain.png').convert_alpha()
        savescore = pygame.image.load('graphics/savescore.png').convert_alpha()
        gamescore = pygame.image.load('graphics/score.png').convert_alpha()
        savescore = pygame.image.load('graphics/savescore.png').convert_alpha()
        playagain_rect = playagain.get_rect(topleft = (365,395))
        gamescore_rect = gamescore.get_rect(topleft = (285,230))
        savescore_rect = savescore.get_rect(topleft = (418,152))
        back_rect = back.get_rect(topleft = (428,499))
        poppeye_end = pygame.image.load('graphics/poppeye_end.png').convert_alpha()
        poppeye_end_rect = poppeye_end.get_rect(topleft = (0,0))
        
        scored = str(score)
        scoredisp = score_font.render(scored,True,'White')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type ==pygame.MOUSEBUTTONDOWN:
                    if back_rect.collidepoint(event.pos):
                        games_main()
                if event.type ==pygame.MOUSEBUTTONDOWN:
                    if playagain_rect.collidepoint(event.pos):
                        poppeye_game()
                if event.type ==pygame.MOUSEBUTTONDOWN:
                    if savescore_rect.collidepoint(event.pos):
                        cursor.execute("UPDATE SCORES SET POPPEYE = %s WHERE USERNAME = %s", (score, username))
                        mysql.commit()



            screen.blit(poppeye_end,poppeye_end_rect)
            screen.blit(playagain,playagain_rect)
            screen.blit(back,back_rect)
            screen.blit(gamescore,gamescore_rect)
            screen.blit(scoredisp,(505,230))
            if username != 'guest':
                screen.blit(savescore,savescore_rect)                


            pygame.display.update()
            clock.tick(60)
            
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('2D Game')

    background = pygame.image.load('graphics/background.jpg')

    char = pygame.image.load('graphics/popeye.png').convert_alpha()
    player = pygame.transform.scale(char, (170, 272))
    player_rect = player.get_rect(midbottom=(500, 650))

    char_l = pygame.image.load('graphics/popeye_left.png').convert_alpha()
    player_l = pygame.transform.scale(char_l, (300, 272))
    player_l_rect = player.get_rect(bottomright=(500, 650))

    char_r = pygame.image.load('graphics/popeye_right.png').convert_alpha()
    player_r = pygame.transform.scale(char_r, (300, 272))
    player_r_rect = player.get_rect(midbottom=(500, 650))

    oli = pygame.image.load('graphics/olive.png').convert_alpha()
    olive = pygame.transform.scale(oli, (140, 211))

    steak_image = pygame.image.load('graphics/steak.png').convert_alpha()
    steak = pygame.transform.scale(steak_image, (70, 70))
    sandwich_image = pygame.image.load('graphics/sandwich.png').convert_alpha()
    sandwich = pygame.transform.scale(sandwich_image, (70, 70))
    wine_image = pygame.image.load('graphics/wine.png').convert_alpha()
    wine = pygame.transform.scale(wine_image, (100, 100))
    hotdog_image = pygame.image.load('graphics/hotdog.png').convert_alpha()
    hotdog = pygame.transform.scale(hotdog_image, (70, 70))

    oli_throw = pygame.image.load('graphics/olive_throw.png').convert_alpha()
    olive_throw = pygame.transform.scale(oli_throw, (140, 211))

    goat = pygame.image.load('graphics/boat.png').convert_alpha()
    boat = pygame.transform.scale(goat, (400, 400))
    boat_rect = boat.get_rect(midbottom=(500, 700))

    plat = pygame.image.load('graphics/platform.png').convert_alpha()
    platform = pygame.transform.scale(plat, (165, 50))

    image = pygame.transform.scale(background, (1000, 700))

    clock = pygame.time.Clock()
    pos = 0

    olive_switch_timer = pygame.time.get_ticks()
    olive_display_throw = False
    switch_interval = 700

    items = []

    gravity = 0.175
    item_speed = 8

    score = 0
    lives = 3

    font = pygame.font.Font(None, 36)

    target_positions = [500,1000,2400]

    catch_rects = {-1: pygame.Rect(300, 550, 100, 100),0: pygame.Rect(450, 550, 100, 100),1: pygame.Rect(650, 550, 100, 100)}

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if pos > -1:
                        pos -= 1
                elif event.key == pygame.K_d:
                    if pos < 1:
                        pos += 1

        current_time = pygame.time.get_ticks()
        if current_time - olive_switch_timer > switch_interval:
            olive_display_throw = not olive_display_throw
            olive_switch_timer = current_time

            if olive_display_throw:
                item_type = ran.choice(['steak', 'sandwich', 'wine', 'hotdog'])
                if item_type == "steak":
                    item_image = steak
                elif item_type == "sandwich":
                    item_image = sandwich
                elif item_type == "hotdog":
                    item_image = hotdog
                else:
                    item_image = wine

                target_x = ran.choice(target_positions)
                target_y = 800

                direction_x = target_x - 80
                direction_y = target_y - 100

                distance = math.sqrt(direction_x**2 + direction_y**2)
                direction_x /= distance
                direction_y /= distance

                velocity_x = direction_x * item_speed
                velocity_y = direction_y * item_speed - 4

                items.append({"image": item_image, "pos": [80, 100], "velocity": [velocity_x, velocity_y], "target": target_x})

        screen.blit(image, (0, 0))

        if olive_display_throw:
            screen.blit(olive_throw, (60, 70))
        else:
            screen.blit(olive, (0, 70))

        if pos == 0:
            screen.blit(player, player_rect)
        elif pos == 1:
            screen.blit(player_r, player_r_rect)
        elif pos == -1:
            screen.blit(player_l, player_l_rect)

        screen.blit(boat, boat_rect)
        screen.blit(platform, (-20, 260))

        
        player_catch_rect = catch_rects[pos]

        for i in items[:]:
            i["pos"][0] += i["velocity"][0]
            i["pos"][1] += i["velocity"][1]
            i["velocity"][1] += gravity

            screen.blit(i["image"], i["pos"])

            if player_catch_rect.colliderect(pygame.Rect(i["pos"][0], i["pos"][1], i["image"].get_width(), i["image"].get_height())):
                score += 1
                items.remove(i)

            elif i["pos"][1] > 700:
                lives -= 1
                items.remove(i)

        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        lives_text = font.render(f'Lives: {lives}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))

        if lives <= 0:
            poppeye_end()


        pygame.display.update()
        clock.tick(60)


       
def mambaio_game():
    mambaio_background = pygame.image.load('graphics/mambaio_background.png').convert_alpha()
    mambaio_background_rect = mambaio_background.get_rect(topleft = (0,0))
    
    width, height = 1000, 700
    block_size, border_thickness = 20, 5
    colors = {
        'snake_body': (0, 0, 0),
        'snake_stripe': (255, 255, 255),
        'food': (255, 255, 0),
        'straw': (255, 0, 0),
        'bg': (128, 128, 128),
        'border': (0, 0, 0)
    }
    directions = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game")

    snake = [(100, 100), (80, 100), (60, 100)]
    direction, new_direction = directions['right'], directions['right']
    score = 0
    score_font =pygame.font.Font('fonts\\adrip1.TTF',43)
    food_pos = (
        ran.randint(0, (width // block_size) - 1) * block_size,
        ran.randint(0, (height // block_size) - 1) * block_size
    )

    def draw():
        screen.blit(mambaio_background,mambaio_background_rect)
        for i, (x, y) in enumerate(snake):
            color = colors['snake_body'] if i % 2 == 0 else colors['snake_stripe']
            pygame.draw.rect(screen, color, (x, y, block_size, block_size))
            pygame.draw.rect(screen, colors['border'], (x, y, block_size, block_size), 1)
        head_x, head_y = snake[0]
        eye_r, eye_offset_x, eye_offset_y = block_size // 6, block_size // 3, block_size // 4
        pygame.draw.circle(screen, (255, 255, 255), (head_x + eye_offset_x, head_y + eye_offset_y), eye_r)
        pygame.draw.circle(screen, (255, 255, 255), (head_x + 2 * eye_offset_x, head_y + eye_offset_y), eye_r)
        food_x, food_y = food_pos
        pygame.draw.rect(screen, colors['food'], (food_x, food_y, block_size, block_size))
        straw_x, straw_y = food_x + block_size // 2, food_y
        pygame.draw.line(screen, colors['straw'], (straw_x, straw_y), (straw_x, straw_y - 10), 3)
        score_display = score_font.render(f"Score: {score}", True, (255,255,255))
        screen.blit(score_display, (width - 150, 10))

    def flash():
        screen.fill((255, 255, 255))
        pygame.display.flip()
        pygame.time.delay(100)
        screen.fill(colors['bg'])

    def game_over():
        score_font = pygame.font.Font('fonts\\adrip1.ttf',73)
        back = pygame.image.load('graphics/backgames.png').convert_alpha()
        playagain = pygame.image.load('graphics/playagain.png').convert_alpha()
        savescore = pygame.image.load('graphics/savescore.png').convert_alpha()
        gamescore = pygame.image.load('graphics/score.png').convert_alpha()
        savescore = pygame.image.load('graphics/savescore.png').convert_alpha()
        playagain_rect = playagain.get_rect(topleft = (365,395))
        gamescore_rect = gamescore.get_rect(topleft = (285,230))
        savescore_rect = savescore.get_rect(topleft = (418,152))
        back_rect = back.get_rect(topleft = (428,499))
        mambaio_end = pygame.image.load('graphics/mambaio_end.png').convert_alpha()
        mambaio_end_rect = mambaio_end.get_rect(topleft = (0,0))
            
        scored = str(score)
        scoredisp = score_font.render(scored,True,'White')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type ==pygame.MOUSEBUTTONDOWN:
                    if back_rect.collidepoint(event.pos):
                        games_main()
                if event.type ==pygame.MOUSEBUTTONDOWN:
                    if playagain_rect.collidepoint(event.pos):
                        mambaio_game()
                if event.type ==pygame.MOUSEBUTTONDOWN:
                    if savescore_rect.collidepoint(event.pos):
                        cursor.execute("UPDATE SCORES SET MAMBAIO = %s WHERE USERNAME = %s", (score, username))
                        mysql.commit()



            screen.blit(mambaio_end,mambaio_end_rect)
            screen.blit(playagain,playagain_rect)
            screen.blit(back,back_rect)
            screen.blit(gamescore,gamescore_rect)
            screen.blit(scoredisp,(505,230))
            if username != 'guest':
                screen.blit(savescore,savescore_rect)



            pygame.display.update()
            clock.tick(60)

    speed = 1
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and direction != directions['down']:
                    new_direction = directions['up']
                elif event.key == pygame.K_s and direction != directions['up']:
                    new_direction = directions['down']
                elif event.key == pygame.K_a and direction != directions['right']:
                    new_direction = directions['left']
                elif event.key == pygame.K_d and direction != directions['left']:
                    new_direction = directions['right']


        if direction != new_direction:
            direction = new_direction
        head_x, head_y = snake[0]
        dir_x, dir_y = direction
        new_head = (head_x + dir_x * block_size, head_y + dir_y * block_size)
        snake.insert(0, new_head)
        if new_head == food_pos:
            flash()
            food_pos = (
                ran.randint(0, (width // block_size) - 1) * block_size,
                ran.randint(0, (height // block_size) - 1) * block_size
            )
            score += 1
            speed+=0.01
        else:
            snake.pop()
        if (new_head[0] < 0 or new_head[0] >= width or
            new_head[1] < 0 or new_head[1] >= height or
            new_head in snake[1:]):
            game_over()
        draw()
        pygame.display.flip()
        clock.tick(10**speed)



warning()


