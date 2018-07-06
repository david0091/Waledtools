from cx_Freeze import setup, Executable

setup(name = "Game_of_life_exe" ,
      version = "0.1" ,
      description = "Game of life on  windows" ,
      executables = [Executable("Game_of_life.py")])


