class board():
    def __init__(self) -> None:
        self.map = [['n' for i in range(3)] for j in range(3)]
        self.ai_tracker = list(tuple())
        self.human_tracker = list(tuple())
    def brd_display(self):
        for i in self.map:
            for j in i:
                print(j,end='\t')
            print('\n')
    def game_loop(self):
        move_ct = 0
        b_vacant = 9
        while not(self.ai_wins() or self.human_wins()) and b_vacant:
            if move_ct%2==0:
                y,x = eval(input("1st player>"))
                self.map[y-1][x-1] = '0'
                self.human_tracker.append((y,x))
                self.brd_display()
            else:
                print("ai_master>")
                y,x = self.ai(b_vacant)
                self.ai_tracker.append(y,x)
                self.map[y-1][x-1] = 'x'
                self.brd_display()
            move_ct+=1
            b_vacant-=1
        if self.ai_wins():
            print("ai wins")
        elif self.human_wins():
            print("human wins")
        else:
            print("draw")
    def ai_wins(self)->bool:
        #ai ->> 'x'
        x_lst = {i:0 for i in range(1,4)}
        y_lst = {i:0 for i in range(1,4)}
        if ((1,1) in self.ai_tracker and (2,2) in self.ai_tracker and (3,3) in self.ai_tracker)\
             or ((1,3) in self.ai_tracker and (2,2) in self.ai_tracker and (3,1) in self.ai_tracker):
             return True
        for y,x in self.ai_tracker:
            x_lst[x]+=1
            y_lst[y]+=1
        if [1 for i in x_lst.values() if i == 3]:
            return True
        if [1 for i in y_lst.values() if i == 3]:
            return True
    def human_wins(self)->bool:
        #human ->> '0'
        x_lst = {i:0 for i in range(1,4)}
        y_lst = {i:0 for i in range(1,4)}
        if ((1,1) in self.human_tracker and (2,2) in self.human_tracker and (3,3) in self.human_tracker)\
             or ((1,3) in self.human_tracker and (2,2) in self.human_tracker and (3,1) in self.human_tracker):
             return True
        for y,x in self.human_tracker:
            x_lst[x]+=1
            y_lst[y]+=1
        if [1 for i in x_lst.values() if i == 3]:
            return True
        if [1 for i in y_lst.values() if i == 3]:
            return True
    def ai(self,b_vacant):
        mx_prb_tup = tuple()
        mx_prob = 0
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == 'n':
                    map_proto = [[self.map[y][x] for x in range(len(self.map[0]))] for y in range(len(self.map))]
                    tracker_proto = list(self.ai_tracker)
                    win_s = 0
                    match_s = 0
                    self.map[y][x] = 'x'
                    map_type = [[self.map[y][x] for x in range(len(self.map[0]))] for y in range(len(self.map))]
                    self.ai_tracker.append((y+1,x+1))
                    tracker_type =  list(self.ai_tracker)
                    x_movs = 0
                    if b_vacant%2==0:x_movs=b_vacant//2
                    else:x_movs=(b_vacant+1)//2
                    lst = ['x']*x_movs+['0']*(b_vacant-x_movs)
                    l = self.permutator(lst)
                    lst = []
                    for i in l:
                        if not(i in lst):
                            lst.append(i)
                    for iter in l:
                        ct = 0
                        for y in range(len(self.map)):
                            for x in range(len(self.map[y])):
                                if self.map[y][x] == 'n':
                                    self.map[y][x] = iter[ct]
                                    if iter[ct] == 'x':
                                        self.ai_tracker.append((y+1,x+1))
                                    ct+=1
                        if self.ai_wins():
                            win_s+=1
                        match_s+=1
                        self.map = map_type
                        self.ai_tracker = tracker_type
                    probs = win_s/match_s
                    if probs > mx_prob:
                        mx_prb_tup = (y,x)
                        mx_prob = probs
                    self.map = map_proto
                    self.ai_tracker = tracker_proto
        return mx_prb_tup
    def permutator(self,lst):  
        if len(lst) == 0:
            return []
        if len(lst) == 1:
            return [lst]
        l = [] 
        for i in range(len(lst)):
            m = lst[i]
            remLst = lst[:i] + lst[i+1:]
            for p in self.permutator(remLst):
                l.append([m] + p)
        return l 

#main()
map1 = board()
map1.game_loop()

