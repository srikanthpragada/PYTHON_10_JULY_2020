st = "How do you do"

for ch in sorted(set(st)):
    print(f"{ch} - {st.count(ch)}")
