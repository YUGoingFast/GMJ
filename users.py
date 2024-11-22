class user:
    def __init__(self, id, type, fname, sname, email, password):
        self.id = id
        self.type = type
        self.fname = fname
        self.sname = sname
        self.email = email
        self.password = password

class student(user):
    def __init__(self, id, fname, sname, email, password):
        super().__init__(id, 'student', fname, sname, email, password)