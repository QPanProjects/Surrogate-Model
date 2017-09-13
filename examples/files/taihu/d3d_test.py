#!/usr/bin/python

# MIT License
#
# Copyright (c) 2016 Daily Actie
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Author: Quan Pan <quanpan302@hotmail.com>
# License: MIT License
# Create: 2016-12-02

# 0 --py:Success::
# 1 --py:Warning::
# 2 --py:Error::
# --py:Start\t['+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+']::
# --py:End\t['+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+']::
# --py:Test::


import os, sys, getopt, datetime


def loop_rec(y, number):
    if (number >= 1):
        loop_rec( y+1, number - 1 )
        for i in range(y):
            print str(i)+' '
        print('')
    else:
        return

def meshgridMD(group=[], grids=[]):
    """

    :param argv:
    :return:
    """

    # irow = 0
    # for ii in grids[0]:
    #     for ij in grids[1]:
    #         variable = [-9999 for x in range(Ndim)]
    #
    #         variable[0] = ii
    #         variable[1] = ij
    #
    #         irow += 1
    #         print str(irow)+'\t'+'\t'.join(map(str, variable))
    #
    #     # variables.append(variable)

    ranges = []
    index  = []
    for igrid in range(len(grids)):
        ranges.append([0, len(grids[igrid])])

    from operator import mul
    operations=reduce(mul,(p[1]-p[0] for p in ranges))-1

    result=[i[0] for i in ranges]
    # print result
    index.append([i for i in result])

    pos=len(ranges)-1
    increments=0
    while increments < operations:
        if result[pos]==ranges[pos][1]-1:
            result[pos]=ranges[pos][0]
            pos-=1
        else:
            result[pos]+=1
            increments+=1
            pos=len(ranges)-1 #increment the innermost loop
            # print result
            index.append([i for i in result])

    value = []
    variables = []
    for irow in range(len(index)):
        # print str(irow)
        # print '\t['+'\t'.join(map(str,index[irow]))+']'

        value.append([grids[idim][igrid] for idim,igrid in enumerate(index[irow])])
        # print '\t['+'\t'.join(map(str,value[irow]))+']'

        variables.append([])
        for icol in group:
            variables[irow].append(value[irow][icol])
        # print '\t['+'\t'.join(map(str,variables[irow]))+']'

    # print '\tvariables = ['
    # for irow in range(0,len(variables)-1):
    #     print '\t\t['+','.join(map(str,variables[irow]))+'],'
    # irow = len(variables)-1
    # print '\t\t['+','.join(map(str,variables[irow]))+']'
    # print '\t]'

    return index,value,variables


def createObjFile(folder='grid01',fileName='taihu_objfun.txt',pref='grid',issm=1,iesm=8):
    # 'taihu_decvar.txt'
    # 'taihu_objfun.txt'
    fileName = folder+'/'+fileName
    pass


def writeJson(folder='grid01',fileName='taihu.json',pref='grid',issm=1,iesm=9):
    # fileName = 'taihu.json'
    # 'taihu_decvar.txt'
    # 'taihu_objfun.txt'

    numPop = iesm-issm+1
    numObj = 2

    fileName = folder+'/'+fileName
    outFile = open(fileName, "wt")
    outFile.write("{")
    outFile.write("\n    \"generation\": [")

    outFile.write("\n        {")
    outFile.write("\n            \"variable\"   : [")
    for icase in range(1,issm+1):
        decvarName = folder+'/'+pref+"%08d" % icase+'/taihu_decvar.txt'
        # print decvarName
        with open(decvarName, 'r') as decvarFref:
            variable = [float(elt.strip()) for elt in decvarFref.readline().split('\t')]
        numVar = len(variable)
        outFile.write("\n                [%.6f" % (variable[0]))
        for j in range(1, numVar):
            outFile.write(",%.6f" % (variable[j]))
        outFile.write("]")

    for icase in range(issm+1,iesm+1):
        decvarName = folder+'/'+pref+"%08d" % icase+'/taihu_decvar.txt'
        # print decvarName
        with open(decvarName, 'r') as decvarFref:
            variable = [float(elt.strip()) for elt in decvarFref.readline().split('\t')]
        numVar = len(variable)
        outFile.write(",\n                [%.6f" % (variable[0]))
        for j in range(1, numVar):
            outFile.write(",%.6f" % (variable[j]))
        outFile.write("]")
    outFile.write("\n            ],")


    outFile.write("\n            \"objective\"  : [")
    outFile.write("\n                [")
    for icase in range(1,issm+1):
        objfunName = folder+'/'+pref+"%08d" % icase+'/taihu_objfun.txt'
        # print objfunName
        with open(objfunName, 'r') as objfunFref:
            values   = [float(elt.strip()) for elt in objfunFref.readline().split('\t')]
        outFile.write("\n                    [%.6f" % (values[0]))
        for j in range(1, numObj):
            outFile.write(",%.6f" % (values[j]))
        outFile.write("]")

    for icase in range(issm+1,iesm+1):
        objfunName = folder+'/'+pref+"%08d" % icase+'/taihu_objfun.txt'
        # print objfunName
        with open(objfunName, 'r') as objfunFref:
            values   = [float(elt.strip()) for elt in objfunFref.readline().split('\t')]
        outFile.write(",\n                    [%.6f" % (values[0]))
        for j in range(1, numObj):
            outFile.write(",%.6f" % (values[j]))
        outFile.write("]")
    outFile.write("\n                ]")
    outFile.write("\n            ]")
    outFile.write("\n        }")

    outFile.write("\n    ]")
    outFile.write("\n}")
    outFile.close()


def plotJson(folder, fileName, issave=False):
    import matplotlib as mpl
    if os.environ.get('DISPLAY','') == '':
        # print('--py:Warning:: No display found. Using non-interactive Agg backend')
        mpl.use('Agg')
    import matplotlib.pyplot as plt

    import numpy as np
    import json

    from matplotlib.pyplot import cm


    fileName = folder+'/'+fileName
    with open(fileName) as data_file:
        data = json.load(data_file)

    gen = data["generation"]
    gen_tot = len(gen)

    color = iter(cm.gray(np.linspace(1, 0.1, gen_tot)))
    # color = iter(cm.rainbow(np.linspace(0,1,gen_tot)))
    for index, item in enumerate(gen):
        obj = item["objective"][0]
        obj_tot = len(obj)
        x = []
        y = []
        r = index / gen_tot
        g = index / gen_tot
        b = index / gen_tot

        for iobj in obj:
            x.append(iobj[0])
            y.append(iobj[1])

            # print '['+'\t'.join(map(str,iobj))+']'
        plt.plot(x, y, 'o', color=next(color), label=str(index))

    minmax = [min(x), max(x), min(y), max(y)]

    plt.title(folder)
    plt.xlabel('obj1')
    if minmax[0]==0.0 and minmax[1]==0.0:
        plt.xlim([minmax[0]-0.05,minmax[1]+0.05])
    elif minmax[0]==0.0 and minmax[1]!=0.0:
        plt.xlim([minmax[0]-0.05,minmax[1]+0.05*abs(minmax[1])])
    elif minmax[0]!=0.0 and minmax[1]==0.0:
        plt.xlim([minmax[0]-0.05*abs(minmax[0]),minmax[1]+0.05])
    else:
        plt.xlim([minmax[0]-0.05*abs(minmax[0]),minmax[1]+0.05*abs(minmax[1])])
    # plt.xlim([minmax[0]-0.05*abs(minmax[0]),minmax[1]+0.05*abs(minmax[1])])
    plt.ylabel('obj2')
    if minmax[2]==0.0 and minmax[3]==0.0:
        plt.ylim([minmax[2]-0.05,minmax[3]+0.05])
    elif minmax[2]==0.0 and minmax[3]!=0.0:
        plt.ylim([minmax[2]-0.05,minmax[3]+0.05*abs(minmax[3])])
    elif minmax[2]!=0.0 and minmax[3]==0.0:
        plt.ylim([minmax[2]-0.05*abs(minmax[2]),minmax[3]+0.05])
    else:
        plt.ylim([minmax[2]-0.05*abs(minmax[2]),minmax[3]+0.05*abs(minmax[3])])
    # plt.ylim([minmax[2]-0.05*abs(minmax[2]),minmax[3]+0.05*abs(minmax[3])])
    plt.grid(True)
    # plt.legend(loc='best')
    if issave:
        plt.savefig(fileName+'.png')
        plt.clf()
    else:
        plt.show()

    return obj

def plotAll(folder, fileName,index,value,variables,objectives,issave=False):
    import matplotlib as mpl
    if os.environ.get('DISPLAY','') == '':
        # print('--py:Warning:: No display found. Using non-interactive Agg backend')
        mpl.use('Agg')
    import matplotlib.pyplot as plt

    import numpy as np
    import json

    from matplotlib.pyplot import cm


    x = []
    y = []
    for iobj in objectives:
        x.append(iobj[0])
        y.append(iobj[1])
    plt.plot(x, y, 'o')
    plt.title(folder)
    plt.xlabel('obj1')
    plt.ylabel('obj2')
    plt.grid(True)
    # plt.legend(loc='best')
    if issave:
        plt.savefig(fileName+'.png')
        plt.clf()
    else:
        plt.show()


def readD3DWaq(taihuDir, caseName, varName, iseg=0, itime=0):
    import numpy as np
    from surrogate.files.delft3d import Delft3D

    print '--py:Test:: ['+ taihuDir+', '+caseName+', '+varName+', '+str(iseg)+', '+str(itime)+']'
    z_min = 0.0
    z_max = 3.5

    dx = 500.0 # meter
    dy = 500.0 # meter
    hour2sec = 24*3600

    gridFname = taihuDir
    mapFname  = caseName+'/taihu.map'

    d3d = Delft3D(gridFname=gridFname, mapFname=mapFname)
    moname, varlist, maptime, nseg, nvar, ntime = d3d.initWaqMap()
    # for i in range(len(maptime)):
    #     print '--py:Test:: '+str(i)+':\t'+str(maptime[i])
    # for i in range(len(varlist)):
    #     print '--py:Test:: '+str(i)+':\t'+varlist[i]

    if iseg>=nseg:
        print '--py:Error:: iseg='+str(iseg)+' > nseg='+str(nseg)
        sys.exit(1)

    if varName in varlist:
        ivar = varlist.index(varName)
    else:
        print '--py:Error:: varName='+varName+' is not in the varlist.'
        for i in range(len(varlist)):
            print str(i)+'\t'+varlist[i]
        sys.exit(1)

    if itime>=ntime:
        print '--py:Error:: itime='+str(itime)+' > ntime='+str(ntime)
        for i in range(len(maptime)):
            print str(i)+'\t'+str(maptime[i])
        sys.exit(1)


    print '--py:Test:: Data size [nseg='+str(nseg)+',nvar='+str(nvar)+',ntime='+str(ntime)+']'
    print '--py:Test:: Data read [iseg='+str(iseg)+',ivar='+str(ivar)+',itime='+str(itime)+']'

    objfunFname = caseName+'/taihu_objfun.txt'

    strHisTitle = caseName+'/his_'+varlist[ivar]+'_s'+str(iseg)
    strMapTitle = caseName+'/map_'+varlist[ivar]+'_t'+str(itime)
    # strMapTitle = caseName+'/map_'+varlist[ivar]+'_t'+str(maptime[itime])
    hisFigFname = strHisTitle+'.png'
    mapFigFname = strMapTitle+'.png'
    mapJsonFname= strMapTitle+'.json'

    dataHis = []
    dataMap = []
    jsonData = {'legend': '', 'iseg': -9999, 'itime': -9999, 'x': [], 'y': [], 'z': [], 'zMin': z_min, 'zMax': z_max}

    nrow, ncol, gridX, gridY, gridIndex = d3d.getWaqGrid()
    maptime = [x/hour2sec for x in maptime]

    if iseg==-9999 and itime==-9999:
        # 20170601-update original code
        print '--py:Test:: Old iseg='+str(iseg)+' itime='+str(itime)+' any time'

        checkData = -999999.99
        for jitime in range(ntime):
            tempDataZ = d3d.getWaqMapDataAtVariableTime(ivar=ivar, itime=jitime) # ok
            for i in range(nrow):
                for j in range(ncol):
                    if gridIndex[i][j]>0:
                        if tempDataZ[gridIndex[i][j]][0] > checkData:
                            checkData = tempDataZ[gridIndex[i][j]][0]
                            jseg  = gridIndex[i][j]
                            jtime = jitime
        print '--py:Test:: New iseg='+str(jseg)+' itime='+str(jtime)

    elif iseg==-9999 and itime>=0:
        # 20170601-update original code
        print '--py:Test:: Old iseg='+str(iseg)+' any seg'
        jtime = itime

        tempDataZ = d3d.getWaqMapDataAtVariableTime(ivar=ivar, itime=jtime) # ok
        checkData = -999999.99
        for i in range(nrow):
            for j in range(ncol):
                if gridIndex[i][j]>0:
                    if tempDataZ[gridIndex[i][j]][0] > checkData:
                        checkData = tempDataZ[gridIndex[i][j]][0]
                        jseg = gridIndex[i][j]
        print '--py:Test:: New iseg='+str(jseg)

    elif iseg>=0 and itime==-9999:
        # 20170601-update original code
        print '--py:Test:: Old itime='+str(itime)+' any time'
        jseg = iseg

        tempDataSeg = d3d.getWaqMapDataAtSegment(iseg=jseg) # ok
        tempDataHis = tempDataSeg[0][ivar][:]
        tempDataHis = np.array(tempDataHis)
        jtime = np.nanargmax(tempDataHis)
        print '--py:Test:: New itime='+str(jtime)

    elif iseg>=0 and itime>=0:
        # 20170601-original code
        print '--py:Test:: Old iseg='+str(iseg)+' itime='+str(itime)
        jseg = iseg
        jtime = itime
        print '--py:Test:: New iseg='+str(jseg)+' itime='+str(jtime)

    else:
        print '--py:Error:: iseg='+str(iseg)+' itime='+str(itime)
        sys.exit(1)


    strHisTitle = caseName+'/his_'+varlist[ivar]+'_s'+str(jseg)
    strMapTitle = caseName+'/map_'+varlist[ivar]+'_t'+str(jtime)

    jsonData['legend'] = varlist[ivar]
    jsonData['iseg']   = jseg
    jsonData['itime']  = jtime


    dataSeg = d3d.getWaqMapDataAtSegment(iseg=jseg) # ok
    dataHis = dataSeg[0][ivar][:]
    dataHis = np.array(dataHis)

    dataZ = d3d.getWaqMapDataAtVariableTime(ivar=ivar, itime=jtime) # ok
    for i in range(nrow):
        dataMap.append([dataZ[gridIndex[i][j]][0] if gridIndex[i][j]>0 else 0 for j in range(ncol)])
    dataMap = np.array(dataMap)

    for i in range(nrow):
        for j in range(ncol):
            if gridIndex[i][j]>0:
                jsonData['x'].append(gridX[i][j])
                jsonData['y'].append(gridY[i][j])
                jsonData['z'].append(dataZ[gridIndex[i][j]][0])

    gridY = np.array(gridY)
    gridX = np.array(gridX)
    gridY = gridY*dy
    gridX = gridX*dx

    dataMap[gridX==0] = np.NaN
    gridY[gridX==0]   = np.NaN
    gridX[gridX==0]   = np.NaN

    gridIndex = np.array(gridIndex)
    dataMap[gridIndex==9969] = np.NaN
    dataMap[gridIndex==6939] = np.NaN

    dataMap = np.ma.masked_invalid(dataMap)
    gridY   = np.ma.masked_invalid(gridY)
    gridX   = np.ma.masked_invalid(gridX)

    savePlotHis(hisFigFname, maptime, dataHis, varlist, ivar, strHisTitle)
    savePlotMap(mapFigFname, gridX, gridY, dataMap, z_min, z_max, strMapTitle)


def savePlotHis(hisFigFname, x, z, varlist, ivar, strHisTitle):
    import matplotlib.pyplot as plt
    from datetime import date,timedelta

    start = date(2008, 1, 1)+timedelta(days=1)
    date_string = start.strftime('%Y-%m-%d')

    print '--py:Start:: Plot his.'
    plt.plot(x,z)
    plt.title(strHisTitle)
    plt.xlabel('time [day]')
    plt.ylabel(varlist[ivar]+' [g/m^3]')
    plt.savefig(hisFigFname)
    # plt.show()
    plt.clf()


def savePlotMap(mapFigFname, x, y, z, z_min, z_max, strMapTitle):
    import matplotlib.pyplot as plt

    print '--py:Start:: Plot map.'
    plt.pcolor(x, y, z, cmap='jet', vmin=z_min, vmax=z_max)
    plt.axis([x.min(), x.max(), y.min(), y.max()])
    plt.colorbar()
    plt.title(strMapTitle)
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.savefig(mapFigFname)
    # plt.show()
    plt.clf()


def printLog(folder, fileName, index,value,variables,objectives):
    # print '\n'+folder+'/'+fileName
    for irow in range(len(index)):
        # Print
        print str(irow)\
              +'\t['+'\t'.join(map(str,index[irow]))+']'\
              +'\t => ['+'\t'.join(map(str,value[irow]))+']'\
              +'\t => ['+'\t'.join(map(str,objectives[irow]))+']'

        # # Excel
        # print folder+'-'+str(irow+1)\
        #       +'\t'+'\t'.join(map(str,value[irow]))\
        #       +'\t'+'\t'.join(map(str,objectives[irow]))

    pass


if __name__ == "__main__":
    print "=================================================="
    print "==                                              =="
    print "==   Project:  Surrogate Model                  =="
    print "==   File:     d3d_test.py                      =="
    print "==                                              =="
    print "==   Author:   Quan Pan                         =="
    print "==   Email:    quanpan302@hotmail.com           =="
    print "==                                              =="
    print "==   License:  MIT License                      =="
    print "==   Create:   2017-06-06                       =="
    print "==                                              =="
    print "=================================================="

    # python run_grid.py -s 1 -e 2 2>&1

    # icaseStart = 1
    # icaseEnd = 2
    # os.system('./run.sh '+str(icaseStart)+' '+str(icaseEnd))

    # for itime in range(0,367):
    #     readD3DWaq('delcoupl/couplnef.txt', 's00000000', 'GREENS', iseg=9969, itime=itime)

    # input         sim g**  g0*,g1*  g2*
    # "Tai"         n   0   0   0
    # "Wang"        y   1   1   1
    # "1_1"         y   2   2   0
    # "1_2"         y   2   2   0
    # "1_3"         y   2   2   0
    # "1_4"         y   2   2   0
    # "1_5"         y   2   2   0
    # "2_1"         y   3   3   0
    # "2_2"         y   3   3   0
    # "2_3"         y   3   3   0
    # "2_4"         y   3   3   0
    # "3_1"         n   0   0   0
    # "3_2"         n   0   0   0
    # "3_3"         n   0   0   0
    # "3_4"         n   0   0   0
    # "3_5"         n   0   0   0
    # "4_1"         y   4   4   0
    # "4_2"         y   4   4   0
    # "4_3"         y   4   4   0
    # "4_4"         y   4   4   0
    # "4_5"         y   4   4   0
    # "5_1"         n   0   0   0
    # "5_2"         n   0   0   0
    # "5_3"         n   0   0   0
    # "5_4"         n   0   0   0
    # "Jiapu"       y   5   5   2
    # "xiaomeikou"  y   6   5   2
    # "daqian"      y   7   5   2
    # "hulou"       y   8   5   2
    # "dapu_1"      y   9   5   3
    # "xiaowanli_1" y   10  5   4
    # "tuoshan_1"   y   11  5   5
    # "zhushan_1"   y   12  5   6
    # "manshan"     y   13  5   2
    # "dapu_2"      y   14  5   3
    # "xiaowanli_2" y   15  5   4
    # "xiaowanli_3" y   15  5   4
    # "zhushan_2"   y   16  5   6
    # "shadungang1" y   17  5   7
    # "shadungang2" y   17  5   7
    # "shadungang3" y   18  5   7


    # =====================================================
    # grid01_02
    # =====================================================

    indexAll,valueAll,variablesAll,objectivesAll = [],[],[],[]
    # grid01
    group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    group = [
        0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
        0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5
    ]
    grids = [
        [1.0],
        [0.0, 0.25, 0.5, 0.75, 1.0],
        [1.0],
        [1.0],
        [1.0],
        [1.0]
    ]
    folder,fileName,pref,issm,iesm = 'grid01','taihu.json','grid',1,5
    index,value,variables = meshgridMD(group,grids)
    # writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    objectives = plotJson(folder, fileName, issave=True)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

        # readD3DWaq('delcoupl/couplnef.txt', folder+'/'+pref+"%08d" % (irow+1), 'GREENS', iseg=9969, itime=4)


    # grid02
    group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    group = [
        0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
        0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5
    ]
    grids = [
        [1.0],
        [1.0],
        [1.0],
        [1.0],
        [1.0],
        [0.0, 0.25, 0.5, 0.75, 1.0]
    ]
    folder,fileName,pref,issm,iesm = 'grid02','taihu.json','grid',1,5
    index,value,variables = meshgridMD(group,grids)
    # writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    objectives = plotJson(folder, fileName, issave=True)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

        # readD3DWaq('delcoupl/couplnef.txt', folder+'/'+pref+"%08d" % (irow+1), 'GREENS', iseg=9969, itime=4)



    # =====================================================
    # grid10_13
    # =====================================================

    # indexAll,valueAll,variablesAll,objectivesAll = [],[],[],[]
    # grid10
    group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    group = [
        0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
        0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5
    ]
    grids = [
        [1.0],
        [0.0, 0.5, 1.0],
        [1.0],
        [1.0],
        [1.0],
        [0.0, 0.5, 1.0]
    ]
    folder,fileName,pref,issm,iesm = 'grid10','taihu.json','grid',1,9
    index,value,variables = meshgridMD(group,grids)
    writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    objectives = plotJson(folder, fileName, issave=True)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

        # readD3DWaq('delcoupl/couplnef.txt', folder+'/'+pref+"%08d" % (irow+1), 'GREENS', iseg=9969, itime=4)


    # grid11
    group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    group = [
        0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
        0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5
    ]
    grids = [
        [1.0],
        [1.0],
        [0.0, 0.5, 1.0],
        [0.0, 0.5, 1.0],
        [0.0, 0.5, 1.0],
        [0.0]
    ]
    folder,fileName,pref,issm,iesm = 'grid11','taihu.json','grid',1,27
    index,value,variables = meshgridMD(group,grids)
    # writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    objectives = plotJson(folder, fileName, issave=True)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

        # readD3DWaq('delcoupl/couplnef.txt', folder+'/'+pref+"%08d" % (irow+1), 'GREENS', iseg=9969, itime=4)


    # grid12
    group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    group = [
        0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
        0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5
    ]
    grids = [
        [1.0],
        [1.0],
        [0.0, 0.5, 1.0],
        [0.0, 0.5, 1.0],
        [0.0, 0.5, 1.0],
        [0.5]
    ]
    folder,fileName,pref,issm,iesm = 'grid12','taihu.json','grid',1,27
    index,value,variables = meshgridMD(group,grids)
    # writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    objectives = plotJson(folder, fileName, issave=True)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

        # readD3DWaq('delcoupl/couplnef.txt', folder+'/'+pref+"%08d" % (irow+1), 'GREENS', iseg=9969, itime=4)


    # grid13
    group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    group = [
        0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
        0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5
    ]
    grids = [
        [1.0],
        [1.0],
        [0.0, 0.5, 1.0],
        [0.0, 0.5, 1.0],
        [0.0, 0.5, 1.0],
        [1.0]
    ]
    folder,fileName,pref,issm,iesm = 'grid13','taihu.json','grid',1,27
    index,value,variables = meshgridMD(group,grids)
    # writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    objectives = plotJson(folder, fileName, issave=True)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

        # readD3DWaq('delcoupl/couplnef.txt', folder+'/'+pref+"%08d" % (irow+1), 'GREENS', iseg=9969, itime=4)


    # folder,fileName = 'grid1*','taihu.json.all1'
    # plotAll(folder, fileName,indexAll,valueAll,variablesAll,objectivesAll,issave=True)
    #
    # from pylab import *
    # from mpl_cfaces import cface
    # fig = figure(figsize=(11,11))
    # for i in range(90):
    #     ax = fig.add_subplot(10,9,i+1,aspect='equal')
    #     # def cface(ax, x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18):
    #     # x1 = height  of upper face
    #     # x2 = overlap of lower face
    #     # x3 = half of vertical size of face
    #     # x4 = width of upper face
    #     # x5 = width of lower face
    #
    #     # x6 = length of nose
    #
    #     # x7 = vertical position of mouth
    #     # x8 = curvature of mouth
    #     # x9 = width of mouth
    #
    #     # x10 = vertical position of eyes
    #     # x11 = separation of eyes
    #     # x12 = slant of eyes
    #     # x13 = eccentricity of eyes
    #     # x14 = size of eyes
    #
    #     # x15 = position of pupils
    #
    #     # x16 = vertical position of eyebrows
    #     # x17 = slant of eyebrows
    #     # x18 = size of eyebrows
    #
    #     # cface(ax, .9, *rand(17))
    #     cface(ax,
    #           0.9,
    #           0.9,
    #           0.3,
    #           0.9*valueAll[i][1],
    #           0.9*valueAll[i][2],
    #
    #           valueAll[i][3],
    #
    #           0.6,
    #           0.5,
    #           valueAll[i][4],
    #
    #           0.4,
    #           0.6,
    #           0.5,
    #           0.6,
    #           valueAll[i][5],
    #
    #           0.5,
    #
    #           0.8,
    #           0.5,
    #           1.0
    #           )
    #     ax.axis([-1.2,1.2,-1.2,1.2])
    #     ax.set_xticks([])
    #     ax.set_yticks([])
    #     title = 'GA mean '+str(objectivesAll[i][0])
    #     ax.text(.5,.9,title,horizontalalignment='center',transform=ax.transAxes,fontsize=6)
    # fig.subplots_adjust(hspace=0, wspace=0)
    # show()



    # =====================================================
    # grid21_26
    # =====================================================

    # indexAll,valueAll,variablesAll,objectivesAll = [],[],[],[]
    # grid21
    group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    group = [
        0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,3,4,5,6,2,3,4,4,6,7,7,7,
        0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,3,4,5,6,2,3,4,4,6,7,7,7
    ]
    grids = [
        [1.0],
        [1.0],
        [0.0, 0.25, 0.5, 0.75, 1.0],
        [1.0],
        [1.0],
        [1.0],
        [1.0],
        [1.0]
    ]
    folder,fileName,pref,issm,iesm = 'grid21','taihu.json','grid',1,5
    index,value,variables = meshgridMD(group,grids)
    # writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    objectives = plotJson(folder, fileName, issave=True)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

        # readD3DWaq('delcoupl/couplnef.txt', folder+'/'+pref+"%08d" % (irow+1), 'GREENS', iseg=9969, itime=4)


    # grid22
    group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    group = [
        0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,3,4,5,6,2,3,4,4,6,7,7,7,
        0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,3,4,5,6,2,3,4,4,6,7,7,7
    ]
    grids = [
        [1.0],
        [1.0],
        [1.0],
        [0.0, 0.25, 0.5, 0.75, 1.0],
        [1.0],
        [1.0],
        [1.0],
        [1.0]
    ]
    folder,fileName,pref,issm,iesm = 'grid22','taihu.json','grid',1,5
    index,value,variables = meshgridMD(group,grids)
    # writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    objectives = plotJson(folder, fileName, issave=True)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

        # readD3DWaq('delcoupl/couplnef.txt', folder+'/'+pref+"%08d" % (irow+1), 'GREENS', iseg=9969, itime=4)


    # grid23
    group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    group = [
        0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,3,4,5,6,2,3,4,4,6,7,7,7,
        0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,3,4,5,6,2,3,4,4,6,7,7,7
    ]
    grids = [
        [1.0],
        [1.0],
        [1.0],
        [1.0],
        [0.0, 0.25, 0.5, 0.75, 1.0],
        [1.0],
        [1.0],
        [1.0]
    ]
    folder,fileName,pref,issm,iesm = 'grid23','taihu.json','grid',1,5
    index,value,variables = meshgridMD(group,grids)
    # writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    objectives = plotJson(folder, fileName, issave=True)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

        # readD3DWaq('delcoupl/couplnef.txt', folder+'/'+pref+"%08d" % (irow+1), 'GREENS', iseg=9969, itime=4)


    # grid24
    group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    group = [
        0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,3,4,5,6,2,3,4,4,6,7,7,7,
        0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,3,4,5,6,2,3,4,4,6,7,7,7
    ]
    grids = [
        [1.0],
        [1.0],
        [1.0],
        [1.0],
        [1.0],
        [0.0, 0.25, 0.5, 0.75, 1.0],
        [1.0],
        [1.0]
    ]
    folder,fileName,pref,issm,iesm = 'grid24','taihu.json','grid',1,5
    index,value,variables = meshgridMD(group,grids)
    # writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    objectives = plotJson(folder, fileName, issave=True)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

        # readD3DWaq('delcoupl/couplnef.txt', folder+'/'+pref+"%08d" % (irow+1), 'GREENS', iseg=9969, itime=4)


    # grid25
    group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    group = [
        0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,3,4,5,6,2,3,4,4,6,7,7,7,
        0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,3,4,5,6,2,3,4,4,6,7,7,7
    ]
    grids = [
        [1.0],
        [1.0],
        [1.0],
        [1.0],
        [1.0],
        [1.0],
        [0.0, 0.25, 0.5, 0.75, 1.0],
        [1.0]
    ]
    folder,fileName,pref,issm,iesm = 'grid25','taihu.json','grid',1,5
    index,value,variables = meshgridMD(group,grids)
    # writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    objectives = plotJson(folder, fileName, issave=True)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

        # readD3DWaq('delcoupl/couplnef.txt', folder+'/'+pref+"%08d" % (irow+1), 'GREENS', iseg=9969, itime=4)


    # grid26
    group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    group = [
        0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,3,4,5,6,2,3,4,4,6,7,7,7,
        0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,3,4,5,6,2,3,4,4,6,7,7,7
    ]
    grids = [
        [1.0],
        [1.0],
        [1.0],
        [1.0],
        [1.0],
        [1.0],
        [1.0],
        [0.0, 0.25, 0.5, 0.75, 1.0]
    ]
    folder,fileName,pref,issm,iesm = 'grid26','taihu.json','grid',1,5
    index,value,variables = meshgridMD(group,grids)
    # writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    objectives = plotJson(folder, fileName, issave=True)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

        # readD3DWaq('delcoupl/couplnef.txt', folder+'/'+pref+"%08d" % (irow+1), 'GREENS', iseg=9969, itime=4)


    # folder,fileName = 'grid2*','taihu.json.all2'
    # plotAll(folder, fileName,indexAll,valueAll,variablesAll,objectivesAll,issave=True)
    #
    # from pylab import *
    # from mpl_cfaces import cface
    # fig = figure(figsize=(11,11))
    # for i in range(30):
    #     ax = fig.add_subplot(6,5,i+1,aspect='equal')
    #     # def cface(ax, x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18):
    #     # x1 = height  of upper face
    #     # x2 = overlap of lower face
    #     # x3 = half of vertical size of face
    #     # x4 = width of upper face
    #     # x5 = width of lower face
    #
    #     # x6 = length of nose
    #
    #     # x7 = vertical position of mouth
    #     # x8 = curvature of mouth
    #     # x9 = width of mouth
    #
    #     # x10 = vertical position of eyes
    #     # x11 = separation of eyes
    #     # x12 = slant of eyes
    #     # x13 = eccentricity of eyes
    #     # x14 = size of eyes
    #
    #     # x15 = position of pupils
    #
    #     # x16 = vertical position of eyebrows
    #     # x17 = slant of eyebrows
    #     # x18 = size of eyebrows
    #
    #     # cface(ax, .9, *rand(17))
    #     cface(ax,
    #           0.9,
    #           0.9,
    #           0.3,
    #           0.9,
    #           0.9,
    #
    #           1.0,
    #
    #           0.6,
    #           0.5,
    #           1.0,
    #
    #           0.4,
    #           0.6*valueAll[i][2],
    #           0.5*valueAll[i][3],
    #           0.6*valueAll[i][4],
    #           1.0,
    #
    #           0.5*valueAll[i][5],
    #
    #           0.8*valueAll[i][6],
    #           0.5*valueAll[i][7],
    #           1.0
    #           )
    #     ax.axis([-1.2,1.2,-1.2,1.2])
    #     ax.set_xticks([])
    #     ax.set_yticks([])
    #     title = 'GA mean '+str(objectivesAll[i][0])
    #     ax.text(.5,.9,title,horizontalalignment='center',transform=ax.transAxes,fontsize=10)
    #     fig.subplots_adjust(hspace=0, wspace=0)
    # show()



    # folder,fileName = 'gridAll','taihu.json.all'
    # plotAll(folder, fileName,indexAll,valueAll,variablesAll,objectivesAll,issave=False)


    # import sklearn
    # print('The scikit-learn version is {}.'.format(sklearn.__version__))
    #
    # Mac: The scikit-learn version is 0.18.dev0. Before 20170721
    # sudo pip install scikit-learn==0.18.1
    # Mac:  The scikit-learn version is 0.18.1. After 20170721
    #
    # VB:  The scikit-learn version is 0.18.1.

    import numpy as np

    Xold_ind = np.array(variablesAll)
    Yold_obj = np.array(objectivesAll)

    Xtst_ind = np.zeros((1, len(Xold_ind[0][:])))
    Ytst_obj = np.zeros((1, len(Yold_obj[0][:])))

    import warnings
    warnings.filterwarnings(action="ignore", category=Warning)
    warnings.filterwarnings(action="ignore", category=DeprecationWarning)

    # sklearn ANN
    from sklearn.neural_network import MLPRegressor
    from sklearn import metrics

    # sklearn GridSearchCV
    from sklearn.model_selection import GridSearchCV


    # # tune 01 all
    # tuned_parameters = [{'solver': ['lbfgs','sgd','adam'],
    #                      'activation' : ['logistic', 'tanh', 'relu'],
    #                      'hidden_layer_sizes': [x for x in range(10,110,10)],
    #                      'batch_size' : [10,20,50,100,200],
    #                      'random_state' : [1,5,10]
    #                      }]
    # # Mac: The scikit-learn version is 0.18.dev0. Before 20170721
    # # Best parameters set found on development set:
    # # {'activation': 'relu', 'random_state': 5, 'batch_size': 10, 'solver': 'lbfgs', 'hidden_layer_sizes': 60}
    # #
    # # Test-18 2.224826	6.782065
    # # Predict 2.22091247306	6.75923620417
    # # Score   0.0	0.999948337965
    # #
    # # GridSearchCV(cv=None, error_score='raise',
    # #        estimator=MLPRegressor(activation='relu', solver='adam', alpha=0.0001,
    # #        batch_size=200, beta_1=0.9, beta_2=0.999, early_stopping=False,
    # #        epsilon=1e-08, hidden_layer_sizes=(100,), learning_rate='constant',
    # #        learning_rate_init=0.001, max_iter=200, momentum=0.9,
    # #        nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
    # #        tol=0.0001, validation_fraction=0.1, verbose=False,
    # #        warm_start=False),
    # #        fit_params={}, iid=True, n_jobs=1,
    # #        param_grid=[{'activation': ['logistic', 'tanh', 'relu'], 'random_state': [1, 5, 10], 'batch_size': [10, 20, 50, 100, 200], 'solver': ['lbfgs', 'sgd', 'adam'], 'hidden_layer_sizes': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}],
    # #        pre_dispatch='2*n_jobs', refit=True, scoring=None, verbose=0)
    #
    # # Mac:  The scikit-learn version is 0.18.1. After 20170721
    # # Best parameters set found on development set:
    # # {'activation': 'relu', 'random_state': 5, 'solver': 'lbfgs', 'batch_size': 10, 'hidden_layer_sizes': 70}
    # #
    # # Test-18 2.224826	6.782065
    # # Predict 2.21987571269	6.76477696541
    # # Score   0.0	0.999968858356
    # #
    # # GridSearchCV(cv=None, error_score='raise',
    # #        estimator=MLPRegressor(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
    # #        beta_2=0.999, early_stopping=False, epsilon=1e-08,
    # #        hidden_layer_sizes=(100,), learning_rate='constant',
    # #        learning_rate_init=0.001, max_iter=200, momentum=0.9,
    # #        nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
    # #        solver='adam', tol=0.0001, validation_fraction=0.1, verbose=False,
    # #        warm_start=False),
    # #        fit_params={}, iid=True, n_jobs=1,
    # #        param_grid=[{'random_state': [1, 5, 10], 'activation': ['logistic', 'tanh', 'relu'], 'hidden_layer_sizes': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 'batch_size': [10, 20, 50, 100, 200], 'solver': ['lbfgs', 'sgd', 'adam']}],
    # #        pre_dispatch='2*n_jobs', refit=True, return_train_score=True,
    # #        scoring=None, verbose=0)


    # # tune 02 incremental learning "sgd"
    # tuned_parameters = [{'solver': ['sgd'],
    #                      'activation' : ['logistic', 'tanh', 'relu'],
    #                      'hidden_layer_sizes': [x for x in range(10,110,10)],
    #                      'batch_size' : [10,20,50,100,200],
    #                      'random_state' : [1,5,10]
    #                      }]
    # # Mac: The scikit-learn version is 0.18.dev0. Before 20170721
    # # Best parameters set found on development set:
    # # {'activation': 'tanh', 'random_state': 5, 'batch_size': 10, 'solver': 'sgd', 'hidden_layer_sizes': 80}
    # #
    # # Test-18 2.224826	6.782065
    # # Predict 2.25521003748	6.62190527774
    # # Score   0.0	0.997440891794
    # #
    # # GridSearchCV(cv=None, error_score='raise',
    # #        estimator=MLPRegressor(activation='relu', solver='adam', alpha=0.0001,
    # #        batch_size=200, beta_1=0.9, beta_2=0.999, early_stopping=False,
    # #        epsilon=1e-08, hidden_layer_sizes=(100,), learning_rate='constant',
    # #        learning_rate_init=0.001, max_iter=200, momentum=0.9,
    # #        nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
    # #        tol=0.0001, validation_fraction=0.1, verbose=False,
    # #        warm_start=False),
    # #        fit_params={}, iid=True, n_jobs=1,
    # #        param_grid=[{'activation': ['logistic', 'tanh', 'relu'], 'random_state': [1, 5, 10], 'batch_size': [10, 20, 50, 100, 200], 'solver': ['sgd'], 'hidden_layer_sizes': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}],
    # #        pre_dispatch='2*n_jobs', refit=True, scoring=None, verbose=0)
    #
    # # Mac:  The scikit-learn version is 0.18.1. After 20170721
    # # Best parameters set found on development set:
    # # {'activation': 'tanh', 'random_state': 5, 'solver': 'sgd', 'batch_size': 20, 'hidden_layer_sizes': 30}
    # #
    # # Test-18 2.224826	6.782065
    # # Predict 2.2348922431	6.68759109001
    # # Score   0.0	0.999130733513
    # #
    # # GridSearchCV(cv=None, error_score='raise',
    # #        estimator=MLPRegressor(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
    # #        beta_2=0.999, early_stopping=False, epsilon=1e-08,
    # #        hidden_layer_sizes=(100,), learning_rate='constant',
    # #        learning_rate_init=0.001, max_iter=200, momentum=0.9,
    # #        nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
    # #        solver='adam', tol=0.0001, validation_fraction=0.1, verbose=False,
    # #        warm_start=False),
    # #        fit_params={}, iid=True, n_jobs=1,
    # #        param_grid=[{'random_state': [1, 5, 10], 'activation': ['logistic', 'tanh', 'relu'], 'hidden_layer_sizes': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 'batch_size': [10, 20, 50, 100, 200], 'solver': ['sgd']}],
    # #        pre_dispatch='2*n_jobs', refit=True, return_train_score=True,
    # #        scoring=None, verbose=0)



    # # 00-fit GridSearchCV
    # clf = GridSearchCV(MLPRegressor(random_state=1), tuned_parameters)
    # clf.fit(Xold_ind, Yold_obj)
    # print ''
    # print("Best parameters set found on development set:")
    # print(clf.best_params_)



    # 01-fit MLPRegressor
    clf = MLPRegressor(activation='relu', solver='lbfgs', hidden_layer_sizes=(70), batch_size=10, random_state=5)
    clf.fit(Xold_ind, Yold_obj)
    # # Mac:  The scikit-learn version is 0.18.1. After 20170721
    # Test-18 2.224826	6.782065
    # Predict 2.21987571269	6.76477696541
    # Score   0.0	0.999968858356
    #
    # MLPRegressor(activation='relu', alpha=0.0001, batch_size=10, beta_1=0.9,
    #        beta_2=0.999, early_stopping=False, epsilon=1e-08,
    #        hidden_layer_sizes=70, learning_rate='constant',
    #        learning_rate_init=0.001, max_iter=200, momentum=0.9,
    #        nesterovs_momentum=True, power_t=0.5, random_state=5, shuffle=True,
    #        solver='lbfgs', tol=0.0001, validation_fraction=0.1, verbose=False,
    #        warm_start=False)



    # # 02a-partial_fit MLPRegressor
    # clf = MLPRegressor(activation='tanh', solver='sgd', hidden_layer_sizes=(30), batch_size=20, random_state=5)
    # clf.fit(Xold_ind, Yold_obj)
    # # Mac:  The scikit-learn version is 0.18.1. After 20170721
    # # Test-18 2.224826	6.782065
    # # Predict 2.2348922431	6.68759109001
    # # Score   0.0	0.999130733513
    # #
    # # MLPRegressor(activation='tanh', alpha=0.0001, batch_size=20, beta_1=0.9,
    # #        beta_2=0.999, early_stopping=False, epsilon=1e-08,
    # #        hidden_layer_sizes=30, learning_rate='constant',
    # #        learning_rate_init=0.001, max_iter=200, momentum=0.9,
    # #        nesterovs_momentum=True, power_t=0.5, random_state=5, shuffle=True,
    # #        solver='sgd', tol=0.0001, validation_fraction=0.1, verbose=False,
    # #        warm_start=False)


    # # 02b-partial_fit MLPRegressor
    # clf = MLPRegressor(activation='tanh', solver='sgd', hidden_layer_sizes=(30), batch_size=20, random_state=5)
    # clf.partial_fit(Xold_ind, Yold_obj)
    # # Mac:  The scikit-learn version is 0.18.1. After 20170721
    # # Test-18 2.224826	6.782065
    # # Predict 2.09491197208	3.67495802572
    # # Score   0.0	0.0686833178897
    # #
    # # MLPRegressor(activation='tanh', alpha=0.0001, batch_size=20, beta_1=0.9,
    # #        beta_2=0.999, early_stopping=False, epsilon=1e-08,
    # #        hidden_layer_sizes=30, learning_rate='constant',
    # #        learning_rate_init=0.001, max_iter=200, momentum=0.9,
    # #        nesterovs_momentum=True, power_t=0.5, random_state=5, shuffle=True,
    # #        solver='sgd', tol=0.0001, validation_fraction=0.1, verbose=False,
    # #        warm_start=False)


    # for itst_ind in range(len(Xold_ind)):
    for itst_ind in range(18,19):
        Xtst_ind[0] = Xold_ind[itst_ind]
        Ytst_obj[0] = Yold_obj[itst_ind]

        Ynew_obj = clf.predict(Xtst_ind)

        print ''
        # print 'Test-'+str(itst_ind)+'\t'.join(map(str,Ytst_obj[0]))+' => '+'\t'.join(map(str,Xtst_ind[0]))
        print 'Test-'+str(itst_ind)+' '+'\t'.join(map(str,Ytst_obj[0]))
        print 'Predict '+'\t'.join(map(str,Ynew_obj[0]))
        print 'Score   '+str(metrics.r2_score(Ytst_obj,Ynew_obj))+'\t'+str(metrics.r2_score(Ytst_obj[0],Ynew_obj[0]))

    # # sklearn linear
    # from sklearn.linear_model import LinearRegression
    # clf = LinearRegression()
    # clf.fit(Xold_ind, Yold_obj)

    print ''
    print clf

    # # methode01
    # from sklearn.externals import joblib
    # joblib.dump(clf, 'test_save_joblib.pkl')
    # # clf = joblib.load('filename.pkl')

    # methode02
    import cPickle as pickle
    # pickle.dump(clf, open('d3d_ann_moea.pkl', 'wb'))
    # # clf = pickle.load(open('/var/www/html/taihu/d3d_ann_moea.pkl', 'rb'))

    # print '\ncPickle'
    # clf = pickle.load(open('d3d_ann_moea.pkl', 'rb'))
    # # for itst_ind in range(len(Xold_ind)):
    # for itst_ind in range(18,19):
    #     Xtst_ind[0] = Xold_ind[itst_ind]
    #     Ytst_obj[0] = Yold_obj[itst_ind]
    #
    #     Ynew_obj = clf.predict(Xtst_ind)
    #
    #     print ''
    #     # print 'Test-'+str(itst_ind)+'\t'.join(map(str,Ytst_obj[0]))+' => '+'\t'.join(map(str,Xtst_ind[0]))
    #     print 'Test-'+str(itst_ind)+' '+'\t'.join(map(str,Ytst_obj[0]))
    #     print 'Predict '+'\t'.join(map(str,Ynew_obj[0]))
    #     print 'Score   '+str(metrics.r2_score(Ytst_obj,Ynew_obj))+'\t'+str(metrics.r2_score(Ytst_obj[0],Ynew_obj[0]))

    print '\nEnd'
