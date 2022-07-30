import psycopg2
from Config import config


def connect( ):
	conn = None
	try:
		params = config( )
		print( "Veritabanına bağlanıyorum" )
		
		conn = psycopg2.connect( **params )
		cur = conn.cursor( )
		
		cur.execute( "SELECT version()" )
		
		db_version = cur.fetchone( )
		print( f"PostgreSQL sürümü {db_version}" )
		conn.close( )
	except (Exception, psycopg2.DataError) as error:
		print( error )


# Ekleme İşlemi
def insert_account( user_name, password, email, birth_year ):
	
	sql = """
			INSERT INTO accounts(user_name,password,email, created_on, birth_year)
			VALUES (%s, %s, %s,current_timestamp, %s) RETURNING  id
	"""
	
	conn = None
	id = None
	
	try:
		params = config( )
		print( "Veritabanına bağlanıyorum" )
		conn = psycopg2.connect( **params )
		cur = conn.cursor( )
		cur.execute( sql, (user_name, password, email, birth_year) )
		id = cur.fetchone( )[ 0 ]
		
		print( "Kullanıcı eklendi idsi : ", id )
		conn.commit( )
		conn.close( )
	except (Exception, psycopg2.DatabaseError) as error:
		print( error )
	
	finally:
		if conn is not None:
			conn.close( )
			print( "Veritabanı bağlantısı kapatıldı" )


def list_account( ):
	
	conn = None
	
	try:
		params = config( )
		print( "Veritabanına bağlanıyorum" )
		conn = psycopg2.connect( **params )
		cur = conn.cursor( )
		cur.execute( "Select * from accounts" )
		account_list = cur.fetchone( )
		conn.commit( )
		conn.close( )
		print( type( account_list ) )
		print( list( account_list ) )
	
	except (Exception, psycopg2.DatabaseError) as error:
		print( error )
	
	finally:
		if conn is not None:
			conn.close( )
			print( "Veritabanı bağlantısı kapatıldı" )


def insert_account_list( account_list ):
	
	sql = """
				INSERT INTO accounts(user_name,password,email, created_on, birth_year)
				VALUES (%s, %s, %s,current_timestamp, %s)
		"""
	
	conn = None
	user_id = None
	try:
		params = config( )
		print( "Veritabanına bağlanıyorum" )
		conn = psycopg2.connect( **params )
		cursor = conn.cursor( )
		
		#coklu veri girişinde kullanılır
		cursor.executemany( sql, account_list )
		
		conn.commit( )
		conn.close( )
	except (Exception, psycopg2.DatabaseError) as error:
		print( error )
	
	finally:
		if conn is not None:
			conn.close( )
			print( "Bağlantı koparıldı" )


# insert_account("hakan_vural", "Abc123", "hakan@hakan.com", "2003")
# list_account()
kullanici_listesi = [
		("murat_kaya", "aaa", "murat@kayacom","1992" ),
		("alicandd", "aaa", "muarat@kayacom","1991")
		
		]
insert_account_list( kullanici_listesi )

# conn = psycopg2.connect(
# 		database="gdsjcdat",
# 		host="manny.db.elephantsql.com",
# 		password="Knf64UelmtN6LfsQJCbFZAc_z3PmyGeW",
# 		user="gdsjcdat",
# 		port="5432"
# 		)
#
# cursor =  conn.cursor()
# cursor.execute("Select  * FROM accounts")
# print(cursor.fetchall())
