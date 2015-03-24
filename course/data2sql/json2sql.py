import mysql.connector
from mysql.connector import errorcode
import json
import sys


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def chooseDatabase(cnx,cursor,DB_NAME):
  try:
    cnx.database = DB_NAME    
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
      create_database(cursor)
      cnx.database = DB_NAME
    else:
      print(err)
      exit(1)

def createTable(cnx,cursor):
  TABLES = {}
  TABLES['courses'] = (
    "CREATE TABLE `courses` ("
    "  `courseid` int(5) NOT NULL,"
    "  `name` varchar(75) NOT NULL,"
    "  `desc` varchar(800) NOT NULL,"
    "  `units` int(3) NOT NULL,"
    "  `semester` varchar(5) NOT NULL,"
    "  `coreqs` varchar(100) NOT NULL,"
    "  `prereqs` varchar(100) NOT NULL,"
    "  PRIMARY KEY (`courseid`)"
    ") ENGINE=InnoDB")
  for name, ddl in TABLES.iteritems():
    try:
      print("Creating table {}: ".format(name), end='')
      cursor.execute(ddl)
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("already exists.")
      else:
        print(err.msg)
    else:
      print("Table(s) Created")

def convertData(jsonCourseData):
  jcd=jsonCourseData
  def add(x,y): return x+y
  semesterC=reduce(add, jcd['semester'])
  cdata=(jcd['num'],jcd['name'],jcd['desc'],jcd['units'],semesterC,
         jcd['coreqs'],jcd['prereqs'])
  return cdata

def tranferData(filename,cnx,cursor):
  with open(filename) as data_file: 
    data = json.load(data_file)
    add_course = ("INSERT INTO courses "
               "(courseid, name, desc, units, semester, coreqs, prereqs) "
               "VALUES (%d, %s, %s, %d, %s, %s, %s)")
    for coursedata in data:
      data_course = convertData(coursedata)
      # Insert new course
      cursor.execute(add_course, data_course)
    





#Uses transfer JSON file to MySQL database
#need to change config section 
if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('Usage: parse_descs.py [INFILE]')
    sys.exit()
  jsonfilename = sys.argv[1]
  config = {
    'user': 'scott',
    'password': 'tiger',
    'host': '127.0.0.1',
    'database': 'gradpath',
    'raise_on_warnings': True,
  }
  try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    chooseDatabase(cnx,cursor,'gradpath')
    createTable(cnx,cursor)
    tranferData(filename,cnx,cursor)
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    cursor.close()
    cnx.close()


