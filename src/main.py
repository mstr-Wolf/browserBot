import sys

sys.path.append("/home/lo/bin/git/browserBot/src")

from attendClass import GoogleClass, ZoomClass

if __name__ == "__main__" and len(sys.argv) >= 5:
    sys.argv[1].lower()
    if sys.argv[1] == "meet" or sys.argv[1] == "google":
        try:
            benThe_Clock = GoogleClass(code=sys.argv[2], class_length=float(sys.argv[3]), hour=int(sys.argv[4]), minute=int(sys.argv[5]))
            benThe_Clock.run()
        except KeyboardInterrupt:
            sys.exit()
    elif sys.argv[1] == "zoom":
        try:
            benThe_Clock = ZoomClass(code=sys.argv[2], class_length=float(sys.argv[3]), hour=int(sys.argv[4]), minute=int(sys.argv[5]))
            benThe_Clock.run()
        except KeyboardInterrupt:
            sys.exit()

elif __name__ == "__main__" and len(sys.argv) < 5:
    print("Execution example:\n\tpython3 main.py [platform] [code] [length] [target hour] [target minute]")
    print("Platforms:\n\tgoogle (meet)\n\tzoom")
