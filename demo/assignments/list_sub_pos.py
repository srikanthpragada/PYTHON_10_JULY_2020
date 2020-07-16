st = "How do you do"
word = "o"

pos = -1
while True:
    pos = st.find(word, pos + 1)
    if pos == -1:
        break

    print(pos)
