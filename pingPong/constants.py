from game.casting.color import Color
from game.casting.point import Point

# --------------------------------------------------------------------------------------------------
# GENERAL GAME CONSTANTS
# --------------------------------------------------------------------------------------------------

# GAME
GAME_NAME = "Ping Pong"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "pingPong/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
ASSETS_SOUND = "pingPong/assets/sounds"
BOUNCE_SOUND = "pingPong/assets/sounds/game_boing.wav"
OVER_SOUND = "pingPong/assets/sounds/game_points.wav"
WELCOME_SOUND = "pingPong/assets/sounds/game_start.wav"
INIT_SOUND = "pingPong/assets/sounds/game_init.wav"


# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "up"
RIGHT = "down"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4


# --------------------------------------------------------------------------------------------------
# SCRIPTING CONSTANTS
# --------------------------------------------------------------------------------------------------

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# --------------------------------------------------------------------------------------------------
# CASTING CONSTANTS
# --------------------------------------------------------------------------------------------------

# STATS
STATS_GROUP = "stats"


# HUD
HUD_MARGIN = 15
SCORE_GROUP = "score"
SCORE_FORMAT = "SCORE: {}"
SCORE_A_POSITION = Point(80, HUD_MARGIN)
SCORE_B_POSITION = Point(SCREEN_WIDTH - 100, HUD_MARGIN)

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "pingPong/assets/images/000.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 6

# RACKET
RACKET_GROUP = "rackets"
RACKET_IMAGES = [f"pingPong/assets/images/{n:03}.png" for n in range(110, 113)]
RACKET_WIDTH = 25
RACKET_HEIGHT = 200
RACKET_RATE = 6
RACKET_VELOCITY = 7


# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"
WINNER_GAME = "Winner Chicken Dinner {}"

PLAYER_A_IDX = 0
PLAYER_B_IDX = 1

PLAYER_A_NAME = "PLAYER A"
PLAYER_B_NAME = "PLAYER B"

PLAYER_A_KEY_UP = 'w'
PLAYER_A_KEY_DOWN = 's'

PLAYER_B_KEY_UP = 'i'
PLAYER_B_KEY_DOWN = 'k'

PLAYER_DEFAULT_POINTS = 1
GAME_MAX_SCORE = 10
