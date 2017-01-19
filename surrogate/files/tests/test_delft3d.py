from surrogate.files.delft3d import Delft3D

filename = '../../../examples/files/s01-algaebloom_original.map'
d3d = Delft3D(fileName=filename)
moname,varlist,maptime,nseg,nvar,ntime = d3d.readWaqMapInit()

# iseg=0
# ivar=0
# itime=0

# iseg=4011
iseg=10011
ivar=79
itime=3

print 'test_delft3d'

print 'data size: [nseg='+str(nseg)+',nvar='+str(nvar)+',ntime='+str(ntime)+']'

# 79	GREENS
# for i in range(len(varlist)):
#     print str(i)+'\t'+varlist[i]
#
# for i in range(len(maptime)):
#     print str(i)+'\t'+str(maptime[i])

dataOffset = d3d.readWaqMapDataAtOffset(iseg=iseg,ivar=ivar,itime=itime)
print dataOffset

dataTime = d3d.readWaqMapDataAtTime(itime=itime)
print dataTime[iseg][ivar][0]

dataSeg = d3d.readWaqMapDataAtSegment(iseg=iseg)
# print dataSeg[0][ivar][:]
print dataSeg[0][ivar][itime]

dataVar = d3d.readWaqMapDataAtVariable(ivar=ivar)
# print dataVar[iseg][0][:]
print dataVar[iseg][0][itime]

print 'end'