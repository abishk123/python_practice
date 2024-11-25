class Player:
    def __init__(self,pn,pa,pc,pm,pr,pw):
        self.p_name=pn
        self.p_age=pa
        self.p_country=pc
        self.p_matches=pm
        self.p_runs=pr
        self.p_wickets=pw
'''
    def player_details(self):
        print(f'Name of the Player is {self.p_name}')
        print(f'Age of the Player is {self.p_age}')
        print(f'Country of the Player is {self.p_country}')
        print(f'Matches Played by the Player is {self.p_matches}')
        print(f'Runs Scored by the Player is {self.p_runs}')
        print(f'Wickets Taken by Player is {self.p_wickets}')
'''
class Team:
    def __init__(self):
        self.lop=[]
        self.no_of_players=int(input('no. of players: '))
        for o in range(self.no_of_players):
            n=input('name:')
            a=int(input('age:'))
            c=input('country:')
            m=int(input('matches'))
            r=int(input('runs:'))
            w=int(input('wickets:'))
            po=Player(n,a,c,m,r,w)
            self.lop.append(po)

    def max_runs(self):
        mrpo=self.lop[0]
        for po in self.lop:
            if mrpo.p_runs < po.p_runs:
                mrpo=po
        return mrpo.p_name

            
    def max_wickets(self):
        mwpo=self.lop[0]
        for po in self.lop:
            if mwpo.p_wickets<po.p_wickets:
                mwpo=po
        return mwpo.p_name



india=Team()
print(f'The max wickets took by {india.max_wickets()}')
print(f'The max runs scored by {india.max_runs()}')



        

