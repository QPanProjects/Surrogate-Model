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
import warnings
warnings.filterwarnings(action="ignore", category=Warning)

import numpy as np
from copy import deepcopy

import random
random.seed(0.5)

# from sklearn.preprocessing import StandardScaler, MinMaxScaler

sys.path.append("..")
from d3d_read_map import objfunCost

from surrogate.base import Individual
from surrogate.selection import selNSGA2, selTournamentDCD
from surrogate.crossover import cxSimulatedBinaryBounded
from surrogate.mutation import mutPolynomialBounded
from surrogate.sampling import samRandom
# from surrogate.sampling import samBeta, samUniform
# from surrogate import benchmarks
# from surrogate.estimator import ANNSurrogate
from surrogate.estimator import delft3dWAQ
from surrogate.files import jsonMOEA, decvarMOEA

from hashlib import sha1

def main(argv):
    """

    :param argv:
    :return:
    """
    # run.sh: icaseStart=1, icaseEnd=2
    # d3d_read_map.py: taihuDir, caseName, varName, iseg, itime
    # d3d_create_inp.py: blockDir, blockFname, inp00Fname, tempFname

    _Ngen = 0
    _Ndim = 0
    _Npop = 0

    _Nobj = 0
    _Ncon = 0
    CXPB = 0.0


    try:
        opts, args = getopt.getopt(argv,"hg:d:p:o:c:x:",["gen=","dim=","pop=","obj=","con=","cxpb"])
    except getopt.GetoptError:
        print sys.argv[0]+' -g <gen> -d <dim> -p <pop> -o <obj> -c <con> -x <cxpb>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print sys.argv[0]+' -g <gen> -d <dim> -p <pop> -o <obj> -c <con> -x <cxpb>'
            sys.exit()

        elif opt in ("-g", "--gen"):
            _Ngen = int(arg)
        elif opt in ("-d", "--dim"):
            _Ndim = int(arg)
        elif opt in ("-p", "--pop"):
            _Npop = int(arg)
        elif opt in ("-o", "--obj"):
            _Nobj = int(arg)
        elif opt in ("-c", "--con"):
            _Ncon = int(arg)

        elif opt in ("-x", "--cxpb"):
            CXPB = float(arg)

    print '--py:Start::['+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'] run_moea.py'

    if _Ngen > 0 and _Ndim > 0 and _Npop > 0 and _Nobj > 0 and _Ncon >= 0 and CXPB >= 0.0:
        moeaLoop(_Ngen, _Ndim, _Npop, _Nobj, _Ncon, CXPB)
    else:
        print '--py:Error:: '

    print '--py:End::  ['+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+']'


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


def Population(numPop=4, numVar=10, estimator=delft3dWAQ, weights=(-1.0, -1.0)):
    """Population

    :param numPop:
    :param numVar:
    :param estimator:
    :param weights:
    :return:
    """
    constraint = []
    Individuals = []
    variables = []
    # group,grids,index,value,variables = [],[],[],[],[]
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
    #     [1.0]
    # ]
    # index,value,variables = meshgridMD(group,grids)

    for i in range(numPop):
        # variable = variables[0]
        # variable = variables[i]

        variable = samRandom(n=numVar)
        # variable = samBeta(a=0.1, b=0.1, size=numVar)
        # variable = samUniform(low=0.0, high=1.0, size=numVar).tolist()

        # print '--py:Test::\t[' + ','.join(map("{:.5f}".format, variable)) + '],'
        Individuals.append(Individual(estimator=estimator, variable=variable, constraint=constraint, weights=weights))
    return Individuals


def delwaq(caseDir, casePref, icaseStart=99999999, icaseEnd=99999999, icase=0):
    print ''
    print '--py:Start::['+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'] os.system('+str(icaseStart)+' '+str(icaseEnd)+'), icase: '+str(icase)+''

    os.system('./run.sh '+str(icaseStart)+' '+str(icaseEnd)+' '+caseDir+' '+casePref)

    caseName = casePref+"%08d" % icaseStart
    objfunFname = '/var/www/html/taihu'+'/'+caseDir+'/'+caseName+'/taihu_objfun.txt'
    with open(objfunFname, 'r') as objfunFref:
        # 20171110 before, without cost
        # [obj1, obj2, iseg, itime] = [float(elt.strip()) for elt in objfunFref.readline().split('\t')]
        # 20171110, with cost
        [obj1, obj2, obj3, iseg, itime] = [float(elt.strip()) for elt in objfunFref.readline().split('\t')]

    print '--py:End::  ['+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'] os.system('+str(obj1)+' '+str(obj2)+'), icase: '+str(icase)+''
    print ''

    # 20171110 before, without cost
    # return obj1,obj2
    # 20171110, with cost
    return obj1,obj2,obj3


def getSSD(scaler,variable,x_ssd_1,factor=0.5):
    numPop = len(variable)
    numVar = len(variable[0])

    # sd = np.sum(np.std(variable, axis=1))/float(numPop)
    sd = np.sum(np.std(scaler.transform(variable), axis=1))/float(numPop)

    ssd = x_ssd_1[3]+factor*(sd-x_ssd_1[3])
    s = ssd/x_ssd_1[3]*x_ssd_1[1]
    n = int(s*numPop)

    return [n,s,sd,ssd]

def moeaLoop(_Ngen, _Ndim, _Npop, _Nobj, _Ncon, CXPB):
    # # --sh:[icaseStart = 1, icaseEnd = 2] => [t00000001, t00000002]
    # os.system('./run.sh '+str(icaseStart)+' '+str(icaseEnd))
    #
    # createdir     "$casedir"
    # createD3Dinp  "$blockdir" "$blockfname" "$decvarfname" "$inp00fname" "$tempfname"
    # copyfile      "$decvarfname" "$casedir/taihu_decvvar.txt"
    # movefile      "$tempfname" "$inpfname"
    # rundelwaq     "$exedelwaqdir" "$casedir" "$inpfname" "$bloomfname" "$procfname"
    print '--py:MOEA:: Init moeaLoop('+str(_Ngen)+', '+str(_Ndim)+', '+str(_Npop)+', '+str(_Nobj)+', '+str(_Ncon)+', '+str(CXPB)+')'

    jsonFname = 'result/moea/taihu.json'
    varDir = 'deltemp'
    caseDir  = 'result'
    casePref = 'moea'

    _INF = 1e-14
    weights = (-1.0, -1.0)

    print '--py:MOEA:: Init estimator'
    estimator = delft3dWAQ
    # estimator = benchmarks.zdt3
    # os.system('./run.sh '+str(icaseStart)+' '+str(icaseEnd))

    # print '--py:MOEA:: Init ANNSurrogate'
    # # import sklearn
    # # # print('The scikit-learn version is {}.'.format(sklearn.__version__))
    # # # surrogate = ANNSurrogate(algorithm='lbfgs', alpha=1e-5, hidden_layer_sizes=(8), random_state=1)
    # surrogate = ANNSurrogate(algorithm='lbfgs', activation='relu', hidden_layer_sizes=(70), batch_size=10, random_state=5)
    # import cPickle as pickle
    # surrogate = pickle.load(open('/var/www/html/taihu/mlmodel/d3d_ann_moea.pkl', 'rb'))
    # # surrogate.fit(X_train, Y_train)
    # # surrogate = ANNSurrogate(algorithm='sgd', alpha=1e-5, hidden_layer_sizes=(8), random_state=1)
    # # surrogate.partial_fit(X_train, Y_train)
    """algorithm => solver"""

    """
    0.*.* init size of training dataset
    1.*.* igen = 0
    2.*.* igen in range[1, _Ngen]

    *.1.* initiate X
        0   Xold_ind
        1   Xnew_ind
    *.2.* predict
        0   delwaq
        1   ann
        2   updated ann
    *.3.* set Y
        0   Yold_obj
        1   Ynew_obj
    *.4.* print
        0   Xold_ind, Yold_obj
        1   Xnew_ind, Ynew_obj
    """

    """0.1.0"""
    Xold_ind, Yold_obj = np.zeros([_Npop, _Ndim]), np.zeros([_Npop, _Nobj])
    """0.1.1
    ANGA needs to initiate step: 1.1.1 and 1.3.1
    """
    # Xnew_ind, Ynew_obj = [], []
    """0.1.2
    ANGA needs to initiate step: 1.1.1 and 1.3.1
    ANGA needs to be updated by new training dataset
    """
    # Xnew_ind, Ynew_obj > [_Npop, _Ndim], [_Npop, _Nobj]
    Xnew_ind, Ynew_obj = [], []
    # hash table
    # print(sha1(np.reshape([X for X in [0.1,0.2,0.3]],(1,-1))).hexdigest())
    Htbl_Xnew_ind, Htbl_Ynew_obj = [], []
    ipop_new = 0

    X_n0, X_S0, X_SD0, X_SSD0 = _Npop, 1.0, 0.0, 1.0

    """objtype: 12.obj12; 13.obj13; 23.obj23"""
    if _Nobj == 1:
        weights = (-1.0, -1.0)
        objtype = 1
        # objtype = 2
        # objtype = 3
    elif _Nobj == 2:
        weights = (-1.0, -1.0)
        # objtype = 12
        # objtype = 13
        objtype = 23
    elif _Nobj == 3:
        weights = (-1.0, -1.0, -1.0)
        objtype = 123
    else:
        weights = (-1.0, -1.0)
        objtype = 12
    # print str(objtype)

    # TODO NSGA2-0 initiate
    igen = 0
    print '\n'
    print '--py:MOEA:: ['+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'] Gen: ' + str(igen)
    population = Population(numPop=_Npop, numVar=_Ndim, estimator=estimator, weights=weights)

    ioDecVarFile = decvarMOEA(varDir=varDir, casePref=casePref, numVar=_Ndim, numPop=_Npop, numCon=_Ncon, numObj=_Nobj, numGen=_Ngen)
    ioResultFile = jsonMOEA(fileName=jsonFname, numVar=_Ndim, numPop=_Npop, numCon=_Ncon, numObj=_Nobj, numGen=_Ngen)
    ioResultFile.writeHeader()


    # TODO NSGA2-1 delwaq or ann
    print '--py:MOEA::\tDecision Variable'
    ioDecVarFile.writeHeader(igen=igen)
    icaseStart = ioDecVarFile.icase + 1
    for ipop in range(_Npop):
        """1.1.0-initiate training dataset: Xold_ind"""
        Xold_ind[ipop] = [deepcopy(X) for X in population[ipop].variable]
        # TODO 20170203 test set ipop == 0 : DecVar = 0.0
        # if ipop == 0:
        #     Xold_ind[ipop] = Xold_ind[ipop]*0.0
        ioDecVarFile.writeDecVar(variable=Xold_ind[ipop], ipop=ipop)
    ioDecVarFile.writeEnd()
    icaseEnd = ioDecVarFile.icase
    # print '--py:MOEA:: icase\tStart['+str(_Npop)+'*'+str(igen)+'+1]: '+str(icaseStart)+'\tEnd['+str(_Npop)+'*('+str(igen)+'+1)]: '+str(icaseEnd)
    print '--py:MOEA::\tFitness Variable'
    for ipop in range(_Npop):
        issm = icaseStart+ipop
        iesm = icaseStart+ipop
        # print str(ipop)+'\t=========='
        """1.2.0-predict by delwaq with cost"""
        obj1,obj2,obj3 = delwaq(caseDir=caseDir, casePref=casePref, icaseStart=issm, icaseEnd=iesm, icase=ipop)
        """1.2.1-predict by ann and calculate cost"""
        # [obj1,obj2] = [deepcopy(Y) for Y in surrogate.predict(np.reshape(Xold_ind[ipop],(1,-1)))[0]]
        # obj3 = objfunCost("deltemp/moea%08i.txt" % issm)
        """1.3.0-set training dataset: Yold_obj"""
        if objtype==1:
            population[ipop].fitness.values = [deepcopy(Y) for Y in [obj1]]
        if objtype==2:
            population[ipop].fitness.values = [deepcopy(Y) for Y in [obj2]]
        if objtype==3:
            population[ipop].fitness.values = [deepcopy(Y) for Y in [obj3]]
        if objtype==12:
            population[ipop].fitness.values = [deepcopy(Y) for Y in [obj1,obj2]]
        if objtype==13:
            population[ipop].fitness.values = [deepcopy(Y) for Y in [obj1,obj3]]
        if objtype==23:
            population[ipop].fitness.values = [deepcopy(Y) for Y in [obj2,obj3]]
        if objtype==123:
            population[ipop].fitness.values = [deepcopy(Y) for Y in [obj1, obj2,obj3]]
        Yold_obj[ipop] = [deepcopy(Y) for Y in population[ipop].fitness.values]
        """1.4.0-print result training dataset: Xold_ind, Yold_obj"""
        # print '\tXold_ind: [' + '\t'.join(map("{:.5f}".format, Xold_ind[ipop])) + ']' \
        #     + '\n\tMean_X: ' + str(np.mean(Xold_ind[ipop])) \
        #     + '\n\tStd_X: ' + str(np.std(Xold_ind[ipop])) \
        #     + '\n\tYold_obj: [' + '\t'.join(map("{:.5f}".format, Yold_obj[ipop])) + ']'


    # # TODO ANGA-1.0 initiation, NSGA2_igen=0
    # print '--py:ANGA::\tDecision Variable'
    # X_scaler = StandardScaler()
    # # X_scaler = MinMaxScaler()
    # X_scaler.fit(Xold_ind)
    # # # print(X_scaler.mean_)
    # # # print(X_scaler.var_)
    # X_n0 = _Npop
    # X_S0 = 1.0
    # X_SD0 = 1.0
    # # # X_SD0 = np.sum(np.std(Xold_ind, axis=1))/float(_Npop)
    # # X_SD0 = np.sum(np.std(X_scaler.transform(Xold_ind), axis=1))/float(_Npop)
    # # # X_scaler.fit(np.transpose(Xold_ind))
    # # # X_SD0 = np.sum(np.std(X_scaler.transform(np.transpose(Xold_ind)), axis=0))/float(_Npop)
    # X_SSD0 = X_SD0
    # X_SSD = [[X_n0, X_S0, X_SD0, X_SSD0]]
    # print str(igen)+'\tX_SSD: [' + '\t'.join(map("{:.5f}".format, X_SSD[igen])) + ']'
    #
    # print '--py:ANGA::\tSurrogate Model'
    # # surrogate.fit(Xold_ind, Yold_obj)
    # # surrogate.partial_fit(Xold_ind, Yold_obj)
    # print '--py:ANGA::\tSurrogate Model'
    # surrogate.fit(X_scaler.transform(Xold_ind), Yold_obj)
    # # surrogate.partial_fit(X_scaler.transform(Xold_ind), Yold_obj)
    #
    # print '--py:ANGA::\tFitness Variable'
    # for ipop in range(_Npop):
    #     # print str(ipop)+'\t=========='
    #     """1.1.1-initiate training dataset: Xnew_ind"""
    #     # Xnew_ind.append([deepcopy(X) for X in samBeta(a=0.1, b=0.1, size=_Ndim)])
    #     Xnew_ind.append([deepcopy(X) for X in Xold_ind[ipop]])
    #     """1.2.1-predict by ann and calculate cost"""
    #     [obj1,obj2] = [deepcopy(Y) for Y in surrogate.predict(np.reshape(Xnew_ind[ipop],(1,-1)))[0]]
    #     # [obj1,obj2] = [deepcopy(Y) for Y in surrogate.predict(X_scaler.transform(np.reshape(Xnew_ind[ipop],(1,-1))))[0]]
    #     obj3 = objfunCost("deltemp/moea%08i.txt" % issm)
    #     """1.3.1-set training dataset: Ynew_obj"""
    #     if objtype==1:
    #         Ynew_obj.append([deepcopy(Y) for Y in [obj1]])
    #     if objtype==2:
    #         Ynew_obj.append([deepcopy(Y) for Y in [obj2]])
    #     if objtype==3:
    #         Ynew_obj.append([deepcopy(Y) for Y in [obj3]])
    #     if objtype==12:
    #         Ynew_obj.append([deepcopy(Y) for Y in [obj1,obj2]])
    #     if objtype==13:
    #         Ynew_obj.append([deepcopy(Y) for Y in [obj1,obj3]])
    #     if objtype==23:
    #         Ynew_obj.append([deepcopy(Y) for Y in [obj2,obj3]])
    #     if objtype==123:
    #         Ynew_obj.append([deepcopy(Y) for Y in [obj1, obj2,obj3]])
    #     """1.4.1-print result training dataset: Xnew_ind, Ynew_obj"""
    #     # print '\tXnew_ind: [' + '\t'.join(map("{:.5f}".format, Xnew_ind[ipop])) + ']' \
    #     #     + '\n\tMean_X: ' + str(np.mean(Xnew_ind[ipop])) \
    #     #     + '\n\tStd_X: ' + str(np.std(Xnew_ind[ipop])) \
    #     #     + '\n\tYnew_obj: [' + '\t'.join(map("{:.5f}".format, Ynew_obj[ipop])) + ']'
    #     """1.5.1-hash table: Htbl_Xnew_ind, Htbl_Ynew_obj"""
    #     Htbl_Xnew_ind.append(sha1(np.reshape(Xold_ind[ipop],(1,-1))).hexdigest())
    #     Htbl_Ynew_obj.append(sha1(np.reshape(Yold_obj[ipop],(1,-1))).hexdigest())
    #     # print '\tHtbl_Xnew_ind: [' + Htbl_Xnew_ind[ipop] + ']' \
    #     #     + '\n\tHtbl_Ynew_obj: [' + Htbl_Ynew_obj[ipop] + ']'


    # TODO NSGA2-2 main loop, NSGA2_igen>0
    print '--py:MOEA::\tNSGA2 Selection'
    population = selNSGA2(population, _Npop)
    ioResultFile.writePareto(individuals=population, igen=igen)
    # print str(igen) + '\tGen:'
    # for ipop in population:
    #     print '\tpopulation.sel.a'\
    #           + '\tvar1: [' + ', '.join(map("{:.5f}".format, ipop.variable)) + ']'
    # print
    for igen in range(1, _Ngen):
        # TODO NSGA2-2.1 offspring
        print '\n'
        print '--py:MOEA:: ['+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'] Gen: ' + str(igen)
        # print '\n' + str(igen) + '\tGen:'
        # for ipop in population:
        #     print '\tpopulation.sel.b'\
        #           + '\tvar: [' + ', '.join(map("{:.5f}".format, ipop.variable)) + ']'\
        #           + '\tobj: [' + ', '.join(map("{:.5f}".format, ipop.fitness.values)) + ']'\
        #           + '\tcrw: [' + str(ipop.fitness.crowding_dist) + ']'
        print '--py:MOEA::\tNSGA2 Tournament'
        offspring = selTournamentDCD(population, _Npop)
        # for ipop in offspring:
        #     print '\toffspring.sel.a'\
        #           + '\tvar: [' + ', '.join(map("{:.5f}".format, ipop.variable)) + ']'\
        #           + '\tobj: [' + ', '.join(map("{:.5f}".format, ipop.fitness.values)) + ']'\
        #           + '\tcrw: [' + str(ipop.fitness.crowding_dist) + ']'
        # print
        print '--py:MOEA::\tNSGA2 Offspring'
        offspring = [deepcopy(ind) for ind in offspring]
        # for ipop in offspring:
        #     print '\toffspring.sel.a'\
        #           + '\tvar: [' + ', '.join(map("{:.5f}".format, ipop.variable)) + ']'\
        #           + '\tobj: [' + ', '.join(map("{:.5f}".format, ipop.fitness.values)) + ']'\
        #           + '\tcrw: [' + str(ipop.fitness.crowding_dist) + ']'
        # print
        print '--py:MOEA::\tCrossover of offspring with CXPB: '+str(CXPB)
        for ind1, ind2 in zip(offspring[::2], offspring[1::2]):
            if random.random() <= CXPB:
                # print '\toffspring.cx.b'\
                #       + '\tvar1: [' + ', '.join(map("{:.5f}".format, ind1.variable)) + ']'\
                #       + '\tvar2: [' + ', '.join(map("{:.5f}".format, ind2.variable)) + ']'
                ind1.variable, ind2.variable = cxSimulatedBinaryBounded(ind1.variable, ind2.variable)
                # print '\toffspring.cx.a'\
                #       + '\tvar1: [' + ', '.join(map("{:.5f}".format, ind1.variable)) + ']'\
                #       + '\tvar2: [' + ', '.join(map("{:.5f}".format, ind2.variable)) + ']'
            # print '\toffspring.mut.b'\
            #       + '\tvar1: [' + ', '.join(map("{:.5f}".format, ind1.variable)) + ']'\
            #       + '\tvar2: [' + ', '.join(map("{:.5f}".format, ind2.variable)) + ']'
            ind1.variable = mutPolynomialBounded(ind1.variable)
            ind2.variable = mutPolynomialBounded(ind2.variable)
            # print '\toffspring.mut.a'\
            #       + '\tvar1: [' + ', '.join(map("{:.5f}".format, ind1.variable)) + ']'\
            #       + '\tvar2: [' + ', '.join(map("{:.5f}".format, ind2.variable)) + ']'
            # print
            del ind1.fitness.values, ind2.fitness.values
        print '--py:MOEA::\tEvaluate the individuals with an invalid fitness'
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]


        # TODO NSGA2-2.2 delwaq or ann
        print '--py:MOEA::\tDecision Variable'
        ioDecVarFile.writeHeader(igen=igen)
        icaseStart = ioDecVarFile.icase + 1
        ipop = 0
        for ind in invalid_ind:
            """2.1.0-initiate training dataset: Xold_ind"""
            Xold_ind[ipop] = [deepcopy(X) for X in ind.variable]
            ioDecVarFile.writeDecVar(variable=Xold_ind[ipop], ipop=ipop)
            ipop += 1
        ioDecVarFile.writeEnd()
        icaseEnd = ioDecVarFile.icase
        # print '--py:MOEA:: icase\tStart['+str(_Npop)+'*'+str(igen)+'+1]: '+str(icaseStart)+'\tEnd['+str(_Npop)+'*('+str(igen)+'+1)]: '+str(icaseEnd)
        # TODO ANGA-1.1 delwaq or ann by sampling rate
        print '--py:MOEA::\tFitness Variable'
        ipop = 0
        for ind in invalid_ind:
            issm = icaseStart+ipop
            iesm = icaseStart+ipop
            # ind.fitness.values = estimator(ind.variable)
            # print str(ipop)+'\t=========='
            """2.2.0-predict by delwaq with cost"""
            obj1,obj2,obj3 = delwaq(caseDir=caseDir, casePref=casePref, icaseStart=issm, icaseEnd=iesm, icase=ipop)
            """2.2.1-predict by ann and calculate cost"""
            # [obj1,obj2] = [deepcopy(Y) for Y in surrogate.predict(np.reshape(Xold_ind[ipop],(1,-1)))[0]]
            # obj3 = objfunCost("deltemp/moea%08i.txt" % issm)
            """2.3.0-set training dataset: Yold_obj"""
            if objtype==1:
                ind.fitness.values = [deepcopy(Y) for Y in [obj1]]
            if objtype==2:
                ind.fitness.values = [deepcopy(Y) for Y in [obj2]]
            if objtype==3:
                ind.fitness.values = [deepcopy(Y) for Y in [obj3]]
            if objtype==12:
                ind.fitness.values = [deepcopy(Y) for Y in [obj1,obj2]]
            if objtype==13:
                ind.fitness.values = [deepcopy(Y) for Y in [obj1,obj3]]
            if objtype==23:
                ind.fitness.values = [deepcopy(Y) for Y in [obj2,obj3]]
            if objtype==123:
                ind.fitness.values = [deepcopy(Y) for Y in [obj1, obj2,obj3]]
            Yold_obj[ipop] = [deepcopy(Y) for Y in ind.fitness.values]
            """2.4.0-print result training dataset: Xold_ind, Yold_obj"""
            # print '\tXold_ind: [' + '\t'.join(map("{:.5f}".format, Xold_ind[ipop])) + ']' \
            #     + '\n\tMean_X: ' + str(np.mean(Xold_ind[ipop])) \
            #     + '\n\tStd_X: ' + str(np.std(Xold_ind[ipop])) \
            #     + '\n\tYold_obj: [' + '\t'.join(map("{:.5f}".format, Yold_obj[ipop])) + ']'
            ipop += 1

        # # TODO 20170105 ANGA test
        # ipop = 0
        # for ind in invalid_ind:
        #     issm = icaseStart+ipop
        #     iesm = icaseStart+ipop
        #     # ind.fitness.values = estimator(ind.variable)
        #     """2.1.1-initiate training dataset: Xnew_ind"""
        #     Xnew_ind[ipop] = [deepcopy(X) for X in ind.variable]
        #     """2.2.1-predict by ann and calculate cost"""
        #     [obj1,obj2] = [deepcopy(Y) for Y in surrogate.predict(np.reshape(Xnew_ind[ipop],(1,-1)))[0]]
        #     # [obj1,obj2] = [deepcopy(Y) for Y in surrogate.predict(X_scaler.transform(np.reshape(Xnew_ind[ipop],(1,-1))))[0]]
        #     obj3 = objfunCost("deltemp/moea%08i.txt" % issm)
        #     """2.3.1-initiate training dataset: Ynew_obj"""
        #     if objtype==1:
        #         Ynew_obj[ipop] = [deepcopy(Y) for Y in [obj1]]
        #     if objtype==2:
        #         Ynew_obj[ipop] = [deepcopy(Y) for Y in [obj2]]
        #     if objtype==3:
        #         Ynew_obj[ipop] = [deepcopy(Y) for Y in [obj3]]
        #     if objtype==12:
        #         Ynew_obj[ipop] = [deepcopy(Y) for Y in [obj1,obj2]]
        #     if objtype==13:
        #         Ynew_obj[ipop] = [deepcopy(Y) for Y in [obj1,obj3]]
        #     if objtype==23:
        #         Ynew_obj[ipop] = [deepcopy(Y) for Y in [obj2,obj3]]
        #     if objtype==123:
        #         Ynew_obj[ipop] = [deepcopy(Y) for Y in [obj1, obj2,obj3]]
        #     """2.4.1-print result training dataset: Xnew_ind, Ynew_obj"""
        #     print '\t' + str(ipop) \
        #           + '\tXnew_ind: [' + '\t'.join(map("{:.5f}".format, Xnew_ind[ipop])) + ']' \
        #           + '\tMean_X: ' + str(np.mean(Xnew_ind[ipop])) \
        #           + '\tStd_X: ' + str(np.std(Xnew_ind[ipop])) \
        #           + '\tYnew_obj: [' + '\t'.join(map("{:.5f}".format, Ynew_obj[ipop])) + ']'
        #     ipop += 1

        # # TODO ANGA-2 main, NSGA2_igen>0
        # # implement fitness sampling rate & retraining ANN from anga [py:function:: estimator()]
        # # Important: size Xnew_ind, Ynew_obj > [_Npop, _Ndim], [_Npop, _Nobj]
        # #
        # # find in varaible pool (cache)?
        # #     <Yes> retreive fitness from cache
        # #         Ynew_obj = ind.fitness.values
        # #         ind.fitness.values = Ynew_obj[0]
        # #     <No > model [estimator()]?
        # #         <Yes> model [estimator()]
        # #           ind.fitness.values = estimator(ind.variable)
        # #           <> update cache and training set of ANN
        # #           # Xold_ind[ipop] = [deepcopy(X) for X in ind.variable]
        # #           # Yold_obj = ind.fitness.values
        # #         <No > predict by ANN [ANN.predict()]
        # #           Ynew_obj = surrogate.predict(X_scaler.transform(Xnew_ind))
        # #           ind.fitness.values = Ynew_obj[0]
        # #
        # # retraining [ANN.fit()]?
        # #     <Yes> surrogate.fit(X_scaler.transform(Xold_ind), Yold_obj)
        # #     <No > ind.fitness.values = ind.fitness.values
        # # TODO ANG-2.1 sampling rate
        # print '--py:ANGA::\tUpdate Decision Variable and Fitness Variable'
        # X_SSD.append(getSSD(scaler=X_scaler,variable=Xold_ind,x_ssd_1=X_SSD[igen-1]))
        # print str(igen)+'\tX_SSD: [' + '\t'.join(map("{:.5f}".format, X_SSD[igen])) + ']'
        # ipop = 0
        # for ind in invalid_ind:
        #     # TODO ANGA-2.2 update retraining pool
        #     # print str(ipop)+'\t=========='
        #     """2.1.2-initiate updated training dataset: Xnew_ind, Ynew_obj"""
        #     if sha1(np.reshape(ind.variable,(1,-1))).hexdigest() in Htbl_Xnew_ind:
        #         print str(ipop_new)+'\t=========='
        #         Xnew_ind.append(ind.variable)
        #         Ynew_obj.append(ind.fitness.values)
        #         print '\tXnew_ind: [' + '\t'.join(map("{:.5f}".format, Xnew_ind[_Npop+ipop_new])) + ']' \
        #             + '\n\tMean_X: ' + str(np.mean(Xnew_ind[_Npop+ipop_new])) \
        #             + '\n\tStd_X: ' + str(np.std(Xnew_ind[_Npop+ipop_new])) \
        #             + '\n\tYnew_obj: [' + '\t'.join(map("{:.5f}".format, Ynew_obj[_Npop+ipop_new])) + ']'
        #         ipop_new += 1
        #     # TODO ANGA-2.3 update ANNSurrogate
        #     """2.2.2-predict by updated ann and calculate cost"""
        #     """2.2.2.a-update ann"""
        #     # surrogate.fit(Xnew_ind, Ynew_obj)
        #     # surrogate.partial_fit(Xnew_ind, Ynew_obj)
        #     # # surrogate.fit(X_scaler.transform(Xnew_ind), Ynew_obj)
        #     # # surrogate.partial_fit(X_scaler.transform(Xnew_ind), Ynew_obj)
        #     """2.2.2.b-predict by updated ann"""
        #     # [obj1,obj2] = [deepcopy(Y) for Y in surrogate.predict(np.reshape(Xnew_ind[_Npop+ipop_new],(1,-1)))[0]]
        #     # # [obj1,obj2] = [deepcopy(Y) for Y in surrogate.predict(X_scaler.transform(np.reshape(Xnew_ind[_Npop+ipop_new],(1,-1))))[0]]
        #     """2.2.2.c-calculate cost"""
        #     # obj3 = objfunCost(Xnew_ind[_Npop+ipop_new])
        #     """2.3.2-initiate updated training dataset: Ynew_obj"""
        #     # if objtype==1:
        #     #     Ynew_obj[_Npop+ipop_new] = [deepcopy(Y) for Y in [obj1]]
        #     # if objtype==2:
        #     #     Ynew_obj[_Npop+ipop_new] = [deepcopy(Y) for Y in [obj2]]
        #     # if objtype==3:
        #     #     Ynew_obj[_Npop+ipop_new] = [deepcopy(Y) for Y in [obj3]]
        #     # if objtype==12:
        #     #     Ynew_obj[_Npop+ipop_new] = [deepcopy(Y) for Y in [obj1,obj2]]
        #     # if objtype==13:
        #     #     Ynew_obj[_Npop+ipop_new] = [deepcopy(Y) for Y in [obj1,obj3]]
        #     # if objtype==23:
        #     #     Ynew_obj[_Npop+ipop_new] = [deepcopy(Y) for Y in [obj2,obj3]]
        #     # if objtype==123:
        #     #     Ynew_obj[_Npop+ipop_new] = [deepcopy(Y) for Y in [obj1, obj2,obj3]]
        #     # TODO ANGA-2.4 update fitness.values
        #     # ind.fitness.values = [deepcopy(Y) for Y in Ynew_obj[_Npop+ipop_new]]
        #     """2.4.2-print updated result training dataset: Xnew_ind, Ynew_obj"""
        #     # print '\tXnew_ind: [' + '\t'.join(map("{:.5f}".format, Xnew_ind[ipop])) + ']' \
        #     #     + '\n\tMean_X: ' + str(np.mean(Xnew_ind[ipop])) \
        #     #     + '\n\tStd_X: ' + str(np.std(Xnew_ind[ipop])) \
        #     #     + '\n\tYnew_obj: [' + '\t'.join(map("{:.5f}".format, Ynew_obj[ipop])) + ']'
        #     ipop += 1
        #     # TODO ANGA-2.5 empty retraining pool


        # TODO NSGA2-3 Pareto Front
        print '--py:MOEA::\tNSGA2 Selection'
        # print 'Select the next generation population\nAfter cx mut'
        # for ipop in population:
        #     print '\tpopulation.sel.b'\
        #           + '\tvar: [' + ', '.join(map("{:.5f}".format, ipop.variable)) + ']'\
        #           + '\tobj: [' + ', '.join(map("{:.5f}".format, ipop.fitness.values)) + ']'\
        #           + '\tcrw: [' + str(ipop.fitness.crowding_dist) + ']'
        # for ipop in offspring:
        #     print '\toffspring.sel.b'\
        #           + '\tvar: [' + ', '.join(map("{:.5f}".format, ipop.variable)) + ']'\
        #           + '\tobj: [' + ', '.join(map("{:.5f}".format, ipop.fitness.values)) + ']'\
        #           + '\tcrw: [' + str(ipop.fitness.crowding_dist) + ']'
        # print
        population = selNSGA2(population + offspring, _Npop)
        ioResultFile.writePareto(individuals=population, igen=igen)
        # for ipop in range(_Npop):
        #     print '\tpopulation.sel.a' \
        #           + '\tXold_ind: [' + ', '.join(map("{:.5f}".format, population[ipop].variable)) + ']'\
        #           + '\tYold_obj: [' + ', '.join(map("{:.5f}".format, population[ipop].fitness.values)) + ']'\
        #           + '\tcrw: [' + str(population[ipop].fitness.crowding_dist) + ']'

        # for ipop in range(_Npop):
        #     population[ipop].objective = population[ipop].estimator(population[ipop].variable)
        #
        #     Xold_ind.append(population[ipop].variable)
        #     Yold_obj.append(population[ipop].objective)
        #
        #     print '\t' + str(ipop) \
        #           + '\tXold_ind: [' + ', '.join(map("{:.5f}".format, population[ipop].variable)) + ']'\
        #           + '\tMean_X: ' + str(np.mean(population[ipop].variable))\
        #           + '\tStd_X: ' + str(np.std(population[ipop].variable))\
        #           + '\tYold_obj: [' + ', '.join(map("{:.5f}".format, population[ipop].objective)) + ']'
        #
        # surrogate.fit(X_scaler.transform(Xold_ind), Yold_obj)
        # # surrogate.partial_fit(X_scaler.transform(Xold_ind), Yold_obj)
        # Ynew_obj = surrogate.predict(Xnew_ind)
        # print 'ANNSurrogate.Xnew_ind:\n\t[' + '\t'.join(map(str, Xnew_ind)) + ']'
        # print 'ANNSurrogate.Ynew_obj:\n\t[' + '\t'.join(map(str, Ynew_obj)) + ']'


    # TODO NSGA2-4 end loop
    ioResultFile.writeEnd()
    ioResultFile.savePlot()
    # ioResultFile.plot_json()


if __name__ == "__main__":
    print "=================================================="
    print "==                                              =="
    print "==   Project:  Surrogate Model                  =="
    print "==   File:     run_moea.py                      =="
    print "==                                              =="
    print "==   Author:   Quan Pan                         =="
    print "==   Email:    quanpan302@hotmail.com           =="
    print "==                                              =="
    print "==   License:  MIT License                      =="
    print "==   Create:   2016-12-02                       =="
    print "==                                              =="
    print "=================================================="

    # python run_sm.py -g 10 -d 100 -p 40 -o 2 -c 0 -x 0.9 2>&1

    # icaseStart = 1
    # icaseEnd = 2
    # os.system('./run.sh '+str(icaseStart)+' '+str(icaseEnd))

    main(sys.argv[1:])
