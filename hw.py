class Parent:
    def __init__(self, arg_txt=None):
        self.arg_txt = arg_txt
    def set(self, arg_txt=None):
        if arg_txt == None:
            self.arg_txt="Текст"




class Child(Parent):
    def __init__(self, arg_txt, arg_num):
        super().__init__(arg_txt)
        self.arg_num=arg_num

child=Child("Текст", 123)
print(child.arg_txt)
print(child.arg_num)
