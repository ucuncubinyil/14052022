from  Base import Base

 # CRUD ( Create Read Update Delete)

class Product(Base):
	
	def __init__(self):
		self.price = ""
		self.stoc = ""
		
	def save( self ):
		print(self.id)
	
	def delete( self ):
		pass
	
	def update( self ):
		pass
	
	def list_all( self ):
		pass