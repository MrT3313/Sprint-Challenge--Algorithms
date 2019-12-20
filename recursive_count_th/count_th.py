'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Function Setup
    test = 'th'
    result = []

    windowSize = len(test)
    n = len(word) - windowSize

    recurse(test, word, n, windowSize, result)

    output = f''
    output += f'__FINAL RESULT__ : {result} \n'
    output += f'{len(result)} instances of {test} was found'
    print(output)

    return len(result)

def recurse(passedTest, passedWord, n, passedWindowSize, result):
    # Base Case
    if n < 0:
        print('__BASE CASE__ : n == 0')
        print('__ RECURSION RESULT__ : ', result)
        return 

    # RECURSION
    # -1- # Recursion Work

    startWindow = n
    endWindow = n + passedWindowSize

    if passedWord[startWindow : endWindow] == passedTest:
        print(f'Start Position: {startWindow} // End Position: {endWindow}')

        result.append((startWindow, endWindow))
        print(result)

    # -2- # REcursion Call
    recurse(passedTest, passedWord, n - 1, passedWindowSize, result)




# count_th("")
# count_th("abcthxyz")
# count_th("abcthefthghith")
# count_th("thhtthht")
count_th("THtHThth")