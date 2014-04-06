from google.appengine.ext import db

class RescueReport(db.Model):
    names = db.StringProperty()
    location = db.StringProperty()
    situation = db.StringProperty()
    contactinfo = db.StringProperty()
    
class Tweet(db.Model):
    text = db.StringProperty()
    user = db.StringProperty
    
class HeatMapPins(db.Model):
    lat = db.FloatProperty()
    long = db.FloatProperty()
    
class ReliefOrg(db.Model):
    name = db.StringProperty()
    picurl = db.StringProperty()
    description = db.StringProperty()
    link = db.StringProperty()