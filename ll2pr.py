__author__ = '22kaj22'
#To change this template use Tools | Templates.
#
#to convert lon/lat to NASA WRS path/row

def ll2Pr(lat,lon,wrsCsvFile,day=1,fast=1):
    """ll2Pr(float,float,str,[bool],[bool])->tuple of ints"""
    
    if -80.85 > lat > 80.783333:
        print 'latitude must be between -80.85 and 80.78'
        return None
    
    
    ## read in CSV file
    try:
        csvFile=open(wrsCsvFile,'r')
    except (IOError):
        print 'cannot open file: ',wrsCsvFile
        return None
    
    wrsPoints = []
    
    for line in csvFile:
        values=line.split(',')
        
        for i in range(len(values)):
            if 0 <= i <= 1: values[i]=int(values[i])
            else: values[i]=float(values[i])
        
        if day and values[1]< 123: wrsPoints.append(values) #only list daylight rows
        elif not day: wrsPoints.append(values) #all rows
    
    wrsPath=0
    wrsRow=0
    minDist=10000.
    
    for point in wrsPoints:
        
        distance = abs(point[3]-lon) + abs(point[2]-lat) #calculate distance from lat/lon to centre path/row

        if distance<minDist:
            wrsPath=point[0]
            wrsRow=point[1]
            minDist=distance
 
    return (wrsPath,wrsRow)

def main():
    
    wrsCsv='./assets/WRS-2_bound_world.csv'
    
    print ll2Pr(37.7749,-122.4194,wrsCsv)
    
    return None

if __name__ == '__main__': main()
    
    
    
