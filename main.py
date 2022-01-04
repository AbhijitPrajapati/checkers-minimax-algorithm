import pygame
from game.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, BLACK, BLUE
from game.game import Game
from minimax.algorithm import minimax
from time import sleep
from game.piece import Piece

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers Minimax')

COLOR_DICT = {(255, 255, 255): 'AI Wins!', (255, 0, 0): 'Human Wins!'}

def get_row_col_from_mouse_pos(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    game = Game(screen)
    run = True
    while run:
        if game.winner() != None:
            print(COLOR_DICT[game.winner()])
            run = False
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse_pos(pos)
                game.select(row, col)
                
        game.update()
    pygame.quit()

if __name__ == '__main__':
    main()