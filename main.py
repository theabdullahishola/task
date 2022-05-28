class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,tracks, age,score):
        self.name=str(name)
        self.age=int(age)
        self.tracks=tracks
        self.score=float(score)
    def change_name(self,new_name):
        self.name=new_name
        print("Student-info(name=%s, age=%s, tracks=%s,score=%s)"%(self.name,self.age,self.tracks,self.score))
    def change_age(self,new_age):
        self.age=new_age
        print("Student-info(name=%s, age=%s, tracks=%s,score=%s)"%(self.name,self.age,self.tracks,self.score))
    def add_track(self,new_track):
        self.new_track=self.tracks.append(new_track)
        print("Student-info(name=%s, age=%s, tracks=%s,score=%s)"%(self.name,self.age,self.tracks,self.score))
    def get_score(self):
        print(self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

