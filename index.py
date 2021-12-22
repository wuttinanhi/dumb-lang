from src.filereader import FileReader
from src.interpreter import Interpreter
from src.parser import Parser


def main():
    scripts = FileReader.read("scripts/v2.dumb")
    parser = Parser(scripts)
    module = parser.parse()
    module.exec()


if __name__ == "__main__":
    main()
