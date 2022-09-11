class Test():
    # something = 1
    # print(something)


    def thing(self):
        self.something = 3
        print(self.something)
    

    def after(self):
        print(self.something)


c = Test()

c.thing()

c.after()
