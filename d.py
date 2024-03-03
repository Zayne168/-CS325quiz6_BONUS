from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def debug(self, message):
        pass
    @abstractmethod
    def info(self, message):
        pass
    @abstractmethod
    def warning(self, message):
        pass
    @abstractmethod
    def error(self, message):
        pass
      
class Application:
    def __init__(self, logger: Logger):
        self.logger = logger
    def performTask(self):
        # Example application logic
        self.logger.debug("Debug message")
        self.logger.info("Information message")
        self.logger.warning("Warning message")
        self.logger.error("Error message")
      
class ConsoleLogger(Logger):
    def debug(self, message):
        print(f"[DEBUG] {message}")
    def info(self, message):
        print(f"[INFO] {message}")
    def warning(self, message):
        print(f"[WARNING] {message}")
    def error(self, message):
        print(f"[ERROR] {message}")
      
class FileLogger(Logger):
    def __init__(self, file_path):
        self.file_path = file_path
    def debug(self, message):
        with open(self.file_path, "a") as file:
            file.write(f"[DEBUG] {message}\n")
    def info(self, message):
        with open(self.file_path, "a") as file:
            file.write(f"[INFO] {message}\n")
    def warning(self, message):
        with open(self.file_path, "a") as file:
            file.write(f"[WARNING] {message}\n")
    def error(self, message):
        with open(self.file_path, "a") as file:
            file.write(f"[ERROR] {message}\n")
          
def main():
    #usage:
    console_logger = ConsoleLogger()
    file_logger = FileLogger("app.log")
    app = Application(console_logger)
    app.performTask()
    appLogged = Application(file_logger)
    appLogged.performTask()
if __name__ == "__main__":
    main()

#this shows DIP through the useage of seperating the main logger into seperate 
#classes(decoupling the logger). The testability is improved since any specific 
#method from a class can be tested individually. Adding more output options is very 
#easy since the logger class is abstracted. We can already output to the application, 
#to a file, and to the console if implemented fully. We could also go on to add 
#seperate subclasses for the logger to take inputs from instead of a string method 
#with ease through abstract classes that the input subclasses would inherit.