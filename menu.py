import pygame, sys

pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Menu')


bg = pygame.image.load('background.png')

class Button():
    def __init__(self,image,pos,text_input,font,base_color,hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image == None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self,screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def CheckForInput(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,self.rect.bottom):
            return True
        return False

    def changeColor(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

def get_font(size):
    return pygame.font.Font(None, size)

def play():
    pygame.display.set_caption('Play')

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill('Black')
        play_text = get.font(45).render('This is the PLAY screen', True, 'White')
        play_rect = play_text,get_rect(center=(640,260))
        screen.blit(play_text, play_rect)

        play_back = Button(image = None, pos=(640,460), text_input='BACK', font=get_font(75), base_color='White', hovering_color='Green')

        play_back.changeColor(PLAY_MOUSE_POS)
        play_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.CheckForInput(PLAY_MOUSE_POS):
                    main.menu()

        pygame.display.update()

def options():
    pygame.display.set_caption('Options')

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill('Black')
        options_text = get.font(45).render('This is the OPTIONS screen', True, 'Black')
        options_rect = options_text,get_rect(center=(640,260))
        screen.blit(options_text, options_rect)

        options_back = Button(image = None, pos=(640,460), text_input='BACK', font=get_font(75), base_color='Black', hovering_color='Green')

        options_back.changeColor(OPTIONS_MOUSE_POS)
        options_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_back.CheckForInput(OPTIONS_MOUSE_POS):
                    main.menu()

        pygame.display.update()

def main_menu():
    pygame.display.set_caption('Menu')

    while True:
        screen.blit(bg,(0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        menu_text = get_font(100).render('MAIN MENU',True,(182, 143, 64))
        menu_rect = menu_text.get_rect(center=(640,100))

        play_button = Button(image=pygame.image.load('assets.jpg'), pos=(640,250),
                            text_input='PLAY', font=get_font(75), base_color=(215, 252, 212), hovering_color='White')
        options_button = Button(image=pygame.image.load('assets.jpg'), pos=(640,400),
                            text_input='OPTIONS', font=get_font(75), base_color=(215, 252, 212), hovering_color='White')
        quit_button = Button(image=pygame.image.load('assets.jpg'), pos=(640,550),
                            text_input='QUIT', font=get_font(75), base_color=(215, 252, 212), hovering_color='White') 

        screen.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.CheckForInput(MENU_MOUSE_POS):
                    play()
                if options_button.CheckForInput(MENU_MOUSE_POS):
                    options()
                if quit_button.CheckForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
main_menu()