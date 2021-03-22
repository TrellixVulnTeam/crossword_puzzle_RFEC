from grid import Grid


def run():
    crossword_ = ["xx------x--",
                  "x--x-x-xxx-",
                  "-x-x---x---",
                  "-x-x-x-xxx-",
                  "---x-x-----",
                  "-xx---x-xxx",
                  "-x-x-xx---x",
                  "-----xx-x-x",
                  "-x-xx----x-",
                  "-xxxx-x-xx-",
                  "----x-x----"]

    crossword_ = ["".join(list(map(lambda x: x if not x.isalpha() else ".", string))) for string in crossword_]
    words = ["GE",
             "GM",
             "MS",
             "Big",
             "CIA",
             "FBI",
             "JFK",
             "Las",
             "pig",
             "spy",
             "USA",
             "dime",
             "Ford",
             "yank",
             "applepie",
             "eagle",
             "Elvis",
             "Sears",
             "stars",
             "White",
             "states",
             "Liberty",
             "Hollywood"]
    words = list(map(lambda x: x.upper(), words))
    grid_ = Grid(crossword_)
    print(grid_.insert_words(words))


if __name__ == '__main__':
    run()
