import os

def main(argv):
    print("Hello World!")
    secret="12345"
    password="4543"
    startdir = os.path.abspath(os.curdir)
    requested_path = os.path.relpath(argv, startdir)
    print(requested_path)
    tfile = open(requested_path, 'rb')
    
    
if __name__ == "__main__":
    main(sys.argv[1:])
