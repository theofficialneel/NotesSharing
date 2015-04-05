from app import db

class User(db.Model):
    rollNo = db.Column(db.Integer, primary_key=True)
    #nickname = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<User %r>' % (self.rollNo)


class Department(db.Model):
    department = db.Column(db.String(64), primary_key=True)

    def is_authenticated(self):
        # Return False if the user object is not allowed for some reason
        return True

    def is_active(self):
        return True  # Return False if they are banned

    def __repr__(self):
        return '<Department %r>' % (self.department)


class files(db.Model):
    __searchable__ = ['department','description','author','tags'] #array with all the database fields that will be in the searchable index
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(64), index=True)
    department = db.Column(db.String(64), index=True)
    semester = db.Column(db.Integer, index=True)
    author = db.Column(db.String(64) , index =True)
    tags = db.Column(db.String(64) , index= True) 
    description = db.Column(db.String(100) , index= True)
    downloads = db.Column(db.Integer , index = True)
    stars  = db.Column(db.Integer, index = True) 
    uploader = db.Column(db.String(64)  , index = True)
    def __repr__(self):
        return '<File {0}-> {1} >'.format(self.filename, self.department)
