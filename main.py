import pygame
import random


pygame.init()


window_width = 600
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Hangman")


white = (255, 255, 255)
black = (0, 0, 0)

secret_words = ["apple", "banana", "cherry", "papaya", "absurd", "avenue", "gossip",
                "galaxy", "bookworm", "pixel", "buffalo", "jackpot", "injury", "crypt",
                "jelly", "jogging", "equip", "scratch", "joking", "wizard", "zodiac"]
guessed_letters = []
secret_word = ""
correct_letters = []
letter_dict = {}
mistakes = 0
won = None
length = 0


font = pygame.font.Font(None, 72)
font2 = pygame.font.Font(None, 30)
font3 = pygame.font.Font(None, 60)

start = False

def handle_events():
    global start
    global guessed_letters
    global correct_letters
    global mistakes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            if start and won is None:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letter = chr(event.key)
                    if letter not in guessed_letters:
                        guessed_letters.append(letter)
                        if letter not in secret_word:
                            mistakes += 1
                        else:
                            correct_letters.append(letter)
    return True


def update():
    global start
    global secret_words
    global secret_word
    global letter_dict
    global correct_letters
    global won
    global mistakes
    global guessed_letters
    global length

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if secret_word == "":
            guessed_letters = []
            correct_letters = []
            letter_dict = {}
            mistakes = 0
            length = 0
            won = None
            start = True
            secret_word = random.choice(secret_words)
            length = len(secret_word)
            for i in range(len(secret_word)):
                if not secret_word[i] in letter_dict:
                    letter_dict[secret_word[i]] = [i]
                else: 
                    letter_dict[secret_word[i]].append(i)
    if secret_word != "" and len(correct_letters) == len(letter_dict):
        won = True
        secret_word = ""
    if mistakes >= 7:
        won = False
        secret_word = ""



def render():
    global start
    global secret_word
    global mistakes
    global correct_letters
    global letter_dict
    global won
    global length

    window.fill(white)



    text_surface = font.render("HANGMAN", True, black)
    text_rect = text_surface.get_rect(center=(window_width/2, window_height/15))
    window.blit(text_surface, text_rect)

    if not start:

        text_surface2 = font3.render("Press SPACE to begin!", True, black)
        text_rect2 = text_surface2.get_rect(center=(window_width/2, window_height/2))
        window.blit(text_surface2, text_rect2)

    if start:
        pygame.draw.rect(window, black, ((window_width/2)-100,150,200,10)) #Ceiling
        pygame.draw.rect(window, black, ((window_width/2)-5,150,10,75))   # Rope

        for i in range(length):
            pygame.draw.rect(window, black, (50+((500-(length*50))/2)+(i*50),window_height - 75,40,10))

        if won is None: 

            for i in correct_letters:
                indices = letter_dict[i]
                for j in indices:
                    text_surface3 = font3.render(i.upper(), True, black)
                    text_rect3 = text_surface3.get_rect(center=(70+((500-(length*50))/2)+(j*50), window_height - 95))
                    window.blit(text_surface3, text_rect3)

        if won is not None:
            for i in letter_dict:
                indices = letter_dict[i]
                for j in indices:
                    text_surface3 = font3.render(i.upper(), True, black)
                    text_rect3 = text_surface3.get_rect(center=(70+((500-(length*50))/2)+(j*50), window_height - 95))
                    window.blit(text_surface3, text_rect3)

        if mistakes >= 1:
            pygame.draw.circle(window, black, (window_width/2, 275), 50)   # Head


        if mistakes >= 2:
            pygame.draw.rect(window, black, ((window_width/2)-5,325,10,30))


        if mistakes >= 3:
            pygame.draw.polygon(window, black, [
                ((window_width/2)-5+9,340),
                ((window_width/2)-5+9,355),
                ((window_width/2)-93+9,434),
                ((window_width/2)-100+9,425)
                ])

        if mistakes >= 4:
            pygame.draw.polygon(window, black, [
                ((window_width/2)-5,340),
                ((window_width/2)-5,355),
                ((window_width/2)+93-10,434),
                ((window_width/2)+100-10,425)
                ])

        if mistakes >= 5:
            pygame.draw.rect(window, black, ((window_width/2)-5,355,10,150))

        if mistakes >= 6:
            pygame.draw.polygon(window, black, [
                ((window_width/2)-5+9,490),
                ((window_width/2)-5+9,505),
                ((window_width/2)-93+9,584),
                ((window_width/2)-100+9,575)
                ])

        if mistakes >= 7:
            pygame.draw.polygon(window, black, [
                ((window_width/2)-5,490),
                ((window_width/2)-5,505),
                ((window_width/2)+93-10,584),
                ((window_width/2)+100-10,575)
                ])

        if won: 
            text_surface4 = font3.render("You Won!", True, black)
            text_rect4 = text_surface4.get_rect(center=(window_width/2, 620))
            window.blit(text_surface4, text_rect4)

        if won == False: 
            text_surface4 = font3.render("You Lost!", True, black)
            text_rect4 = text_surface4.get_rect(center=(window_width/2, 620))
            window.blit(text_surface4, text_rect4)

        if won != None:
            text_surface4 = font2.render("Press SPACE to start over!", True, black)
            text_rect4 = text_surface4.get_rect(center=(window_width/2, 655))
            window.blit(text_surface4, text_rect4)

    pygame.display.flip()


def game_loop():
    # Game loop
    running = True
    while running:
        running = handle_events()
        update()
        render()

    # Quit the game
    pygame.quit()


# Start the game
game_loop()
