import pygame, random, sys
from pygame.locals import  *
from card import Card
from deck import Deck

pygame.init()
size = (width,height) = (800,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

deck = None
board = pygame.sprite.Group()
selected_card = pygame.sprite.GroupSingle()

discard_pile = pygame.sprite.Group()
top_card = pygame.sprite.GroupSingle()
next_card = pygame.sprite.GroupSingle()
empty_deck = pygame.Rect(0,0,71,94)
empty_deck.bottomleft = (20,height-20)

BG_COLOR = (0,102,0)

def check_remove(card_clicked):
    if len(selected_card) > 0 and selected_card.sprite.rank + card_clicked.rank == 13:
        selected_card.sprite.kill()
        card_clicked.kill()
    elif card_clicked.rank == 13:
        selected_card.empty()
        card_clicked.kill()
    else:
        selected_card.add(card_clicked)

def check_sprite_clicked(x,y):
    card_clicked = None
    for card in board:
        if card.rect.collidepoint(x,y):
            card_clicked = card
    if card_clicked is not None:
        hit_list = pygame.sprite.spritecollide(card_clicked,board,False)
        for card in hit_list:
            if card.rect.y > card_clicked.rect.y:
                return
        check_remove(card_clicked)

def init():
    deck = Deck()

    for i in range(7):
        for j in range(i+1):
            card = deck.deal()
            card.flip()
            card.rect.midtop = (width//2-40*i+80*j,30*i+100)
            board.add(card)
    next_card.add(deck.deal())
    next_card.sprite.rect.bottomleft =(20,height-20)

def main():
    global screen

    init()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    x,y = event.pos
                    check_sprite_clicked(x,y)
            if event.type == KEYDOWN:
                if event.key == K_f:
                    screen = pygame.display.set_mode(screen,FULLSCREEN)
                if event.key == K_d:
                    screen = pygame.display.set_mode(screen)

        screen.fill(BG_COLOR)
        board.draw(screen)
        top_card.draw(screen)
        next_card.draw(screen)
        discard_pile.draw(screen)
        if len(selected_card) == 1:
            pygame.draw.rect(screen,(204,173,0),selected_card.sprite.rect,3)
        if len(next_card) == 0:
            pygame.draw.rect(screen,(0,0,0),empty_deck,3)
        pygame.display.flip()


if __name__ == '__main__':
    main()

