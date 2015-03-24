import json
import sys


#Used to convert given JSON file to django fixture json
#note does not init nextsemester available field
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: convertToFixture.py [INFILE] [OUTFILE]')
        sys.exit()
    filename = sys.argv[1]
    outfile_name = sys.argv[2]
    with open(filename) as data_file: 
        print("reading INFILE...")
        data = json.load(data_file)
        ndata = []
        print("parsing INFILE...")
        for coursedata in data:
            newcoursedata = {}
            newcoursedata['model']="course.Course"
            fieldsnode = {}
            fieldsnode['id']=coursedata['num']
            fieldsnode['title']=coursedata['name']
            fieldsnode['description']=coursedata['desc']
            fieldsnode['units']=coursedata['units']
            fieldsnode['corequirements']=coursedata['coreqs']
            fieldsnode['prerequirements']=coursedata['prereqs']
            fieldsnode['fallsemester']='F' in coursedata['semester']
            fieldsnode['springsemester']='S' in coursedata['semester']
            fieldsnode['summersemester']='U' in coursedata['semester']
            newcoursedata['fields']=fieldsnode
            ndata.append(coursedata)
        print("Writing to OUTFILE...")
        with open(outfile_name, 'w') as outfile:
            json.dump(ndata, outfile)
            print("Done.")
    
  


