import sys
import random

class Mixer(object):
    
    def __init__(self, title, date, username, banner, filename):
        
        self.title = title
        self.date = date
        self.author = username
        self.banner = banner
        self.filename = filename
        self.tags = []
    
    def make_brick(self):
        #Main run function
        print("Making a brick")
        cement = self.cement()
        concrete = self.mixer(cement)
        self.mould(concrete)
        print(Mixer.special_brick_effects())


        
    def cement(self):
        #Usually I copy and paste the newsletter into a txt document (self.filename)
        #Reads self.filename
        print("Loading up the cement...")
        raw = self.read_file()
        return raw
        
    
    def mixer(self, raw):
        #mixes and matches and formats everything nicely
        print("Putting the cement in the mixer...")
        output = []
        tnext = 1
        last_was_tldr = False
        for line in raw:
            if tnext == 2:
                self.tags.append("  - "+line)
                line = "## "+line
                output.append(line)
                tnext = 0
                continue
            if line.count("-") > 3:
                line = ""
                tnext +=1
                output.append(line)
                continue
            if line.count("- ") == 1:
                last_was_tldr = True
            if last_was_tldr and line.count("- ") != 1:
                output.append("\n<!-- more -->\n\n\n")
                last_was_tldr = False
            else:
                output.append(line)
        return output
        
    
    def mould(self, output, file_out="result.md"):
        #Outputs the mix as MD
        print("Putting the concrete in the mould...")
        with open(file_out, "w") as file:
            file.write("---\n")
            file.write("title: '"+self.title+"'\n")
            file.write("date: '"+self.date+"'\n")
            file.write("banner: "+self.banner+"\n")
            file.write("author: "+self.author+"\n")
            file.write("tags:"+"\n"+"".join(self.tags))
            file.write("---\n")
            file.write("".join(output))
        
    def read_file(self):
        #Simple readfile
        with open(self.filename, "r") as fname:
            return fname.readlines()
    
    @staticmethod
    def special_brick_effects():
        a = ["Wow is that Brick yours?", "Look at the brick, ain't it purdyy!", "Who's a nice little brick? You are!", 
        "Woah making bricks has never been this fun!", "Imagine how faster this would be if this automated with the newsletter!", 
        "I wonder what would happen if we added some herbs?", "WHAT ARE THOSSEEEEEEE? THEY are my bricks", "...And they were bricks? MAH GOD THEY WERE BRICKS!" ]
        return random.choice(a)


def main():
    title = input("Title Please: ")
    date = input("Date Please: ")
    author = input("Username Please: ")
    banner = input("Banner Please: ")
    filename = input("Filename Please: ")
    print("\n\n\n")
    brick = Mixer(title, date, author, banner, filename)
    brick.make_brick()

if __name__ == '__main__':
    main()