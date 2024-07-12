print('C:\some\name')
#\s and \t will be assumed as escape sequence by system. As we don't have escape sequence as \s so it
#will be printed but when it comes to \n, we use this for new line. So when the output comes after
#\n will be printed in new line.
print(r"C:\some\name") # r means raw. To solve above issue we use r.