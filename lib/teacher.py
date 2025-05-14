#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Math", "Science", "History"] #teacher's knowledge   
        #self.knowledge = random.choice(self.knowledge)
    
    def teach(self):
        return self.knowledge[0]
        #return self.knowledge[random.randint(0, len(self.knowledge)-1)]
        