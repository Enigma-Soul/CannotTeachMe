from os import system
from sys import executable
def import_model():
    try:
        import psutil
    except:
        system(f"{executable} -m pip install psutil")

if __name__ == '__main__':
    import_model()