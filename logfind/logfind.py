import os


class LogFind(object):
    def __init__(self):
        pass

    def get_home(self):
        """
         Return home path of the user.
        :return:
        """
        return os.path.expanduser('~')

    def load_config_file(self, filename='.logfind'):
        """
         Load config file with regex on each line.
        :param filename: [optional] name of the config file
        :return: list
        """
        try:
            config_file = open(self.get_home() + "\\" + filename)
        except IOError:
            raise

        regex_list = []
        for line in config_file:
            regex_list.append(line.strip())

        config_file.close()
        return regex_list


def main():
    print LogFind().get_home()
    print LogFind().load_config_file()


if __name__ == "__main__":
    main()
