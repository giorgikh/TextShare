import os
from pathlib import Path


class ManagePath():
    def __init__(self):
        try:
            modulePath = os.path.abspath(__file__)
            print(modulePath)
        except Exception as ex:
            print(ex)

    def createTmpFolder(self, filePath, userId):
        try:
            Path(
                f'{filePath}/templates/tmp/{userId}').mkdir(parents=True, exist_ok=True)
            print(filePath)
        except Exception as ex:
            print(ex)

    def createFile(self, filePathWithName):
        try:
            print(filePathWithName)
            Path(filePathWithName).touch()
        except Exception as ex:
            print(ex)

    def writeTextToFile(self, filePath, text):
        if Path(filePath).exists():
            file = Path(filePath)
            file.write_text(text)

    def appendTextToFile(self, filePath, text):
        if Path(filePath).exists():
            try:
                f = Path(filePath).open('a')
                f.write(text)
                f.close()
            except Exception as ex:
                print(ex)
