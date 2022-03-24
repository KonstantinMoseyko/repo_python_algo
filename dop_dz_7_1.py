
class Solution():
    def __init__(self,dictionary,sentence):
        self.dictionary = dictionary
        self.sentence = sentence
    def replaceWords(self):
        dictionary = sorted(self.dictionary, key=len)
        print(dictionary)
        result = []
        for word in self.sentence.split(" "):
            point = 1
            for elem in dictionary:
                if len(elem)<len(word) and word.startswith(elem):
                    result.append(elem)
                    point = 0
                    break
            if point == 1:
                result.append(word)
        return " ".join(result)
array = Solution(["catt","bat","rat"],'the cattle was rattled by the battery')
print(array.replaceWords())



# Output: "the cat was rat by the bat"
