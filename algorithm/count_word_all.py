

#统计一句话中单词的数量
#"I am a good boy!You too!"
def count_words(s):
    if not isinstance(s,str):
        return None

    word_list = s.split()
    #print(word_list)

    #把非字母的内容替换为空格
    #遍历一下字符串把非字母的替换为空格

    new_s = ""
    for i in s:
        if (i>='a' and i<='z') or (i>='A' and i<='Z'):
            new_s+=i
        else:
            new_s+=" "

    return len(new_s.split())


sentence = "I am a good boy!You too!"
print(count_words(sentence))