# -*- coding: utf-8 -*-

import sys

class Brainfuck(object):

    actions = []
    action_pos = 0

    pointer = []
    position = 0

    
    def readScript(self, strings):
        self.actions = ''
        self.action_pos = 0
        self.position = 0
        self.pointer = [0]
        
        self.actions = strings
        return self


    def exe(self):

        while len(self.actions) > self.action_pos:
            act = self.actions[self.action_pos]
            if '>' == act:
                self.incrementPosition()
            elif '<' == act:
                self.decrementPosition()
            elif '+' == act:
                self.incrementPointer()
            elif '-' == act:
                self.decrementPointer()
            elif '.' == act:
                self.printPointer()
            elif ',' == act:
                self.setPointer()
            elif '[' == act:
                self.jumpToClose()
            elif ']' == act:
                self.jumpToOpen()

            self.action_pos += 1


    def jumpToClose(self):
        if self.pointer[self.position] == 0:
            open_counter = 0
            while True:
                self.action_pos += 1
                if self.actions[self.action_pos] == '[':
                    open_counter += 1
                elif self.actions[self.action_pos] == ']':
                    if open_counter == 0:
                        break
                    open_counter -= 1


    def jumpToOpen(self):
        if self.pointer[self.position] != 0:
            close_counter = 0
            while True:
                self.action_pos -= 1
                if self.actions[self.action_pos] == ']':
                    close_counter += 1
                elif self.actions[self.action_pos] == '[':
                    if close_counter == 0:
                        break
                    close_counter -= 1


    def incrementPosition(self):
        self.position += 1
        if len(self.pointer) <= self.position:
            self.pointer.append(0)

    def decrementPosition(self):
        self.position -= 1

    def incrementPointer(self):
        self.pointer[self.position] +=1

    def decrementPointer(self):
        self.pointer[self.position] -=1

    def printPointer(self):
        num = self.pointer[self.position]
        sys.stdout.write(unichr(num))

    def setPointer(self):
        c = self.getchar()
        
        if len(self.pointer) <= self.position or len(self.pointer) == 0:
            self.pointer.append(c)
            return
            
        self.pointer[self.position] = self.getchar()


    def printPosition(self):
        print self.position


    def getchar(self):
        c = sys.stdin.read(1)
        return c


    
if __name__ == '__main__':

    '''test1 hogeと出力されます'''
    b = "++++++++++++++++++++++++++++++++"
    b = b + b + b
    b += "++++++++."
    b += "+++++++."
    b += "--------."
    b += "--."
    program1 = b
    

    '''test2 hogeと出力されます'''
    b = "++++++++++[>++++++++++<-]>"
    b += "++++.+++++++.--------.--."
    program2 = b


    '''test3 足し算をして3が表示されます'''
    b = "+>++><<"
    b += ">[-<+>]<"
    b += "++++++++++++++++++++++++++++++++++++++++++++++++."
    program3 = b



    '''test4 足し算をして3が表示されます'''
    b = "+>++><<"
    b += "[->>>+<<<]"
    b += ">>>[-<+<<+>>>]<<"
    b += "[->>+<<]"
    b += ">>[-<+<+>>]<"
    b += "++++++++++++++++++++++++++++++++++++++++++++++++."
    program4 = b

    '''test5 かけ算を行っています 4 * 2を行い8が出力されます'''
    b =  "++++>++><<"
    b += "[-"
    b += "   >[->>+<<]"
    b += "   >>[-<+<+>>]"
    b += "   <<<"
    b += "]>>"
    b += "++++++++++++++++++++++++++++++++++++++++++++++++."
    program5 = b



    fuck = Brainfuck()

    fuck.readScript(program1).exe()
    print ""
    fuck.readScript(program2).exe()
    print ""
    fuck.readScript(program3).exe()
    print ""
    fuck.readScript(program4).exe()
    print ""
    fuck.readScript(program5).exe()
    print ""
    
