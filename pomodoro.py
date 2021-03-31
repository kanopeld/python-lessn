from abc import abstractmethod, ABC


class LoggerInterface(ABC):
    @abstractmethod
    def log(self, message: str):
        raise NotImplemented


class FileLogger(LoggerInterface):
    def __init__(self, pathToFile: str):
        with open(pathToFile, 'a') as file:
            self.file = file

    def log(self, message: str):
        self.file.write(message)


class DatabaseLogger(LoggerInterface):
    def __init__(self, pathToFile: str):
        with open(pathToFile, 'a') as file:
            self.file = file

    def log(self, message: str):
        self.file.write(message)


class Pomodoro:
    def __init__(self, logger: LoggerInterface):
        self.logger = logger


if __name__ == '__main__':
    file_logger = FileLogger('log.txt')
    file_logger.log(1)

    # pomodoro = Pomodoro(file_logger)
