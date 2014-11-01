__author__ = '22kaj22'
#To change this template use Tools | Templates.
#
# to convert NASA WRS-2_bound_world.kml to csv of points
# for further processing

def kml2csv(kmlFile, csvFile):
    """kml2csv(str,str)->int"""
    
    from os import path
    
    if not path.isfile(kmlFile):
        print 'file not found: ', kmlFile
        return -1
    
    if path.isfile(csvFile):
        strOverwrite = 'file, ' + csvFile + ', already exists. overwrite (y/n)? '
        
        newCsv=''
        
        while newCsv != 'y':
            newCsv = raw_input(strOverwrite)
            if newCsv == 'n': return -1
    
    try:
        fKml = open(kmlFile,'r')
    except (IOError):
        print 'cannot open file ',kmlFile
        return -1
    
    try:
        fCsv = open(csvFile,'w')
    except (IOError):
        print 'cannot open file ',csvFile
        return -1
     
    wrsPointsList=[]
    wrsPoint=[]
    i=0
     
    for line in fKml:
        if 'PATH' in line: 
            if len(wrsPoint)>0:
                wrsPointsList.append(wrsPoint)
                wrsPoint=[]
            i=1
        elif 'ROW' in line: i=1
        elif 'CTR LAT' in line: i=1
        elif 'CTR LON' in line: i=1
        elif 'LAT UL' in line: i=1
        elif 'LON UL' in line: i=1
        elif 'LAT UR' in line: i=1
        elif 'LON UR' in line: i=1
        elif 'LAT LL' in line: i=1
        elif 'LON LL' in line: i=1
        elif 'LAT LR' in line: i=1
        elif 'LON LR' in line: i=1

        if i==1:
            valStart = line.find('</strong>: ')
            valEnd = line.find('<br>')
            wrsPoint.append(line[valStart+11:valEnd])
            i=0
    
    if len(wrsPoint)>0: wrsPointsList.append(wrsPoint) #to capture the last read entry
   
    for i in wrsPointsList: #convert PATH & ROW to ints
        writeString=''
        
        for j in range(len(i)):
            if 0 <= j <=1: i[j]=i[j].split('.')[0]
            writeString += i[j] + ','
            
        fCsv.write(writeString[0:-1]+'\n')
        
    return 1

def main():
    
    kmlFile='./assets/WRS-2_bound_world.kml'
    csvFile='./assets/WRS-2_bound_world.csv'
    
    kml2csv(kmlFile,csvFile)
    
    return None

if __name__ == '__main__': main()
