import json
import sys
from datetime import datetime 

#Used to convert given JSON files to django course/dept fixture json
#note does not init nextsemester available field
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: convertToFixture.py [INFILE course] '
              '[INFILE department] [OUTFILE]')
        sys.exit()
    filename = sys.argv[1]
    filenameD = sys.argv[2]
    outfile_name = sys.argv[3]
    with open(filenameD) as data_fileD: 
        ndata = []
        print("reading INFILE dept...")
        datad = json.load(data_fileD)
        print("parsing INFILE dept...")
        for deptdata in datad:
            newdeptdata={}
            newdeptdata['model']="course.Department"
            fieldsnode = {}
            fieldsnode['id']=deptdata['dept_id']
            fieldsnode['title']=deptdata['dept_name']
            fieldsnode['created_at']=str(datetime.now())
            fieldsnode['updated_at']=str(datetime.now())
            newdeptdata['fields']=fieldsnode
            ndata.append(newdeptdata)
        with open(filename) as data_file: 
            print("reading INFILE course...")
            data = json.load(data_file)
            print("parsing INFILE course...")
            for coursedata in data:
                newcoursedata = {}
                newcoursedata['model']="course.Course"
                fieldsnode = {}
                fieldsnode['id']=coursedata['num']
                fieldsnode['department']=coursedata['num']/1000
                fieldsnode['title']=coursedata['name']
                fieldsnode['description']=coursedata['desc']
                fieldsnode['units']=coursedata['units']
                fieldsnode['corequirements']=coursedata['coreqs']
                fieldsnode['prerequirements']=coursedata['prereqs']
                fieldsnode['fallsemester']='F' in coursedata['semester']
                fieldsnode['springsemester']='S' in coursedata['semester']
                fieldsnode['summersemester']='U' in coursedata['semester']
                fieldsnode['created_at']=str(datetime.now())
                fieldsnode['updated_at']=str(datetime.now())
                newcoursedata['fields']=fieldsnode
                ndata.append(newcoursedata)
            
            print("Writing to OUTFILE...")
            with open(outfile_name, 'w') as outfile:
                 json.dump(ndata, outfile)
                 print("Done.")
    
  


