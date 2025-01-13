#ruben
#11/20
#pokemon

#init
import random
#functions
pokemon_level = 0
pokemon_name = "gastly"
win = random.randint(0,10)
day = 1
wins = 0
losses = 0
pokemon_mood = 10
def draw_gastly():
    print("""                   ⣤⠶⠒⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⠶⠞⠉⠀⠀⠀⠉⠙⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣄⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠈⠉⠛⣦⠀⣠⣤⣄⣀⣠⠤⠞⠋⠛⠛⠛⠉⠙⠛⢶⣄⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⢀⣤⣄⡀⢀⣶⢤⣀⣉⣯⣍⡁⠀⠙⡆⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⢿⡀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡆⠀⠀⠀⠀
    ⠀⠀⠀⠀⣠⠞⠋⠉⠉⠛⣾⣇⡀⠙⠋⠁⠀⠈⠁⠀⠈⠙⠒⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀
    ⠀⠀⠀⢰⠏⠀⠀⠀⠀⢀⣾⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⠴⠚⠛⠛⠛⠛⠛⠓⠲⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀
    ⠀⠀⠀⢸⣄⠀⢠⡴⠶⣫⡷⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⣰⠀⠀⠀⠀⠀⠀⠀⢀⣾⠀⠀⠀
    ⠀⠀⠀⠀⠻⠷⠋⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣠⡟⣧⠀⠀⠀⠀⢾⡗⠛⠋⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠘⢧⣀⣀⣀⣀⡀⠀⠀⠀⣠⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠀⠙⣆⠀⠀⠀⠈⢷⡄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⡀⠀⠈⣿⠀⠀⢰⡏⠈⠙⠶⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠃⠀⠀⢹⡄⠀⠀⠀⠀⣷⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠙⠓⠒⠋⠀⢠⣿⡇⠀⠀⠀⠀⠙⠲⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠸⣇⠀⠀⢀⡼⠏⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⣾⢸⡇⠀⠀⠀⠀⠀⠀⠈⠙⠷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠏⡀⠀⠀⠀⠀⢹⠀⠀⣿⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠙⠶⣄⡀⠀⠀⠀⠀⠀⠀⣰⠏⢸⡇⠀⠀⠀⠀⢸⡇⠀⠈⠻⣇⠀⠀⠀⠀
    ⣠⡶⠶⠖⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⠙⢶⣄⠀⠀⠀⢼⣟⠀⠈⠉⠀⠀⠀⢀⣾⠀⠀⠀⠀⠙⠳⢶⣄⠀
    ⢿⡇⠀⠀⠀⣠⠞⠛⠻⣦⠀⠀⠀⠀⠘⣷⠀⠈⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⣸⠏⠁⠀⠀⠀⢻⣄⠀⠀⠀⠀⣤⣾⡇⠀⠀⠀⠀⠀⠀⣠⡿⠀
    ⠈⠛⠒⠶⢿⣥⣄⣀⡀⣿⠀⠀⠀⠀⠀⢹⡄⠀⠀⠙⠷⣄⡀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠙⠳⠶⢾⣟⡇⣸⠃⢠⡾⣆⠀⠀⢀⣿⠁⠀
    ⠀⠀⠀⣼⠉⠀⠀⠉⣧⠙⣦⡀⠀⠀⠀⠈⢧⡀⠀⠀⠀⠈⠉⠓⠲⠶⠶⠶⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⣀⣠⡴⣾⣟⡇⣰⠏⠀⣼⣀⠿⣄⠀⣰⡟⠀⠀
    ⠀⠀⠀⢻⣄⠀⢀⣼⠃⠀⢸⠇⠀⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⢾⣄⡀⠀⠀⠀⠀⠀⣀⣠⣤⡤⠶⠚⠋⠁⣤⠴⠋⢹⣿⠟⠀⠀⠈⠙⣻⡎⠙⠃⠀⠀⠀
    ⠀⠀⠀⠀⠈⢛⣉⡀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠈⠛⢿⡉⣿⣋⡉⠉⠁⣀⣀⣀⡤⠶⠚⠋⠀⠀⢀⡾⠋⠀⠀⢠⣶⡿⠛⠁⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣿⠉⠙⠓⠶⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⠀⠀⠈⠿⠋⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⣠⡴⠋⠀⣴⣦⣀⡾⠉⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠴⠛⠁⠀⠀⠀⠻⣦⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠙⢦⣀⣀⣀⣀⡤⠴⠶⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠻⣆⣀⣠⡴⠶⠦⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⢶⣦⠀⠀⠈⢷⣄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣵⠛⠛⠳⡆⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⡾⠁⠀⠀⠀⠀⣽⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢠⡟⡴⠛⠋⠀⠀⠀⢀⣤⠞⠛⠛⠛⠛⠦⣤⡀⢠⡟⣧⠀⢀⣤⠼⠞⠋⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢦⣀⣠⠾⠀⣧⣀⡤⠖⠒⠊⠉⠁⠀⠀⠀⠀⠀⠀⠀⠙⠋⠀⠙⠋⠉""")
def draw_haunter():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⢠⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣤⣄⣀⣀⠀⢀⣀⣀⣠⣤⣤⣴⣶⣶⣶⣶⣿⣿⣿⣿⣿⡿⠋
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣶⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣦⣼⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣋⣁⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀
    ⠀⠀⠀⠀⣠⣾⣿⣿⣿⣷⣶⣶⣦⣤⣤⡀⠀⠀⢿⣷⣄⣹⣿⣿⣿⣿⣿⡿⠟⡿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀
    ⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣤⣤⣅⣀⣀⣀⡀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀
    ⠀⡀⣿⣿⣿⣿⠟⣿⣿⣿⣿⣿⣿⣿⠿⠃⠀⠀⠀⠀⢻⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣾⣧⢿⣿⠏⠀⢸⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠈⠿⠁⠀⠀⠀⠀⠈⠿⠁⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀
    ⠈⠻⡎⠟⠀⠀⠈⢿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠁⠀⠀⠀⠀⠀⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢦⣄⡀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣶⣶⣶⣶⣿⣿⡿⢟⣫⣭⣟⠿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢙⣵⣮⣭⣷⣾⣿⣿⣿⣿⣷⡜⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢹⣿⣿⣿⣿⡎⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢻⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠟⠉⠀⣴⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⡇⠈⠙⠻⢿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃⠀⠀⢰⣿⣿⣿⠟⠁⠀⠀⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠉⠙⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠏⠀⠀⠀⢠⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡏⠀⠀⠀⠀⢸⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠘⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
def draw_gengar():
    print("""⠀⠀⠀⣿⠿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠈⠻⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⣿⣷⣄⢀⣤⡀⠀⠀⢀⣀⣤⣶⡶⠿⢛⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣬⠻⣿⡟⣿⣶⠾⠛⠋⠉⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢀⣸⡿⣶⣄⣀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣧⣤⣴⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢿⣟⠛⠋⠀⠉⠛⠿⣦⣄⠀⠀⣿⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣯⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄
    ⢀⣽⡷⠀⠀⠀⠀⠀⠈⠙⠻⣶⣿⣤⣶⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⢀⣨⡿⠋
    ⠘⠻⢷⣦⡀⠀⠀⠀⠀⠀⠀⢠⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀
    ⠀⠀⠀⠹⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠉⠀⠀⠀⠀
    ⠀⠀⠀⠀⠹⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠁⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠹⣷⣠⡿⠀⠀⠀⠀⠀⠀⢠⣿⠃⠘⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣸⡟⠀⠀⠀⠀⡀⠀⠀⣾⡇⠀⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠾⠀⠀⠀⠀⠀⣿⣄⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⣿⠁⠀⠀⠀⠀⣿⡄⠀⢹⣧⠀⠀⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠟⠋⣿⠀⠀⠀⠀⠀⠀⢸⣿⣁⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⣿⢿⣄⠀⠙⢷⣤⣄⣈⣿⡀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠟⠋⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⢸⡏⠉⠉⠙⠛⠛⠛⠛⠛⠷⣶⣶⡄⠀⠀
    ⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⣿⠈⠻⣦⣄⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⣠⣾⠟⠙⠏⠀⠀⠀⣠⡿⠁⠀⠀⠀⠀⠀⠀⠸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢻⣶⡄⠀
    ⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣿⡄⢠⡿⠛⢷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠉⠙⠿⢶⣦⣴⣶⠾⠋⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣸⡟⠋⠁⠀
    ⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠘⣿⣼⠇⠀⠀⠈⣽⠟⠷⢶⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⣀⣀⣤⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠾⠛⠛⠻⠃⠀⠀⠀
    ⠀⠀⠀⠀⠀⣸⣇⠀⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⢰⡿⠀⠀⠀⠀⠉⠙⣿⠟⠛⠛⠛⢻⡿⠛⢫⣿⠃⠀⠀⠀⠀⠀⢠⣿⣀⣠⣴⡶⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣼⡿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠈⠻⢷⣾⣇⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⣼⣇⣴⠟⠁⠀⠀⠀⠀⠀⠀⣼⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢰⡿⠀⠹⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢶⣦⣤⣄⣼⣇⣀⣠⣤⣴⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢸⡇⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⣦⣄⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠻⣷⡀⠀⠀⠀⠘⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠙⠻⣷⣤⡀⢀⣈⣻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⣮⣿⣿⣿⠙⠿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠁⠀⠀⠀⠀⠉⠛⣿⣷⣶⣶⣶⣶⡶⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⣼⡟⠀⠀⠻⣧⠀⢀⠊⠢⠔⢱⡀⡀⣠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⢀⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⣤⣤⣴⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
print("Welcome to Pokemon")
def days():
    global day
    day = day + 1
    print("Select an activity for day " + str(day))
def record():
    global wins
    global losses
    print("Wins " +str(wins))
    print("Losses " + str(losses))
def pokemon_evolve1():
    global pokemon_level
    global pokemon_name
    if pokemon_level >= 5 and pokemon_level < 15:
        draw_haunter()
        pokemon_name = "insert name of pokemon here"
def pokemon_evolve2():
    global pokemon_level
    global pokemon_name
    if pokemon_level >= 15:
        draw_gengar()
        pokemon_name = "insert name of pokemon here"
def train():
    global pokemon_level
    pokemon_level = pokemon_level + 1
    print("your pokemon level: " + str(pokemon_level))

def gym_battle():
    global pokemon_level
    global win
    global losses
    global pokemon_mood
    global win
    guess = int(input("Enter Guess"))
    if pokemon_level >= 5:
        win = random.randint(0,9)
            if pokemon_name == win:
            pokemon_level = pokemon_level + 2
            print("your pokemon level: " + str(pokemon_level))
            wins = wins + 1
            pokemon_mood = pokemon_mood + 1
            print("your pokemon mood: " + str(pokemon_mood))
            else:
            pokemon_level = pokemon_level + 1
            print("your pokemon level: " + str(pokemon_level))
            losses = losses + 1
            pokemon_mood = pokemon_mood - 1
            print("your pokemon mood: " + str(pokemon_mood))
    elif pokemon_level >= 15:
        win = random.randint(0,8)
           if pokemon_name == win:
            pokemon_level = pokemon_level + 2
            print("your pokemon level: " + str(pokemon_level))
            wins = wins + 1
            pokemon_mood = pokemon_mood + 1
            print("your pokemon mood: " + str(pokemon_mood))
            else:
            pokemon_level = pokemon_level + 1
            print("your pokemon level: " + str(pokemon_level))
            losses = losses + 1
            pokemon_mood = pokemon_mood - 1
            print("your pokemon mood: " + str(pokemon_mood))
        win = random.randint(0,7)
            if pokemon_name == win:
            pokemon_level = pokemon_level + 2
            print("your pokemon level: " + str(pokemon_level))
            wins = wins + 1
            pokemon_mood = pokemon_mood + 1
            print("your pokemon mood: " + str(pokemon_mood))
            else:
            pokemon_level = pokemon_level + 1
            print("your pokemon level: " + str(pokemon_level))
            losses = losses + 1
            pokemon_mood = pokemon_mood - 1
            print("your pokemon mood: " + str(pokemon_mood))
    elif pokemon_level >= 35:
        win = random.randint(0,6)
            if pokemon_name == win:
            pokemon_level = pokemon_level + 2
            print("your pokemon level: " + str(pokemon_level))
            wins = wins + 1
            pokemon_mood = pokemon_mood + 1
            print("your pokemon mood: " + str(pokemon_mood))
            else:
            pokemon_level = pokemon_level + 1
            print("your pokemon level: " + str(pokemon_level))
            losses = losses + 1
            pokemon_mood = pokemon_mood - 1
            print("your pokemon mood: " + str(pokemon_mood))

    elif pokemon_level >= 45:
        win = random.randint(0,5)
            if pokemon_name == win:
            pokemon_level = pokemon_level + 2
            print("your pokemon level: " + str(pokemon_level))
            wins = wins + 1
            pokemon_mood = pokemon_mood + 1
            print("your pokemon mood: " + str(pokemon_mood))
            else:
            pokemon_level = pokemon_level + 1
            print("your pokemon level: " + str(pokemon_level))
            losses = losses + 1
            pokemon_mood = pokemon_mood - 1
            print("your pokemon mood: " + str(pokemon_mood))
    elif pokemon_level >= 50:
        win = random.randint(0,4)
            if pokemon_name == win:
            pokemon_level = pokemon_level + 2
            print("your pokemon level: " + str(pokemon_level))
            wins = wins + 1
            pokemon_mood = pokemon_mood + 1
            print("your pokemon mood: " + str(pokemon_mood))
            else:
            pokemon_level = pokemon_level + 1
            print("your pokemon level: " + str(pokemon_level))
            losses = losses + 1
            pokemon_mood = pokemon_mood - 1
            print("your pokemon mood: " + str(pokemon_mood))


def rest():
    global pokemon_mood
    print("If Pokemon mood 7 or more its happy")
    print("If Pokemon mood 4 to 6 its netural")
    print("If Pokemon mood 3 or less its sad")
    print("your pokemon name: " + str(pokemon_name))
    print("your pokemon level: " + str(pokemon_level))
    pokemon_mood = pokemon_mood + 1
        print("your pokemon mood: " + str(pokemon_mood))




#main ⠀⠀⠀⠀⠀⠀⠀⠀ ⠀
print("Welcome trainer to Pokemone Evolution")
print("select an activity for day 1: ")
print("""1.Train
2.Gym Battle
3.Rest (Display Pokemon)
4.Quit """)
while 4:
        option = int(input("1-4: "))
        if option == 1:
            train()
            pokemon_evolve1()
            pokemon_evolve2()
            days()
        elif option == 2:
            gym_battle()
            pokemon_evolve1()
            pokemon_evolve2()
            days()
        elif option == 3:
            rest()
            mood()
            record()
            if pokemon_level < 5:
                draw_gastly()
            pokemon_evolve1()
            pokemon_evolve2()
            days()
        elif option == 4:
            print("Bye")
            break

