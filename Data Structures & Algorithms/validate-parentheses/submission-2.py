class Solution:
    def isValid(self, s: str) -> bool:
        # Are those the only options available?? Those 3 brackets
        #Or is there another way it can come like ^ or <>. What 
        #Are the other ways it can come. 
        #

        #first I put in each in the array, 
        #If it comes out to be {), }, ]} and there is one {{,(,[}
        #Then I return pop the {{,(,[} out. 
        # Data Structure. 
        # It would be an 
        # open[{,(,[] close[), }, ]]
        # characters[[(]
        # for i in str:
        #       if character not empgy
            #         if characer.length-1 is '{' and i == '}'
            #             pop.
                    #   else:
                    #     push(i)
            #         if character.length-1 is '(' and i == ')'
            #             pop
                    #   else:
                    #       push(i)
            #         if character.length-1 is '[' and i == ']'
            #             pop
                    #    else:
                    #       push(i)
                
        #        else: 
        #             push(i)
                
        #    if the character is empty:
        #        return true
        #     else:
        #         return False
        #     "[(])"
        #     characters.push(i)
        #     if i == 
        character = []
        for i in s:
            if character:
                print(s[len(character)-1])
                if character[len(character)-1] == '{' and i == '}':
                    character.pop()
                elif character[len(character)-1] == '(' and i == ')':
                    character.pop()
                elif character[len(character)-1] == '[' and i == ']':
                    character.pop()
                else:
                    character.append(i)
            else:
                character.append(i)
        print(character)
        if character:
            return False
        else:
            return True


        