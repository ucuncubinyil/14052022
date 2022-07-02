from  abc import ABC , abstractmethod


class Base(ABC):
	
	def __init__(self):
		self.id = ""
		self.name = ""
		self.add_date = ""
		self.update_date = ""
		self.delete_date = ""
	
	@abstractmethod
	def save( self ):
		pass
	
	@abstractmethod
	def list_all( self ):
		pass
	
	@abstractmethod
	def update( self ):
		pass
	
	@abstractmethod
	def delete( self ):
		pass
	