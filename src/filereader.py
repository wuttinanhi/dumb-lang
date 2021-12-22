class FileReader:
    @staticmethod
    def read(filepath: str):
        file = open(file=filepath, mode="r")
        return file.read()
