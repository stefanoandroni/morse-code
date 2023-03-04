from models import MorseCodeTranslator

def main():
    translator = MorseCodeTranslator()
    
    # encrypt
    string = "STRING EXAMPLE"
    result = translator.encrypt(string)
    print(result)
 
    # decrypt
    string = "... - .-. .. -. --.  . -..- .- -- .--. .-.. ."
    result = translator.decrypt(string)
    print (result)
 
if __name__ == '__main__':
    main()