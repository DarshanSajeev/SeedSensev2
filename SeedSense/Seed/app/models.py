from app import db
from flask_login import UserMixin


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(15), index=True, unique=True)
    Password = db.Column(db.String(30))

    #User email too email incaase of emergancy
    Email = db.Column(db.String(50))

    #List of seeds used by the user
    SeedList = db.Column(db.String)

def __repr__(self):
    return (
        f"Variable(id={self.id}, "
        f"Username={self.Username}, "
        f"Password={self.Password}, "
        f"Email={self.Email}, "
        f"SeedList={self.SeedList})"
    )




class Seeds(db.Model):
    #Primary Id of the seeds
    SeedId = db.Column(db.Integer, primary_key=True)

    #Name of the seed
    SeedName = db.Column(db.String(30))

    #UserId of the user that owns the grid
    OwnerId = db.Column(db.Integer, db.ForeignKey('user.id')) 

    #Min/Max temp for seed in degrees celcius
    MinTemp = db.Column(db.Float)
    MaxTemp = db.Column(db.Float)

    #Min/Max water for seed in mm
    MinWater = db.Column(db.Float)
    MaxWater = db.Column(db.Float)

    #Min/Max sunlight duration  for seed in hours
    MinSun = db.Column(db.Float)
    MaxSun = db.Column(db.Float)

    #Time required for germanation in days
    GermeTime = db.Column(db.Integer)

    #Number of times to water per day
    WaterFreq = db.Column(db.Integer)

    #Minerals that seed takes/gives from/to the field
    MineralGive = db.Column(db.String(30))
    MineralTake = db.Column(db.String(30))


def __repr__(self):
    return (f"Seed(SeedId={self.SeedId}, "
            f"SeedName='{self.SeedName}', "
            f"OwnerId={self.OwnerId}, "
            f"MinTemp={self.MinTemp}, MaxTemp={self.MaxTemp}, "
            f"MinWater={self.MinWater}, MaxWater={self.MaxWater}, "
            f"MinSun={self.MinSun}, MaxSun={self.MaxSun}, "
            f"GermeTime={self.GermeTime}, "
            f"WaterFreq={self.WaterFreq}, "
            f"MineralGive='{self.MineralGive}', "
            f"MineralTake='{self.MineralTake}')")

    


class Fields(db.Model):
    #Primary Id of the Grid
    FieldId = db.Column(db.Integer, primary_key=True)

    #UserId of the user that owns the grid
    OwnerId = db.Column(db.Integer, db.ForeignKey('user.id'))

    #Name Of The Grid Set By The User
    FieldName = db.Column(db.String(30))

    #Num of row/columns of the grid
    NumRow = db.Column(db.Integer)
    NumColumn = db.Column(db.Integer)  

    #Matrix that stores how seeds are planted across a grid
    SeedMatrix = db.Column(db.String)

    #Matrix that stores the lacking minerals within a subgrid
    MineralsMatrix = db.Column(db.String)

    def __repr__(self):
        return (f"Fields(FieldId={self.FieldId}, "
                f"OwnerId={self.OwnerId}, "
                f"FieldName='{self.FieldName}', "
                f"NumRow={self.NumRow}, NumColumn={self.NumColumn}, "
                f"SeedMatrix='{self.SeedMatrix}', "
                f"MineralsMatrix='{self.MineralsMatrix}')")


