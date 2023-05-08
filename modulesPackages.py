#EXEMPLE
# game.py
# import the draw module
#import draw
def play_game():
    ...

def main():
    result = play_game()
    #draw.draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()

# draw.py
#def draw_game():
#    ...

#def clear_screen(screen):
#    ...

# game.py
# import the draw module
#from draw import draw_game

def main():
    result = play_game()
#    draw_game(result)

# game.py
# import the draw module
#from draw import *

def main():
    result = play_game()
#    draw_game(result)

# game.py
# import the draw module
#if visual_mode:
    # in visual mode, we draw using graphics
#    import draw_visual as draw
#else:
    # in textual mode, we print out text
#    import draw_textual as draw

def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
#    draw.draw_game(result)

# draw.py
def draw_game():
    # when clearing the screen we can use the main screen object initialized in this module
    clear_screen(main_screen)
    ...

def clear_screen(screen):
    ...

class Screen():
    ...

# initialize main_screen as a singleton
main_screen = Screen()

#PYTHONPATH=/foo python game.py

#sys.path.append("/foo")

# import the library
#import urllib

# use it
#urllib.urlopen(...)

#>>> import urllib
#>>> dir(urllib)

#help(urllib.urlopen)

#import foo.bar

#from foo import bar

#__init__.py:

#__all__ = ["bar"]

#EXERCICE
import re

# Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))