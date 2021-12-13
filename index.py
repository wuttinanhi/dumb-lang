from src.filereader import FileReader
from src.interpreter import Interpreter

def main():
    scripts = FileReader.read("scripts/hello.dumb")
    interpreter = Interpreter(scripts)
    interpreter.execute()

if __name__ == "__main__":
    main()
