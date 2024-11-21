class StringManipulation:
    def __init__(self,words):
        self.words = words

    def total_words(self):
        return len(self.words)
    
    def count(self,someword):
        somecount = 0
        for word in self.words:
            if word == someword:
                somecount = somecount+1
        return somecount
    
    def words_of_lenght(self,lenght)->list:
        # self.lencount = lencount // no need for this is this is not part of class only argument
        lencount_lst = []
        for word in self.words:
            if len(word)==lenght:
                lencount_lst.append(word)
        return lencount_lst
    
    def words_start_with(self,c)->list:
        start_list = []
        for word in self.words:
            if word.startswith(c):
                start_list.append(word)
        return start_list
    
    def longest_word(self):
        return max(self.words, key=len)
    
    def palindromes(self):
        pali_list = []
        for word in self.words:
            if(word[::-1]==word):
                pali_list.append(word)
        return pali_list
     
list1 = ["hello","hi","asda","ggfsd","uiertui","abcba"]
s1 = StringManipulation(list1)
print(s1.total_words())

print(s1.count("hi"))
print(s1.words_start_with('h'))
print(s1.words_of_lenght(2))
print(s1.longest_word())
print(s1.palindromes())






