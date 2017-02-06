# Author: Quan Pan <quanpan302@hotmail.com>
# License: MIT License
# Create: 2016-12-02

# 0 --py:Success::
# 1 --py:Warning::
# 2 --py:Error::
# --py:Start::['+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+']
# --py:End::  ['+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+']
# --py:Test::

"""
decvar-MOEA class for save MOEA Decision Variables into json file format.
"""

import os, json

import numpy as np

class decvarMOEA(object):

    def __init__(self, varDir, casePref, numVar, numPop, numCon, numObj, numGen):
        """

        :param varDir:
        :param casePref: 't' for 'test'
        :param numVar:
        :param numPop:
        :param numCon:
        :param numObj:
        :param numGen:
        :return:
        """
        # # Method 1
        # # fileName = 'variable/surrogate'/g00000000_dv.json
        # self.fileName = self.varDir + '/' + "g%08d" % igen + self.fileExt
        # self.varDir = varDir
        # self.casePref = casePref
        # self.icase = 0
        # self.fileExt = '_dv.json'
        # self.fileName = ''

        # # Method 2
        # fileName = 'variable/surrogate'/'t'00000001.txt
        self.varDir = varDir
        self.casePref = casePref
        self.icase = 0
        self.fileExt = '.txt'
        self.fileName = ''

        self.numPop = numPop
        self.numVar = numVar
        self.numCon = numCon
        self.numObj = numObj
        self.numGen = numGen


    def writeHeader(self, igen):
        """

        :return:
        """
        # # Method 1
        # self.fileName = self.varDir + '/' + "g%08d" % igen + self.fileExt
        # print '--py:Test:: ' + 'decvarMOEA.writeHeader( Gen: '+str(igen)+' ) '+self.fileName
        #
        # outFile = open(self.fileName, "wt")
        # outFile.write("{\n")
        # outFile.write("\"variable\":[\n")
        # outFile.close()

        # # Method 2
        pass

    def writeEnd(self):
        """

        :return:
        """
        # # Method 1
        # outFile = open(self.fileName, "a")
        # outFile.write("]\n}\n")
        # outFile.close()

        # # Method 2
        pass

    def writeDecVar(self, variable, ipop):
        """

        :param variable:
        :param igen:
        :return:
        """
        # # Method 1
        # self.icase += 1
        # caseName = self.casePref+"%08d" % self.icase
        #
        # outFile = open(self.fileName, "a")
        # outFile.write("  { \""+caseName+"\" : ["+','.join(map("{:.5f}".format, variable))+"] }")
        # if ipop < self.numPop - 1:
        #     outFile.write(",")
        # outFile.write("\n")
        # outFile.close()

        # # Method 2
        self.icase += 1
        self.fileName = self.varDir + '/' + self.casePref+"%08d" % self.icase+self.fileExt
        print '--py:Test:: ' + 'decvarMOEA.writeHeader( Pop: '+str(ipop)+' ) '+self.fileName

        outFile = open(self.fileName, "wt")
        outFile.write('\t'.join(map("{:.5f}".format, variable)))
        outFile.write("\n")
        outFile.close()
