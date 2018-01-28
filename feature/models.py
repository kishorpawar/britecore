from feature import db

# base model to be inherited by other models
class Base(db.Modle):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key = True)
    created_on = db.Column(db.DateTime, default = db.func.current_timestamp())
    updated_on = db.Column(db.DateTime, default = db.func.current_timestamp(),
                                        onupdate = db.func.current_timestamp())


# feature model
class Feature(Base):
    __tablenaem__ = 'feature'
   
    title = db.Column(db.String(200))
    description = db.Column(db.String(2000))
    client = db.Column(db.String(20))
    priority = db.Column(db.SmallInteger)
    targate_date = db.Column(db.DateTime)
    product_area = db.Column(db.String(20))
    __table_args__ = (UniqueConstraint('client', 'priority', name='_uniq_client_priority'))
    
    def __repr__(self):
       return self.title 


