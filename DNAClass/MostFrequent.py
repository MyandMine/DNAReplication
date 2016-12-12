def PatternCount(k_mer, Text):
    dict = {"AA":0}
    for i in range (len(Text)-k_mer):
        dict.setdefault(Text[i:i+k_mer],0)
        dict[Text[i:i+k_mer]] = dict[Text[i:i+k_mer]] + 1
    frequence = "AA"
    count = 0
    for i in dict:
        if dict[i] > count:
            frequence = i
            count = dict[i]
    return frequence

Text = "GATCCAGATCCCCATAC"
print(PatternCount(2,Text))