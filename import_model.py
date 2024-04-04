from os import system

def import_model():
    try:
        import psutil
    except:
        system("pip install psutil")

if __name__ == '__main__':
    import_model()