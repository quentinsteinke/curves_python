import pygame
from circle import Circle
from functions import lerp


pygame.init()


###################### Variables ######################
white = (200, 200, 200)
gray = (23, 37, 70)
black = (0, 0, 0)
red = (210, 50, 50)
green = (80, 160, 80)
blue = (80, 80, 160)

screen_width = 1280
screen_height = 720

p1_pos = (screen_width - 20, screen_height/2)
p4_pos = (20, screen_height/2)

fps = 60

mouse_down  = False

screen = pygame.display.set_mode((screen_width, screen_height))

t = 0.5


###################### Creating shapes ######################
px = Circle("px", screen, white, 20, 20, 10)

p1 = Circle("p1", screen, red, screen_width - 20, screen_height/2, 25)

p3 = Circle("p3", screen, green, 0, 0, 10)

p4 = Circle("p4", screen, red, 20, screen_height/2, 25)

###################### Program loop ######################
running = True
while running:

    pygame.time.Clock().tick(fps)

    # Event triggers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
                
        if event.type == pygame.K_ESCAPE:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if mouse_down == False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Pickup")
                mouse_down = True
        
        if event.type == pygame.MOUSEBUTTONUP:
            print("letting go")
            mouse_down = False
    
    
    mouse_pos = pygame.mouse.get_pos()

    screen.fill(gray)


    # Drawing and Moving points
    px.x_pos(px.x + 2)
    px.draw()

    p1.draw()

    if mouse_down == True:
        pass
        # p4.transform(mouse_pos)
    
    p4.draw()

    p3.transform(lerp(p1.position, p4.position, t))
    p3.draw()

    if mouse_down == True:
        for inst in Circle.instances:
            if mouse_pos[0] < inst.x + inst.size and mouse_pos[0] > inst.x - inst.size:
                if mouse_pos[1] < inst.y + inst.size and mouse_pos[1] > inst.y - inst.size:
                    inst.on_clicked(mouse_pos)


    # Updating the screen
    pygame.display.update()


pygame.quit()