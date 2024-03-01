from interface import Interface
from request import Requests
from parser import Parser

def main():
    request = Requests("english", "french", "apple")
    result = request.make_request()
    reader = Parser(result)
    print(reader.language_translation())

if __name__ == "__main__":
    main()