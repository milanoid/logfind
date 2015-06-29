import os


class LogFind(object):
    def __init__(self):
        pass

    def get_home(self):
        return os.path.expanduser('~')


def main():
    print LogFind().get_home()


if __name__ == "__main__":
    main()
