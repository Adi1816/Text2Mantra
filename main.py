import sys
def count_matras(word):
    c1 = 0
    c2 = 0
    count = 0
    i = 0
    a = []
    scansion = ""  # Initialize an empty string to store the scansion

    while i < len(word):
        char = word[i]

        if char in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ',
                      'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                      'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़'] and i+1<len(word) and word[i + 1] == 'ृ' :
            if (c1 == 0):
                c1 += 1
                count += 1
            else:
                c2 += 1
                count += 1
            i += 2

        elif char == 'ड' and i + 2 < len(word) and word[i + 1] == '़' and word[i + 2] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']:
            if (c1 == 0):
                c1 += 2
                count += 2
            else:
                c2 += 2
                count += 2
            i += 3


        elif char == 'ढ' and i + 2 < len(word) and word[i + 1] == '़' and word[i + 2] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']:
            if (c1 == 0):
                c1 += 2
                count += 2
            else:
                c2 += 2
                count += 2
            i += 3

        elif char == 'ढ' and i + 1 < len(word) and word[i + 1] == '़':
            if (c1 == 0):
                c1 += 2
                count += 2
            else:
                c2 += 2
                count += 2
            i += 2

        elif char == 'म' and i + 3 < len(word) and word[i + 1] == '्' and word[i + 2] == 'ह' and word[i + 3] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']:
            if (c1 == 0):
                c1 += 2
                count += 2
            else:
                c2 += 2
                count += 2

            i += 4

        elif char == 'न' and i + 3 < len(word) and word[i + 1] == '्' and word[i + 2] == 'ह' and word[i + 3] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']:
            if (c1 == 0):
                c1 += 2
                count += 2
            else:
                c2 += 2
                count += 2

            i += 3

        elif char == 'ल' and i + 3 < len(word) and word[i + 1] == '्' and word[i + 2] == 'ह' and word[i + 3] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']:
            if (c1 == 0):
                c1 += 2
                count += 2
            else:
                c2 += 2
                count += 2

            i += 3


        elif char == 'म' and i + 2 < len(word) and word[i + 1] == '्' and word[i + 2] == 'ह':
            if (c1 == 0):
                c1 += 1
                count += 1
            else:
                c2 += 1
                count += 1

            i += 3

        elif char == 'न' and i + 2 < len(word) and word[i + 1] == '्' and word[i + 2] == 'ह':
            if (c1 == 0):
                c1 += 1
                count += 1
            else:
                c2 += 1
                count += 1

            i += 3

        elif char == 'ल' and i + 2 < len(word) and word[i + 1] == '्' and word[i + 2] == 'ह':
            if (c1 == 0):
                c1 += 1
                count += 1
            else:
                c2 += 1
                count += 1

            i += 3

        elif char == 'अ' and i + 1 < len(word) and word[i + 1] == 'ं':
            if (c1 == 0):
                c1 += 2
                count += 2
            else:
                c2 += 2
                count += 2

            i += 2

        elif char in ['अ', 'इ', 'उ', 'ऋ']:
            if (c1 == 0):
                c1 += 1
                count += 1
            else:
                c2 += 1
                count += 1

            i += 1

        elif char in ['आ', 'ई', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ', 'अं']:
            if (c1 == 0):
                c1 += 2
                count += 2
            else:
                c2 += 2
                count += 2

            i += 1


        elif char == 'क' and i < len(word) - 3 and word[i + 1] == '्' and word[i + 2] == 'ष' and word[i + 3] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']:
            if (c1 == 0):
                c1 += 2
                count += 2
            else:
                c2 += 2
                count += 2

            i += 4

        elif char == 'त' and i < len(word) - 3 and i != 0 and word[i + 1] == '्' and word[i + 2] == 'र' and word[i + 3] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']:
            if (c1 < 2):
                c1 += 1
                count += 1

            c2 += 2
            count += 2

            i += 4

        elif char == 'त' and i + 2 < len(word) and i != 0 and word[i + 1] == '्' and word[i + 2] == 'र':
            if (c1 < 2):
                c1 += 1
                count += 1

            c2 += 1
            count += 1

            i += 3

        elif char == 'त' and i < len(word) - 3 and word[i + 1] == '्' and word[i + 2] == 'र' and word[i + 3] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']:
            if (c1 == 0):
                c1 += c2
                count += c1
            else:
                c2 += 2
                count += 2

            i += 4

        elif char == 'त' and i + 2 < len(word) and word[i + 1] == '्' and word[i + 2] == 'र':
            if (c1 == 0):
                c1 += 1
                count += 1
            else:
                c2 += 1
                count += 1

            i += 3

        elif char == 'श' and i < len(word) - 1 and i + 3 < len(word) and word[i + 1] == '्' and word[i + 2] == 'र' and word[i + 3] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']:
            if (c1 == 0):
                c1 += 2
                count += 2
            else:
                c2 += 2
                count += 2

            i += 4

        elif char == 'श' and i + 2 < len(word) and word[i + 1] == '्' and word[i + 2] == 'र':
            if (c1 == 0):
                c1 += 1
                count += 1
            else:
                c2 += 1
                count += 1

            i += 3

        elif char == 'ज' and i + 3 < len(word) and word[i + 1] == '्' and word[i + 2] == 'ञ' and word[i + 3] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']:
            if (c1 == 0):
                c1 += 2
                count += 2
            else:
                c2 += 2
                count += 2

            i += 4

        elif char == 'ज' and i + 2 < len(word) and word[i + 1] == '्' and word[i + 2] == 'ञ':
            if (c1 == 0):
                c1 += 1
                count += 1
            else:
                c2 += 1
                count += 1

            i += 3

        elif (char in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ',
                       'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                       'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़'] and
              i + 1 < len(word) and word[i + 1] in ['ँ']):
            if (c1 == 0):
                c1 += 1
                count += 1
            else:
                c2 += 1
                count += 1

            i += 2


        elif (char in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ',
                       'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                       'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़'] and
              i + 2 < len(word) and word[i + 1] in ['ि']) and word[i + 2] == 'ं':
            if (c1 == 0):
                c1 += 1
                count += 1
            else:
                c2 += 1
                count += 1

            i += 3

        elif (char in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ',
                       'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                       'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़'] and
              i + 2 < len(word) and word[i + 1] in ['ी', 'ौ', 'ो']) and word[i + 2] == 'ं':
            if (c1 == 0):
                c1 += 2
                count += 2
            else:
                c2 += 2
                count += 2

            i += 3


        elif (char in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ',
                       'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                       'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़'] and
              i + 2 < len(word) and word[i + 1] in ['ि', 'ु', 'ऋ']) and word[i + 2] == 'ं':
            if (c1 == 0):
                c1 += 2
                count += 2
            else:
                c2 += 2
                count += 2

            i += 3

        elif (char in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ',
                       'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                       'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़'] and
              i + 2 < len(word) and word[i + 1] in ['ि', 'ु', 'ऋ']) and word[i + 2]=='ँ':
            if (c1 == 0):
                c1 += 1
                count += 1
            else:
                c2 += 1
                count += 1

            i += 3

        elif (char in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ',
                       'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                       'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़'] and
              i + 1 < len(word) and word[i + 1] in ['ि', 'ु', 'ऋ']):
            if (c1 == 0):
                c1 += 1
                count += 1
            else:
                c2 += 1
                count += 1

            i += 2

        elif (char in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ',
                       'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                       'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़'] and
              i < len(word) - 2 and word[i + 1] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']) and word[i + 2]=='ँ':
            if (c1 == 0):
                c1 += 2
                count += 2
            else:
                c2 += 2
                count += 2

            i += 3

        elif (char in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ',
                       'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                       'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़'] and
              i < len(word) - 1 and word[i + 1] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']):
            if (c1 == 0):
                c1 += 2
                count += 2
            else:
                c2 += 2
                count += 2

            i += 2

        elif (char in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ',
                       'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                       'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़'] and
              i < len(word) - 1 and word[i + 1] == '्' and (i == 0 or word[i - 1] == ' ')):
            i += 2


        elif (char in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ',
                       'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                       'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़'] and
              i < len(word) - 1 and word[i + 1] == '्' and c1 == 2):
            i += 2


        elif (char in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ',
                       'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                       'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़'] and
              i < len(word) - 3 and word[i + 1] == '्' and word[i + 2] == 'ह' and word[i + 3] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']):
            i += 2


        elif (char in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                       'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़'] and
              i < len(word) - 1 and word[i + 1] == '्' and i - 1 >= 0 and word[i - 1] != '्'):
            c1 += 1
            count += 1
            i += 2

        elif (char in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                       'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़'] and
              i < len(word) - 1 and word[i + 1] == '्'):
            i += 2



        elif char in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ',
                      'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                      'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़']:
            if (c1 == 0):
                c1 += 1
                count += 1
            else:
                c2 += 1
                count += 1

            i += 1


        else:
            i += 1
            if(c1 > 0):
              # sys.stdout.write(str(c1))
              scansion += str(c1)
              # a.append(" ")
              c1 = c2
              c2 = 0
              # sys.stdout.write(" ")
              scansion += " "

        if (c2 > 0):
            # sys.stdout.write(str(c1))
            scansion += str(c1)
            # a.append(" ")
            c1 = c2
            c2 = 0

    if (c1 > 0):
        scansion += str(c1)

    return scansion, count

# Example usage:
# devanagari_word = ("")
# result = count_matras(devanagari_word)
# print(result)

# Function to process a file and print output for each line
def group_scansions(scansion, word):
    # grouped_scansions = []
    current_group = "]]"
    sum = 0
    k = 0
    j = len(word) - 1
    flag = True # Variable to track the condition

    for i in range(len(scansion) - 1, -1, -1):
        test = word[j]
        digit = scansion[i]

        while ( word[j] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '।', ',', '॥'] ):
            j -= 1

        test = word[j]


        if word[j] == ' ':
            k = 0
            sum = 0
            if (current_group[0] != '[' and current_group[0] != ']'):
                current_group = "]] [[" + current_group
            else:
                current_group = "]] [" + current_group[1:]


            j -= 1
          # Fix: Use len(word) instead of word.length()
        if word[j] == 'ँ':
            j -= 1
            # flag = False
        if word[j] == 'ं':
            j -= 1

        if word[j] == '्':
            j -= 2

        if word[j] == 'ृ':
            j -= 1

        if digit == ' ':
            k = 0
            # current_group = " " + current_group
            continue
            # if(current_group[0]!=']'):
            #  current_group =  " [" + current_group
            # else:
            #  current_group=current_group[0]+" "+current_group[1:]

        if digit in ['1', '2'] and word[j] in ['अ', 'इ', 'उ', 'ऋ', 'आ', 'ई', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ', 'अं']:
            if (i + 1 < len(scansion) and scansion[i + 1] == ' ') or (i == len(scansion) - 1):
                k = 1

            sum = 0
            current_group = "]" + "[" + digit + current_group
            if word[j - 1] == 'ँ' or word[j - 1] == '़' or word[j - 1] == '्':
                j -= 2
            else:
                j -= 1


        elif digit == '1' and word[j] in ['ि', 'ु', 'ऋ']:
            if (i + 1 < len(scansion) and scansion[i + 1] == ' ') or (i == len(scansion) - 1):
                k = 1

            sum = 0
            current_group = "]" + "[" + digit + current_group

            if word[j - 2] == 'त' and j - 2 >= 0 and word[j - 1] == '्' and word[j] == 'र':
                j -= 3

            elif word[j - 2] == 'श' and j - 2 >= 0 and word[j - 1] == '्' and word[j] == 'र':
                j -= 3

            elif word[j - 2] == 'ज' and j - 2 >= 0 and word[j - 1] == '्' and word[j] == 'ञ':
                j -= 3

            elif word[j - 2] == 'श' and j - 2 >= 0 and word[j - 1] == '्' and word[j] == 'र' :
                j -= 3

            elif word[j - 1] == 'ँ' or word[j - 1] == '़' :
                j -= 3
            else:
                if word[j - 1] == ' ':
                    j -= 1
                else:
                    j -= 2

        elif digit == '1' and word[j] in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ',
                       'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                       'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़'] and k == 1:
            k = 0
            sum = 0
            current_group = "]" + "[" + digit + current_group

            if word[j - 2] == 'त' and j - 2 >= 0 and word[j - 1] == '्' and word[j] == 'र':
                j -= 3

            elif word[j - 2] == 'श' and j - 2 >= 0 and word[j - 1] == '्' and word[j] == 'र':
                j -= 3

            elif word[j - 2] == 'ज' and j - 2 >= 0 and word[j - 1] == '्' and word[j] == 'ञ':
                j -= 3

            elif word[j - 2] == 'श' and j - 2 >= 0 and word[j - 1] == '्' and word[j] == 'र':
                j -= 3

            elif word[j - 1] == '्':
                j -= 3

            elif word[j - 1] == 'ँ' or word[j - 1] == '़':
                j -= 2

            else:
                j -= 1

        elif digit == '1':
            k = 0
            sum += (int)(digit)
            if(sum < 2):
             current_group = digit + current_group
            elif sum == 3 or sum == 2:
              current_group = "]["+digit + current_group
              sum = 0
            else:
              current_group =  digit +"]" + "["+ current_group
              sum = 0

            if word[j - 2] == 'त' and j - 2 >= 0 and word[j - 1] == '्' and word[j] == 'र':
                j -= 3

            elif word[j - 2] == 'श' and j - 2 >= 0 and word[j - 1] == '्' and word[j] == 'र':
                j -= 3

            elif word[j - 2] == 'ज' and j - 2 >= 0 and word[j - 1] == '्' and word[j] == 'ञ':
                j -= 3

            elif word[j - 2] == 'श' and j - 2 >= 0 and word[j - 1] == '्' and word[j] == 'र':
                j -= 3

            elif word[j - 1] == '्':
                j -= 3

            elif word[j - 1] == 'ँ' or word[j - 1] == '़':
                j -= 2

            else:
                j -= 1

        else:
            k = 0
            sum += (int)(digit)
            if (sum > 3):
             current_group = "]" + "[" + digit + "]" + "[" + current_group
             sum = 0
            else:
             current_group = "]" + "[" + digit  + current_group
             sum = 0
            # if word[j-3] == 'म' and j - 3 >= 0 and word[j-2] == '्' and word[j-1] == 'ह' and word[j] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']:
            #     j -= 4

            if word[j - 3] == 'क' and j - 3 >= 0 and word[j - 2] == '्' and word[j - 1] == 'ष' and word[j] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']:
                j -= 4

            elif word[j - 3] == 'त' and j - 3 >= 0 and i != 0 and word[j - 2] == '्' and word[j - 1] == 'र' and word[j] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']:
                j -= 4

            elif word[j - 3] == 'श' and j - 3 >= 0 and word[j - 2] == '्' and word[j - 1] == 'र' and word[j] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']:
                j -= 4

            elif word[j - 3] == 'ज' and j - 3 >= 0 and word[j - 2] == '्' and word[j - 1] == 'ञ' and word[j] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']:
                j -= 4

            elif j + 1 < len(word)  and word[j + 1] == 'ँ':
                j -= 2

            # elif j+1 <len(word) and (word[j+1]=='ं' or  word[j+1] == 'ँ') and flag:
            #     j -= 1

            # elif word[j-3] == 'न' and j- 3 >= 0 and word[j-2] == '्' and word[j-1] == 'ह' and word[j] in ['ा', 'ी', 'ू', 'ै', 'े', 'ो', 'ौ', 'ं']:
            #     j -= 4
            elif j + 1 < len(word) and  word[j + 1] == 'ं' and word[j] in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ',
                       'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                       'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़'] :
                j -= 1
            elif word[j - 2] == '्':
                j -= 4

            elif word[j - 1] == 'ँ' or word[j - 1] == '़':
                j -= 3

            elif word[j] in ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ञ',
                       'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
                       'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ज्ञ', 'ड़'] :
                j -= 1

            else:
                if word[j - 1] == ' ':
                    j -= 1
                else:
                    j -= 2

        # Print the current_group
    if(current_group[0] == ']'):
      current_group = '[' + current_group[1:]
    else:
        current_group = "[[" + current_group

    print(f"Line: {word}")
    print(f"Scansion: {scansion}")
    print(f"Grouped Scansion: {current_group}")

# def process_file(file_path):
#     with open(file_path, 'r') as file:
#         for line_number, line in enumerate(file, start=0):
#             line = line.strip()
#             if line:
#                 print(f"\n{line}")
#                 result, _ = count_matras(line)
#                 print(result)
                # if (result>0): print(f"-> {result} matras")

def process_file(file_path):
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=0):
            line = line.strip()
            if line:
                words = line.split()
                full_line = ' '.join(words)
                result, _ = count_matras(full_line)
                group_scansions(result, full_line)
                print()

                # print(grouped_scansions)
                # if grouped_scansions:
                # print("->", "".join(grouped_scansions), "matras")

# Example usage:
file_path = "HC.txt"  # Replace with the actual file path
process_file(file_path)
