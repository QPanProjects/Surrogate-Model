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


def printLog(folder, fileName, index,value,variables,objectives):
    print '\n'+folder+'/'+fileName
    for irow in range(len(index)):
        print str(irow)\
              +'\t['+'\t'.join(map(str,index[irow]))+']'\
              +'\t => ['+'\t'.join(map(str,value[irow]))+']'\
              +'\t => ['+'\t'.join(map(str,objectives[irow]))+']'

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

    # input         sim g**  g1*  g2*
    # "Tai",        n   0   0   0
    # "Wang",       y   1   1   1
    # "1_1",        y   2   2   0
    # "1_2",        y   2   2   0
    # "1_3",        y   2   2   0
    # "1_4",        y   2   2   0
    # "1_5",        y   2   2   0
    # "2_1",        y   3   3   0
    # "2_2",        y   3   3   0
    # "2_3",        y   3   3   0
    # "2_4",        y   3   3   0
    # "3_1",        n   0   0   0
    # "3_2",        n   0   0   0
    # "3_3",        n   0   0   0
    # "3_4",        n   0   0   0
    # "3_5",        n   0   0   0
    # "4_1",        y   4   4   0
    # "4_2",        y   4   4   0
    # "4_3",        y   4   4   0
    # "4_4",        y   4   4   0
    # "4_5",        y   4   4   0
    # "5_1",        n   0   0   0
    # "5_2",        n   0   0   0
    # "5_3",        n   0   0   0
    # "5_4",        n   0   0   0
    # "Jiapu",      y   5   5   2
    # "xiaomeikou", y   6   5   2
    # "daqian",     y   7   5   2
    # "hulou",      y   8   5   2
    # "dapu_1",     y   9   5   3
    # "xiaowanli_1",y   10  5   4
    # "tuoshan_1",  y   11  5   5
    # "zhushan_1",  y   12  5   6
    # "manshan",    y   13  5   2
    # "dapu_2",     y   14  5   3
    # "xiaowanli_2",y   15  5   4
    # "xiaowanli_3",y   15  5   4
    # "zhushan_2",  y   16  5   6
    # "shadungang1",y   17  5   7
    # "shadungang2",y   17  5   7
    # "shadungang3" y   18  5   7

    indexAll,valueAll,variablesAll,objectivesAll = [],[],[],[]
    # # grid01
    # group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    # group = [
    #     0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
    #     0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5
    # ]
    # grids = [
    #     [1.0],
    #     [0.0, 0.25, 0.5, 0.75, 1.0],
    #     [1.0],
    #     [1.0],
    #     [1.0],
    #     [1.0]
    # ]
    # folder,fileName,pref,issm,iesm = 'grid01','taihu.json','grid',1,5
    # index,value,variables = meshgridMD(group,grids)
    # # writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    # objectives = plotJson(folder, fileName, issave=False)
    # printLog(folder, fileName, index,value,variables,objectives)
    # for irow in range(len(index)):
    #     indexAll.append(index[irow])
    #     valueAll.append(value[irow])
    #     variablesAll.append(variables[irow])
    #     objectivesAll.append(objectives[irow])
    #
    # # grid02
    # group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    # group = [
    #     0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
    #     0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5
    # ]
    # grids = [
    #     [1.0],
    #     [1.0],
    #     [1.0],
    #     [1.0],
    #     [1.0],
    #     [0.0, 0.25, 0.5, 0.75, 1.0]
    # ]
    # folder,fileName,pref,issm,iesm = 'grid02','taihu.json','grid',1,5
    # index,value,variables = meshgridMD(group,grids)
    # # writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    # objectives = plotJson(folder, fileName, issave=False)
    # printLog(folder, fileName, index,value,variables,objectives)
    # for irow in range(len(index)):
    #     indexAll.append(index[irow])
    #     valueAll.append(value[irow])
    #     variablesAll.append(variables[irow])
    #     objectivesAll.append(objectives[irow])

    # # grid10
    # group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    # group = [
    #     0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
    #     0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5
    # ]
    # grids = [
    #     [1.0],
    #     [0.0, 0.5, 1.0],
    #     [1.0],
    #     [1.0],
    #     [1.0],
    #     [0.0, 0.5, 1.0]
    # ]
    # folder,fileName,pref,issm,iesm = 'grid10','taihu.json','grid',1,9
    # index,value,variables = meshgridMD(group,grids)
    # writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    # objectives = plotJson(folder, fileName, issave=True)
    # printLog(folder, fileName, index,value,variables,objectives)
    # for irow in range(len(index)):
    #     indexAll.append(index[irow])
    #     valueAll.append(value[irow])
    #     variablesAll.append(variables[irow])
    #     objectivesAll.append(objectives[irow])
    #
    # # grid11
    # group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    # group = [
    #     0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
    #     0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5
    # ]
    # grids = [
    #     [1.0],
    #     [1.0],
    #     [0.0, 0.5, 1.0],
    #     [0.0, 0.5, 1.0],
    #     [0.0, 0.5, 1.0],
    #     [0.0]
    # ]
    # folder,fileName,pref,issm,iesm = 'grid11','taihu.json','grid',1,27
    # index,value,variables = meshgridMD(group,grids)
    # # writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    # objectives = plotJson(folder, fileName, issave=False)
    # printLog(folder, fileName, index,value,variables,objectives)
    # for irow in range(len(index)):
    #     indexAll.append(index[irow])
    #     valueAll.append(value[irow])
    #     variablesAll.append(variables[irow])
    #     objectivesAll.append(objectives[irow])
    #
    # folder,fileName = 'grid1*','taihu.json.all1'
    # plotAll(folder, fileName,indexAll,valueAll,variablesAll,objectivesAll,issave=True)
    #
    # # grid12
    # group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    # group = [
    #     0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
    #     0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5
    # ]
    # grids = [
    #     [1.0],
    #     [1.0],
    #     [0.0, 0.5, 1.0],
    #     [0.0, 0.5, 1.0],
    #     [0.0, 0.5, 1.0],
    #     [0.5]
    # ]
    # folder,fileName,pref,issm,iesm = 'grid12','taihu.json','grid',1,27
    # index,value,variables = meshgridMD(group,grids)
    # # writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    # objectives = plotJson(folder, fileName, issave=False)
    # printLog(folder, fileName, index,value,variables,objectives)
    # for irow in range(len(index)):
    #     indexAll.append(index[irow])
    #     valueAll.append(value[irow])
    #     variablesAll.append(variables[irow])
    #     objectivesAll.append(objectives[irow])
    #
    # # grid13
    # group,grids,index,value,variables,objectives = [],[],[],[],[],[]
    # group = [
    #     0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
    #     0,1,2,2,2,2,2,3,3,3,3,0,0,0,0,0,4,4,4,4,4,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5
    # ]
    # grids = [
    #     [1.0],
    #     [1.0],
    #     [0.0, 0.5, 1.0],
    #     [0.0, 0.5, 1.0],
    #     [0.0, 0.5, 1.0],
    #     [1.0]
    # ]
    # folder,fileName,pref,issm,iesm = 'grid13','taihu.json','grid',1,27
    # index,value,variables = meshgridMD(group,grids)
    # # writeJson(folder=folder,fileName=fileName,pref=pref,issm=issm,iesm=iesm)
    # objectives = plotJson(folder, fileName, issave=False)
    # printLog(folder, fileName, index,value,variables,objectives)
    # for irow in range(len(index)):
    #     indexAll.append(index[irow])
    #     valueAll.append(value[irow])
    #     variablesAll.append(variables[irow])
    #     objectivesAll.append(objectives[irow])
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


    indexAll,valueAll,variablesAll,objectivesAll = [],[],[],[]
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
    objectives = plotJson(folder, fileName, issave=False)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

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
    objectives = plotJson(folder, fileName, issave=False)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

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
    objectives = plotJson(folder, fileName, issave=False)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

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
    objectives = plotJson(folder, fileName, issave=False)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

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
    objectives = plotJson(folder, fileName, issave=False)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

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
    objectives = plotJson(folder, fileName, issave=False)
    printLog(folder, fileName, index,value,variables,objectives)
    for irow in range(len(index)):
        indexAll.append(index[irow])
        valueAll.append(value[irow])
        variablesAll.append(variables[irow])
        objectivesAll.append(objectives[irow])

    folder,fileName = 'grid2*','taihu.json.all2'
    plotAll(folder, fileName,indexAll,valueAll,variablesAll,objectivesAll,issave=True)

    from pylab import *
    from mpl_cfaces import cface
    fig = figure(figsize=(11,11))
    for i in range(30):
        ax = fig.add_subplot(6,5,i+1,aspect='equal')
        # def cface(ax, x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18):
        # x1 = height  of upper face
        # x2 = overlap of lower face
        # x3 = half of vertical size of face
        # x4 = width of upper face
        # x5 = width of lower face

        # x6 = length of nose

        # x7 = vertical position of mouth
        # x8 = curvature of mouth
        # x9 = width of mouth

        # x10 = vertical position of eyes
        # x11 = separation of eyes
        # x12 = slant of eyes
        # x13 = eccentricity of eyes
        # x14 = size of eyes

        # x15 = position of pupils

        # x16 = vertical position of eyebrows
        # x17 = slant of eyebrows
        # x18 = size of eyebrows

        # cface(ax, .9, *rand(17))
        cface(ax,
              0.9,
              0.9,
              0.3,
              0.9,
              0.9,

              1.0,

              0.6,
              0.5,
              1.0,

              0.4,
              0.6*valueAll[i][2],
              0.5*valueAll[i][3],
              0.6*valueAll[i][4],
              1.0,

              0.5*valueAll[i][5],

              0.8*valueAll[i][6],
              0.5*valueAll[i][7],
              1.0
              )
        ax.axis([-1.2,1.2,-1.2,1.2])
        ax.set_xticks([])
        ax.set_yticks([])
        title = 'GA mean '+str(objectivesAll[i][0])
        ax.text(.5,.9,title,horizontalalignment='center',transform=ax.transAxes,fontsize=10)
        fig.subplots_adjust(hspace=0, wspace=0)
    show()


    # folder,fileName = 'gridAll','taihu.json.all'
    # plotAll(folder, fileName,indexAll,valueAll,variablesAll,objectivesAll,issave=False)


    print '\nEnd'
