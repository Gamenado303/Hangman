import pygame
import math 
import random

pygame.init()

def init_all_words():
    word_list = []
    f = open("words.txt", "r")
    for line in f:
        word_list.append(line.strip())

    return word_list

def draw_keyboard():
    spacing = 12
    font = pygame.font.Font('freesansbold.ttf', 32)
    rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    keyboard_position.clear()
    for i in range(3):
        startx = WIDTH/2 - len(rows[i])*(TILE_SIZE + spacing)/2
        starty = HEIGHT - (3.5-i)*(TILE_SIZE+spacing)
        for j in range(len(rows[i])):
            key_colour = UNKNOWN_KEY_COLOUR
            if rows[i][j] in guessed_letters:
                if rows[i][j] in actual_word: key_colour = CORRECT_KEY_COLOUR
                else: key_colour = WRONG_KEY_COLOUR

            pygame.draw.rect(screen, key_colour, pygame.Rect(startx, starty, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(startx, starty, TILE_SIZE, TILE_SIZE), 2)
            text = font.render(rows[i][j], True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (startx + TILE_SIZE/2, starty+TILE_SIZE/2)
            screen.blit(text, textRect)

            keyboard_position[rows[i][j]] = (startx, starty)

            startx += TILE_SIZE + spacing

def draw_word():
    font = pygame.font.Font('freesansbold.ttf', 44)
    spacing = 14
    startx = WIDTH/2 - len(actual_word)*(TILE_SIZE + spacing)/2
    starty = HEIGHT - 5*TILE_SIZE

    for i in actual_word:
        pygame.draw.line(screen, (0, 0, 0), (startx, starty), (startx + TILE_SIZE, starty), 2)
        if i in guessed_letters:
            text = font.render(i, True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (startx + TILE_SIZE/2, starty-17)
            screen.blit(text, textRect)
        
        startx += TILE_SIZE + spacing

def draw_hangman():
    wrong = 0
    for l in guessed_letters: 
        if l not in actual_word: wrong += 1

    if wrong <= 0: return

    # base
    startx = WIDTH/2 - 2 *TILE_SIZE
    starty = HEIGHT - 7*TILE_SIZE
    pygame.draw.line(screen, (0, 0, 0), (startx, starty), (startx + 4*TILE_SIZE, starty), 4)

    wrong -= 1
    if wrong <= 0: return

    # vert base
    startx = WIDTH/2 - 1.6*TILE_SIZE
    starty = HEIGHT - 7*TILE_SIZE
    pygame.draw.line(screen, (0, 0, 0), (startx, starty), (startx, starty - 4*TILE_SIZE), 4)

    wrong -= 1
    if wrong <= 0: return

    # top base
    startx = WIDTH/2 - 1.6*TILE_SIZE
    starty = HEIGHT - 11*TILE_SIZE
    pygame.draw.line(screen, (0, 0, 0), (startx, starty), (startx + 1.6*TILE_SIZE, starty), 4)

    wrong -= 1
    if wrong <= 0: return

    # rope
    startx = WIDTH/2
    starty = HEIGHT - 11*TILE_SIZE
    pygame.draw.line(screen, (0, 0, 0), (startx, starty), (startx, starty+0.6*TILE_SIZE), 4)

    wrong -= 1
    if wrong <= 0: return

    # face
    startx = WIDTH/2
    starty = HEIGHT - 10*TILE_SIZE
    pygame.draw.circle(screen, (0, 0, 0), (startx, starty), 0.4*TILE_SIZE, 4)

    wrong -= 1
    if wrong <= 0: return

    # body
    startx = WIDTH/2
    starty = HEIGHT - 9.6*TILE_SIZE
    pygame.draw.line(screen, (0, 0, 0), (startx, starty), (startx, starty+1.4*TILE_SIZE), 4)

    wrong -= 1
    if wrong <= 0: return

    # left arm
    startx = WIDTH/2
    starty = HEIGHT - 9.4*TILE_SIZE
    pygame.draw.line(screen, (0, 0, 0), (startx, starty), (startx-0.5*TILE_SIZE, starty+0.4*TILE_SIZE), 6)

    wrong -= 1
    if wrong <= 0: return

    # right arm
    startx = WIDTH/2
    starty = HEIGHT - 9.4*TILE_SIZE
    pygame.draw.line(screen, (0, 0, 0), (startx, starty), (startx+0.5*TILE_SIZE, starty+0.4*TILE_SIZE), 6)

    wrong -= 1
    if wrong <= 0: return

    # left leg
    startx = WIDTH/2
    starty = HEIGHT - 8.2*TILE_SIZE
    pygame.draw.line(screen, (0, 0, 0), (startx, starty), (startx-0.5*TILE_SIZE, starty+0.4*TILE_SIZE), 6)

    wrong -= 1
    if wrong <= 0: return

    # right leg
    startx = WIDTH/2
    starty = HEIGHT - 8.2*TILE_SIZE
    pygame.draw.line(screen, (0, 0, 0), (startx, starty), (startx+0.5*TILE_SIZE, starty+0.4*TILE_SIZE), 6)

def check_lost():
    wrong = 0
    for l in guessed_letters: 
        if l not in actual_word: wrong += 1

    if wrong >= 10:
        return True
    return False

def check_won():
    for l in actual_word:
        if l not in guessed_letters:
            return False
    return True

def draw_msg(msg):
    font = pygame.font.Font('freesansbold.ttf', 80)
    text = font.render(msg, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (WIDTH/2, HEIGHT - 3.2*TILE_SIZE)
    screen.blit(text, textRect)

    r = pygame.Rect(0, 0, 3.6*TILE_SIZE, TILE_SIZE)
    r.center = (WIDTH/2, HEIGHT - 1.6*TILE_SIZE)
    pygame.draw.rect(screen, (0, 0, 0), r, 2)

    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render("Play Again", True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (WIDTH/2, HEIGHT - 1.6*TILE_SIZE)
    screen.blit(text, textRect)

def start_game():
    guessed_letters.clear()
    actual_word = random.choice(ALL_WORDS)
    return actual_word

WIDTH = 850
HEIGHT = 700
TILE_SIZE = 60
ALL_WORDS = init_all_words()
UNKNOWN_KEY_COLOUR = (245, 217, 182)
CORRECT_KEY_COLOUR = (142, 242, 114)
WRONG_KEY_COLOUR = (242, 137, 114)
running = True
guessed_letters = set()
keyboard_position = {}
actual_word = start_game()
lost = False
won = False

BACKGROUND_COLOUR = (224, 198, 153)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

while running:
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    lost = check_lost()
    won = check_won()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if (event.button == 1):
                x, y = pygame.mouse.get_pos()
                if won or lost:
                    startx = WIDTH/2 - 1.8*TILE_SIZE
                    starty = HEIGHT - 2.1*TILE_SIZE
                    if startx <= x <= startx + 3.6*TILE_SIZE and starty <= y <= starty + TILE_SIZE:
                        actual_word = start_game()
                        won = False
                        lost = False
                else:
                    for l in keyboard_position.keys():
                        startx, starty = keyboard_position[l]
                        if startx <= x <= startx + TILE_SIZE and starty <= y <= starty + TILE_SIZE:
                            guessed_letters.add(l)
                                   
    screen.fill(BACKGROUND_COLOUR) 
    draw_word()
    draw_hangman()
    if not lost and not won:
        draw_keyboard()  
    elif lost:
        draw_msg("YOU LOST!!!!")
    elif won:
        draw_msg("YOU WON.")
        
    pygame.display.flip()

pygame.quit()