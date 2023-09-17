class Post():
    def __init__(self, title, summary):
        self.title = title
        self.summary = summary
        self.upvotes = 0
        self.downvotes = 0
        
        self.upvoters = []
        self.downvoters = []
        
    #TODO Refactor this shit its gross to look at
    def downvote(self, id):
        if(self.downvoters.count(id) < 1):
            self.downvotes += 1
            self.downvoters.append(id)
            if(self.upvoters.count(id) > 0): 
                self.upvotes -= 1
                self.upvoters.remove(id)
            return 200
        else: return 423
        
    def upvote(self, id):
        if(self.upvoters.count(id) < 1):
            self.upvotes += 1
            self.upvoters.append(id)
            if(self.downvoters.count(id) > 0): 
                self.downvotes -= 1
                self.downvoters.remove(id)
            return 200
        else: return 423
        
    # Class operator overrides
    def __eq__(self, obj):
        return self.title == obj
    def __en__(self, obj):
        return self.title != obj
    