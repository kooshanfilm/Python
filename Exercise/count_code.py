#
# Return the number of times that the string "code"
# appears anywhere in the given string,
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.
#
#
# count_code('aaacodebbb')  1
# count_code('codexxcode')  2
# count_code('cozexxcope')  2


def count_code(str):
    count = 0
    i = 0
    while "co" in str[i:]:
        if len(str[i + str[i:].index("co"):]) >= 4 and str[i + 3 + str[i:].index("co")] == "e":
            count += 1
        i += str[i:].index("co") + 3
    return count


print (count_code("cozexxcope"))