#

"""
Delft3D classes for all Delft3D generated result files.
naming system: [method:read,write][software:Flow,Waq][file:Map,His]
"""

import os

import struct

class Delft3D(object):
    """Delft3D class

    :param fileName: file name
    """
    def __init__(self, fileName):
        self.fileName = fileName
        self.fileSize = os.path.getsize(fileName)

        self.nseg = -1
        self.nvar = -1
        self.ntime = -1
        self.varlist = []
        self.timlist = []
        self.headOffset = -1
        self.blockOffset = -1

        self.iseg = 0
        self.ivar = 0
        self.itime = [-1,-1]

    def readWaqMapInit(self):
        """readWaqMap
        read Delft3D Water quality model map file.
        open('b') is important -> binary
        file.read(1), 8 bits is 1 byte.

        Map file structure: [row,column]::
            character(len=40) : moname(4) [4,40]
            integer : self.nvar, self.nseg [1,4],[1,4]
            ntime = int(real(fileSize -4*40 -2*4 -self.nvar*20) /real(4+4*self.nvar*self.nseg))

            character(len=20) : self.varlist(self.nvar) [self.nvar,20]

            valmap(ntime,self.nseg,nresult)
            tempValMap(self.nvar, self.nseg) [self.nvar, self.nseg, 4]
            do k=1,ntime
                read (mapfID) maptime [1,4]
                read (mapfID) ((tempValMap(i,j),i=1,self.nvar),j=1,self.nseg)
                do j=1,nresult
                    valmap(k,:,j) = tempValMap(iseg(j),1:self.nseg)
                end do
            end do

        :return: fileContent
        """

        moname = []

        with open(self.fileName, mode='rb') as file:
            for i in range(0,4):
                moname.append(file.read(40).strip())
            self.nvar = struct.unpack('i',file.read(4))[0]
            self.nseg = struct.unpack('i',file.read(4))[0]
            self.ntime = int((self.fileSize -4*40 -2*4 -self.nvar*20)/(4+4*self.nvar*self.nseg))
            self.headOffset = 4*40 + 2*4 + self.nvar*20
            self.blockOffset = self.nvar*self.nseg*4

            for i in range(0,self.nvar):
                self.varlist.append(file.read(20).strip())
            # print self.varlist

            # data = [[[None for k in range(self.ntime)] for j in range(self.nvar)] for i in range(self.nseg)]
            for k in range(0,self.ntime):
                self.timlist.append(struct.unpack('i',file.read(4))[0])
                # print 'self.timlist:\t'+str(self.timlist[k])

                file.seek(self.nseg*self.nvar*4,1)
                # for i in range(0,self.nseg):
                #     for j in range(0,self.nvar):
                #         data[i][j][k] = struct.unpack('f',file.read(4))[0]

        rtn = []
        return moname,\
               self.varlist,\
               self.timlist,\
               self.nseg,\
               self.nvar,\
               self.ntime

    def readWaqMapDataAtOffset(self,iseg=0,ivar=0,itime=0):
        """

        :param iseg:
        :param ivar:
        :param itime:
        :return:
        """
        self.iseg = iseg
        self.ivar = ivar
        self.itime[0] = itime
        with open(self.fileName, mode='rb') as file:
            file.seek(self.headOffset,0)

            file.seek((self.blockOffset+4)*itime,1)
            self.itime[1] = struct.unpack('i',file.read(4))[0]
            file.seek((iseg*self.nvar+ivar)*4,1)
            data = struct.unpack('f',file.read(4))[0]

        return data

    def readWaqMapDataAtTime(self,itime=0):
        """

        :param itime:
        :return:
        """
        self.iseg = -1
        self.ivar = -1
        self.itime[0] = itime
        # data = [[ None for j in range(self.nvar)] for i in range(self.nseg)]
        data = [[[None for k in range(1)] for j in range(self.nvar)] for i in range(self.nseg)]
        with open(self.fileName, mode='rb') as file:
            file.seek(self.headOffset,0)

            file.seek((self.blockOffset+4)*itime,1)
            self.itime[1] = struct.unpack('i',file.read(4))[0]
            for i in range(0,self.nseg):
                for j in range(0,self.nvar):
                    data[i][j][0] = struct.unpack('f',file.read(4))[0]

        return data

    def readWaqMapDataAtSegment(self,iseg=0):
        """

        :param iseg:
        :return:
        """
        self.iseg = iseg
        self.ivar = -1
        self.itime = [-1,-1]
        # data = [[ None for j in range(self.ntime)] for i in range(self.nvar)]
        data = [[[None for k in range(self.ntime)] for j in range(self.nvar)] for i in range(1)]
        with open(self.fileName, mode='rb') as file:
            file.seek(self.headOffset,0)

            # file.seek((self.blockOffset+4)*itime,1)
            for k in range(self.ntime):
                file.seek(4,1)
                file.seek(iseg*self.nvar*4,1)
                for j in range(self.nvar):
                    data[0][j][k] = struct.unpack('f',file.read(4))[0]
                file.seek((self.nseg-iseg-1)*self.nvar*4,1)

        return data

    def readWaqMapDataAtVariable(self,ivar=0):
        """

        :param ivar:
        :return:
        """
        self.iseg = -1
        self.ivar = ivar
        self.itime = [-1,-1]
        # data = [[ None for j in range(self.ntime)] for i in range(self.nseg)]
        data = [[[None for k in range(self.ntime)] for j in range(1)] for i in range(self.nseg)]
        with open(self.fileName, mode='rb') as file:
            file.seek(self.headOffset,0)

            # file.seek((self.blockOffset+4)*itime,1)
            for k in range(self.ntime):
                file.seek(4,1)
                for i in range(self.nseg):
                    file.seek(ivar*4,1)
                    data[i][0][k] = struct.unpack('f',file.read(4))[0]
                    file.seek((self.nvar-ivar-1)*4,1)

        return data

    def readWaqMapDataAtVariableTime(self,ivar=0,itime=0):
        """

        :param ivar:
        :param itime:
        :return:
        """
        self.iseg = -1
        self.ivar = ivar
        self.itime[0] = itime
        # data = [[ None for j in range(self.ntime)] for i in range(self.nseg)]
        data = [[None for j in range(1)] for i in range(self.nseg)]
        with open(self.fileName, mode='rb') as file:
            file.seek(self.headOffset,0)

            file.seek((self.blockOffset+4)*itime,1)
            self.itime[1] = struct.unpack('i',file.read(4))[0]
            for i in range(self.nseg):
                file.seek(ivar*4,1)
                data[i][0] = struct.unpack('f',file.read(4))[0]
                file.seek((self.nvar-ivar-1)*4,1)

        return data
