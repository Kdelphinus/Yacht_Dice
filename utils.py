YACHT_DICE_TEXT = """
    
    
    
    
    YYYYYYY       YYYYYYY                                      hhhhhhh                      tttt               DDDDDDDDDDDDD          iiii
    Y:::::Y       Y:::::Y                                      h:::::h                   ttt:::t               D::::::::::::DDD      i::::i
    Y:::::Y       Y:::::Y                                      h:::::h                   t:::::t               D:::::::::::::::DD     iiii
    Y::::::Y     Y::::::Y                                      h:::::h                   t:::::t               DDD:::::DDDDD:::::D
    YYY:::::Y   Y:::::YYY  aaaaaaaaaaaaa       cccccccccccccccc h::::h hhhhh       ttttttt:::::ttttttt           D:::::D    D:::::D iiiiiii     cccccccccccccccc    eeeeeeeeeeee
       Y:::::Y Y:::::Y     a::::::::::::a    cc:::::::::::::::c h::::hh:::::hhh    t:::::::::::::::::t           D:::::D     D:::::Di:::::i   cc:::::::::::::::c  ee::::::::::::ee
        Y:::::Y:::::Y      aaaaaaaaa:::::a  c:::::::::::::::::c h::::::::::::::hh  t:::::::::::::::::t           D:::::D     D:::::D i::::i  c:::::::::::::::::c e::::::eeeee:::::ee
         Y:::::::::Y                a::::a c:::::::cccccc:::::c h:::::::hhh::::::h tttttt:::::::tttttt           D:::::D     D:::::D i::::i c:::::::cccccc:::::ce::::::e     e:::::e
          Y:::::::Y          aaaaaaa:::::a c::::::c     ccccccc h::::::h   h::::::h      t:::::t                 D:::::D     D:::::D i::::i c::::::c     ccccccce:::::::eeeee::::::e
           Y:::::Y         aa::::::::::::a c:::::c              h:::::h     h:::::h      t:::::t                 D:::::D     D:::::D i::::i c:::::c             e:::::::::::::::::e
           Y:::::Y        a::::aaaa::::::a c:::::c              h:::::h     h:::::h      t:::::t                 D:::::D     D:::::D i::::i c:::::c             e::::::eeeeeeeeeee
           Y:::::Y       a::::a    a:::::a c::::::c     ccccccc h:::::h     h:::::h      t:::::t    tttttt       D:::::D    D:::::D  i::::i c::::::c     ccccccce:::::::e
           Y:::::Y       a::::a    a:::::a c:::::::cccccc:::::c h:::::h     h:::::h      t::::::tttt:::::t     DDD:::::DDDDD:::::D  i::::::ic:::::::cccccc:::::ce::::::::e
        YYYY:::::YYYY    a:::::aaaa::::::a  c:::::::::::::::::c h:::::h     h:::::h      tt::::::::::::::t     D:::::::::::::::DD   i::::::i c:::::::::::::::::c e::::::::eeeeeeee
        Y:::::::::::Y     a::::::::::aa:::a  cc:::::::::::::::c h:::::h     h:::::h        tt:::::::::::tt     D::::::::::::DDD     i::::::i  cc:::::::::::::::c  ee:::::::::::::e
        YYYYYYYYYYYYY      aaaaaaaaaa  aaaa    cccccccccccccccc hhhhhhh     hhhhhhh          ttttttttttt       DDDDDDDDDDDDD        iiiiiiii    cccccccccccccccc    eeeeeeeeeeeeee
        
    
    
        
"""

CATEGORIES = [
    "Aces",
    "Deuces",
    "Threes",
    "Fours",
    "Fives",
    "Sixes",
    "Choice",
    "Four of a Kind",
    "Full House",
    "S. Straight",
    "L. Straight",
    "Yacht",
]

NUM_ICONS = [
    "1)",
    "2)",
    "3)",
    "4)",
    "5)",
    "6)",
    "7)",
    "8)",
    "9)",
    "10)",
    "11)",
    "12)",
]

DICES_DRAW = (
    "  +------+",
    " /      /|",
    "+-----+  |",
    ("|     |  |", "|  @  |  |", "|     | / "),
    ("|@    |  |", "|     |  |", "|    @| / "),
    ("|@    |  |", "|  @  |  |", "|    @| / "),
    ("|@   @|  |", "|     |  |", "|@   @| / "),
    ("|@   @|  |", "|  @  |  |", "|@   @| / "),
    ("|@   @|  |", "|@   @|  |", "|@   @| / "),
    "+-----+   ",
)

END_COLOR = "\033[0m"
RED_COLOR = "\033[91m"
GREEN_COLOR = "\033[92m"
BLUE_COLOR = "\033[94m"
YELLOW_COLOR = "\033[93m"
CYAN_COLOR = "\033[96m"
