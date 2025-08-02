# phone=input("enter number ")
# digits_mapping={
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four"
# }
# out=""
# for ch in phone:
#     out+=digits_mapping.get(ch,"!")+ " "
# print(out)

message=input(">")
words=message.split(' ')
emojis={
    " :)":"😁",
    "(:":"🥺",
    "!":"🖕"
}
out=""
for word in words:
    out+=emojis.get(word,word)+" "
print(out)