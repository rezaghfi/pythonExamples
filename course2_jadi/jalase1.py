with open('./course2_jadi/persian_dict_19k.txt', encoding='utf8') as f:
  lines = f.read().split("\n")

words = []
for line in lines:
  words.append(line.split(":")[0])

# print(words)

for word in words:
  for p in ["من", "ما"]:
    if p + word in words:
      s = "به {} نگو {} ، {}{} تو نیستم.".format(p, word,p,word)
      if(p == "ما"):
        s.replace("نیست","نیستیم")
      print(s)

def add(i):
  return 