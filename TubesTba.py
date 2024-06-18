def tokenRecognizer(word: str):
    word = word.lower()
    try:
        subject_checker = SubjectChecker()
        predicate_checker = PredicateChecker()
        object_checker = ObjectChecker()
        adverb_checker = AdverbChecker()

        if subject_checker.is_subject(word):
            return 'S'
        elif predicate_checker.is_predicate(word):
            return 'P'
        elif object_checker.is_object(word):
            return 'O'
        elif adverb_checker.is_adverb(word):
            return 'K'
        else:
            raise Exception("TokenUnrecognizedError")
    except Exception as e:
        print(f"ERROR: {e}")
        print(f"Word \"{word}\" tidak masuk ke kategori token manapun\n")
        return '?'

class SubjectChecker:
    def is_subject(self, word):
        curr_state = 0
        for letter in word:
            if curr_state == 0:
                if letter == 'a':
                    curr_state = 1
                elif letter == 'k':
                    curr_state = 2
                elif letter == 'd':
                    curr_state = 3
                elif letter == 'm':
                    curr_state = 4
                else:
                    curr_state = -1
            elif curr_state == 1:
                if letter == 'k':
                    curr_state = 5
                else:
                    curr_state = -1
            elif curr_state == 2:
                if letter == 'a':
                    curr_state = 6
                elif letter == 'i':
                    curr_state= 16
                else:
                    curr_state = -1
            elif curr_state == 3:
                if letter == 'i':
                    curr_state = 7
                else:
                    curr_state = -1
            elif curr_state == 4:
                if letter == 'e':
                    curr_state = 8
                else:
                    curr_state = -1
            elif curr_state == 5:
                if letter == 'u':
                    curr_state = 9
                else:
                    curr_state = -1
            elif curr_state == 6:
                if letter == 'm':
                    curr_state = 10
                else:
                    curr_state = -1
            elif curr_state == 7:
                if letter == 'a':
                    curr_state = 11
                else:
                    curr_state = -1
            elif curr_state == 8:
                if letter == 'r':
                    curr_state = 12
                else:
                    curr_state = -1
            elif curr_state == 9:
                return True
            elif curr_state == 10:
                if letter == 'u':
                    curr_state = 13
                else:
                    curr_state = -1
            elif curr_state == 11:
                return True
            elif curr_state == 12:
                if letter == 'e':
                    curr_state = 14
                else:
                    curr_state = -1
            elif curr_state == 13:
                return True
            elif curr_state == 14:
                if letter == 'k':
                    curr_state = 15
                else:
                    curr_state = -1
            elif curr_state == 15:
                if letter == 'a':
                    curr_state = 19
                else:
                    curr_state= -1
                return True
            elif curr_state == 16:
                if letter == 't':
                    curr_state = 17
                else:
                    curr_state = -1
            elif curr_state == 17:
                if letter == 'a':
                    curr_state = 18
                else:
                    curr_state= -1
            elif curr_state == 18:
                return True
            else:
                curr_state = -1
        return curr_state in [9, 11, 13, 19,18]

class PredicateChecker:
    def is_predicate(self, word):
        curr_state = 0
        for letter in word:
            if curr_state == 0:
                if letter == 't':
                    curr_state = 1
                elif letter == 'm':
                    curr_state = 5
                elif letter == 'b':
                    curr_state = 12
                elif letter == 'n':
                    curr_state = 15
                else:
                    curr_state = -1
            elif curr_state == 1:
                if letter == 'i':
                    curr_state = 2
                else:
                    curr_state = -1
            elif curr_state == 2:
                if letter == 'd':
                    curr_state = 3
                else:
                    curr_state = -1
            elif curr_state == 3:
                if letter == 'u':
                    curr_state = 4
                else:
                    curr_state = -1
            elif curr_state == 4:
                if letter == 'r':
                    curr_state = 19
                    return True
                else:
                    curr_state = -1
            elif curr_state == 5:
                if letter == 'i':
                    curr_state = 6
                elif letter == 'a':
                    curr_state = 9
                else:
                    curr_state = -1
            elif curr_state == 6:
                if letter == 'n':
                    curr_state = 7
                else:
                    curr_state = -1
            elif curr_state == 7:
                if letter == 'u':
                    curr_state = 8
                else:
                    curr_state = -1
            elif curr_state == 8:
                if letter == 'm':
                    curr_state = 19
                    return True
                else:
                    curr_state = -1
            elif curr_state == 5:
                if letter == 'a':
                    curr_state = 9
                else:
                    curr_state = -1
            elif curr_state == 9:
                if letter == 'k':
                    curr_state = 10
                else:
                    curr_state = -1
            elif curr_state == 10:
                if letter == 'a':
                    curr_state = 11
                else:
                    curr_state = -1
            elif curr_state == 11:
                if letter == 'n':
                    curr_state = 19
                    return True
                else:
                    curr_state = -1
            elif curr_state == 12:
                if letter == 'a':
                    curr_state = 13
                else:
                    curr_state = -1
            elif curr_state == 13:
                if letter == 'c':
                    curr_state = 14
                else:
                    curr_state = -1
            elif curr_state == 14:
                if letter == 'a':
                    curr_state = 19
                    return True
                else:
                    curr_state = -1
            elif curr_state == 15:
                if letter == 'o':
                    curr_state = 16
                else:
                    curr_state = -1
            elif curr_state == 16:
                if letter == 'n':
                    curr_state = 17
                else:
                    curr_state = -1
            elif curr_state == 17:
                if letter == 't':
                    curr_state = 18
                else:
                    curr_state = -1
            elif curr_state == 18:
                if letter == 'o':
                    curr_state = 11
                else:
                    curr_state = -1
            elif curr_state == 19:
                return True
            else:
                curr_state = -1
        return curr_state in [19]

class ObjectChecker:
    def is_object(self, word):
        curr_state = 0
        for letter in word:
            if curr_state == 0:
                if letter == 'k':
                    curr_state = 1
                elif letter == 'a':
                    curr_state = 3
                elif letter == 'f':
                    curr_state = 5
                elif letter == 'n':
                    curr_state = 8
                elif letter == 'b':
                    curr_state = 11
                else:
                    curr_state = -1
            elif curr_state == 1:
                if letter == 'u':
                    curr_state = 2
                else:
                    curr_state = -1
            elif curr_state == 2:
                if letter == 'e':
                    curr_state = 14
                    return True
                else:
                    curr_state = -1
            elif curr_state == 3:
                if letter == 'i':
                    curr_state = 4
                else:
                    curr_state = -1
            elif curr_state == 4:
                if letter == 'r':
                    curr_state = 14
                    return True
                else:
                    curr_state = -1
            elif curr_state == 5:
                if letter == 'i':
                    curr_state = 6
                else:
                    curr_state = -1
            elif curr_state == 6:
                if letter == 'l':
                    curr_state = 7
                else:
                    curr_state = -1
            elif curr_state == 7:
                if letter == 'm':
                    curr_state = 14
                    return True
                else:
                    curr_state = -1
            elif curr_state == 8:
                if letter == 'a':
                    curr_state = 9
                else:
                    curr_state = -1
            elif curr_state == 9:
                if letter == 's':
                    curr_state = 10
                else:
                    curr_state = -1
            elif curr_state == 10:
                if letter == 'i':
                    curr_state = 14
                    return True
                else:
                    curr_state = -1
            elif curr_state == 11:
                if letter == 'u':
                    curr_state = 12
                else:
                    curr_state = -1
            elif curr_state == 12:
                if letter == 'k':
                    curr_state = 13
                else:
                    curr_state = -1
            elif curr_state == 13:
                if letter == 'u':
                    curr_state = 14
                    return True
                else:
                    curr_state = -1
            elif curr_state == 14:
                return True
            else:
                curr_state = -1
        return curr_state in [14]

class AdverbChecker:
    def is_adverb(self, word):
        curr_state = 0
        for letter in word:
            if curr_state == 0:
                if letter == 'd':
                    curr_state = 1
                elif letter == 'm':
                    curr_state = 18
                elif letter == 'p':
                    curr_state = 26
                else:
                    curr_state = -1
            elif curr_state == 1:
                if letter == "i":
                    curr_state = 2
                else:
                    curr_state = -1
            elif curr_state == 2:
                if letter == 'r':
                    curr_state = 3
                elif letter == 'k':
                    curr_state = 8
                else:
                    curr_state = -1
            elif curr_state == 3:
                if letter == 'u':
                    curr_state = 4
                else:
                    curr_state = -1
            elif curr_state == 4:
                if letter == 'm':
                    curr_state = 5
                else:
                    curr_state = -1
            elif curr_state == 5:
                if letter == 'a':
                    curr_state = 6
                else:
                    curr_state = -1
            elif curr_state == 6:
                if letter == 'h':
                    curr_state = 7
                else:
                    curr_state = -1
            elif curr_state == 8:
                if letter == 'a':
                    curr_state= 9
                else:
                    curr_state = -1
            elif curr_state == 9:
                if letter == 'm':
                    curr_state= 10
                elif letter == 'n':
                    curr_state =14
                else:
                    curr_state = -1
            elif curr_state == 10:
                if letter == 'p':
                    curr_state= 11
                else:
                    curr_state = -1
            elif curr_state == 11:
                if letter == 'u':
                    curr_state= 12
                else:
                    curr_state = -1
            elif curr_state == 12:
                if letter == 's':
                    curr_state= 13
                else:
                    curr_state = -1
            elif curr_state == 14:
                if letter == 't':
                    curr_state= 15
                else:
                    curr_state = -1
            elif curr_state == 15:
                if letter == 'i':
                    curr_state = 16
                else:
                    curr_state = -1
            elif curr_state == 16:
                if letter == 'n':
                    curr_state= 17
                else:
                    curr_state = -1
            elif curr_state == 18:
                if letter == 'a':
                    curr_state = 19
                else:
                    curr_state = -1
            elif curr_state == 19:
                if letter == 'l':
                    curr_state= 20
                else:
                    curr_state = -1
            elif curr_state == 20:
                if letter == 'a':
                    curr_state = 21 
                else:
                    curr_state = -1
            elif curr_state == 21:
                if letter == 'm':
                    curr_state= 22
                else:
                    curr_state = -1
            elif curr_state == 22:
                if letter == 'i':
                    curr_state= 23
                else:
                    curr_state = -1
            elif curr_state == 23:
                if letter == 'n':
                    curr_state= 24
                else:
                    curr_state = -1
            elif curr_state == 24:
                if letter == 'i':
                    curr_state=25
                else:
                    curr_state = -1
            elif curr_state == 26:
                if letter == 'a':
                    curr_state=27
                else:
                    curr_state = -1
            elif curr_state == 27:
                if letter == 'g':
                    curr_state=28
                else:
                    curr_state = -1
            elif curr_state == 28:
                if letter == 'i':
                    curr_state=22
                else:
                    curr_state = -1
            elif curr_state == 23:
                if letter == 'n':
                    curr_state= 24
                else:
                    curr_state = -1
            elif curr_state == 24:
                if letter == 'i':
                    curr_state= 25
                else:
                    curr_state = -1
           
            elif curr_state == 25:
                return True
            elif curr_state == 7 :
                return True
            elif curr_state == 13 :
                return True
            elif curr_state == 17 :
                return True
            elif curr_state == 32:
                return True
        return curr_state in [7,13,17,25]
                
                          
def parser(sentence):
    try:
        words = sentence.split()
        words.append('')

        stack = ['#', 'X']
        res = []

        i = 0
        while stack[-1] != '#':
            word = words[i]
            token = tokenRecognizer(word)

            top = stack[-1]

            if top == 'X':
                if token == 'S':
                    stack.pop()
                    stack.extend(['Y', 'P', 'S'])
                else:
                    raise Exception("ParsingError")
            elif top == 'Y':
                if word == '':
                    stack.pop()
                elif token == 'O':
                    stack.pop()
                    stack.extend(['Z', 'O'])
                elif token == 'K':
                    stack.pop()
                    stack.append('Z')
                else:
                    raise Exception("ParsingError")
            elif top == 'Z':
                if word == '':
                    stack.pop()
                elif token == 'K':
                    stack.pop()
                    stack.append('K')
                else:
                    raise Exception("ParsingError")
            elif top in ['S', 'P', 'O', 'K']:
                if token == top:
                    res.append(stack.pop())
                    stack.append(word)
                else:
                    raise Exception("ParsingError")
            else:
                if token != '?':
                    stack.pop()
                    i += 1
                else:
                    raise Exception("ParsingError")

        print("Struktur: ", end='')
        print(' - '.join(res))

        return True
    except Exception as e:
        print(f"ERROR: {e}")
        print(f"Kalimat \"{sentence}\" struktur tidak sesuai\n")
        return False
if __name__ == '__main__':  
    sentence = input("Kalimat: ")
    print()
    print(f"String: {sentence}\nStatus: Diterima\n") if parser(sentence) else print(f"String: {sentence}\nStatus: Ditolak \n") # type: ignore