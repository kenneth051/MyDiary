class Diary:
    entries=[]
    def __init__(self,_id,title,date,time,body):
        self.id=_id
        self.title=title
        self.time=time
        self.date=date
        self.body=body
        self.updated=time
    def create(self):
        entry=Diary(self.id,self.title,self.date,self.time,self.body)
        lst={}
        lst["id"]=entry.id
        lst["title"]=entry.title
        lst["date"]=entry.date
        lst["time"]=entry.time
        lst["body"]=entry.body
        lst["updated"]=entry.updated
        Diary.entries.append(lst)
        return lst

    @classmethod    
    def all(self):
        return Diary.entries

    @classmethod    
    def singleEntry(cls,entryId):
        result="invalid Id,Try again"
        for info in Diary.entries:
            if info['id'] == entryId:
                result =info
        return result

    @classmethod    
    def update(self,entryId,data):
        result="invalid Id, cannot update"
        for info in Diary.entries:
            if info['id'] == entryId:       
                info["title"]=data["title"]
                info["body"]=data["body"]
                result="update successful"
        return result    
