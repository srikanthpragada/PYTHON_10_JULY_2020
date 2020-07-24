def count_upper(st):
    count = 0
    for ch in st:
        if ch.isupper():
            count += 1

    return count


def count_word(st):
    return len(st.split(" "))



