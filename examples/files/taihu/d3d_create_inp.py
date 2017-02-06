#!/usr/bin/python

# Author: Quan Pan <quanpan302@hotmail.com>
# License: MIT License
# Create: 2016-12-02

# 0 --py:Success::
# 1 --py:Warning::
# 2 --py:Error::
# --py:Start::['+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+']
# --py:End::  ['+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+']
# --py:Test::

import os, sys, getopt, datetime
import warnings
warnings.filterwarnings(action="ignore", category=Warning)

import re

# def main(blockDir, blockFname, decvarFname, inp00Fname, tempFname):

def main(argv):
    """

    :param argv:
    :return:
    """
    blockDir    = ''
    blockFname  = ''
    decvarFname = ''
    inp00Fname  = ''
    tempFname   = ''
    try:
        opts, args = getopt.getopt(argv,"hd:b:v:i:t:",["dir=","block=","variable=","input=","temporary="])
    except getopt.GetoptError:
        print sys.argv[0]+' -d <dir> -b <block> -v <variable> -i <input> -t <temporary>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print sys.argv[0]+' -d <dir> -b <block> -v <variable> -i <input> -t <temporary>'
            sys.exit()
        elif opt in ("-d", "--dir"):
            blockDir = arg
        elif opt in ("-b", "--block"):
            blockFname = arg
        elif opt in ("-v", "--variable"):
            decvarFname = arg
        elif opt in ("-i", "--input"):
            inp00Fname = arg
        elif opt in ("-t", "--temporary"):
            tempFname = arg

    print '--py:Start::['+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'] '+tempFname

    if blockDir and blockFname and decvarFname and inp00Fname and tempFname:
        writeTempFile(blockDir, blockFname, decvarFname, inp00Fname, tempFname)

    print '--py:End::  ['+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'] '+tempFname


def writeTempFile(blockDir, blockFname, decvarFname, inp00Fname, tempFname):
    """

    :param blockDir:
    :param blockFname:
    :param decvarFname:
    :param inp00Fname:
    :param tempFname:
    :return:
    """
    # print '--py:Test:: blockDir   : '+blockDir
    # print '--py:Test:: blockFname : '+blockFname
    # print '--py:Test:: decvarFname: '+decvarFname
    # print '--py:Test:: inp00Fname : '+inp00Fname
    # print '--py:Test:: tempFname  : '+tempFname

    #
    # Header, list of input points
    #
    strInputH = ""
    strInputH += "  %i ; number of waste loads/continuous releases\r\n"
    strInputL = ""
    strInputL += "  %i '%i (%i) %s' ' ' ' '\r\n"
    # index id num name
    # print strInputL % (15311,1,1,'Tai')


    #
    # Block-5 col, block header of input points
    #
    strInputB5 = ""
    strInputB5 += "; Data for '%s'\r\n"
    strInputB5 += "ITEM\r\n"
    strInputB5 += " '%i (%i) %s'\r\n"
    strInputB5 += "CONCENTRATIONS\r\n"
    strInputB5 += "   USEFOR 'FLOW' 'FLOW'\r\n"
    strInputB5 += "   USEFOR 'NO3' 'NO3'\r\n"
    strInputB5 += "   USEFOR 'PO4' 'PO4'\r\n"
    strInputB5 += "   USEFOR 'Continuity' 'Continuity'\r\n"
    strInputB5 += "TIME BLOCK\r\n"
    strInputB5 += "DATA\r\n"
    strInputB5 += " 'FLOW' 'NO3' 'PO4' 'Continuity'\r\n"
    # name id num name
    # print strInputB5 % ('Tai',1,1,'Tai')

    # Block-5 col, block data of input points
    strInputD5 = ""
    strInputD5 += "  %s  %.4e  %.4e  %.4e  %.4e\r\n"
    # time FLOW NO3 PO4 Continuity
    # 2008/01/01-00:00:00  1.0040e+001  3.3000e-001  4.3000e-002  1.0000e+000
    # print strInputD5 % ('2008/01/01-00:00:00',10.04,0.33,0.043,1.0)


    #
    # Block-4 col, block header of input points
    #
    strInputB4 = ""
    strInputB4 += "; Data for '%s'\r\n"
    strInputB4 += "ITEM\r\n"
    strInputB4 += " '%i (%i) %s'\r\n"
    strInputB4 += "CONCENTRATIONS\r\n"
    strInputB4 += "   USEFOR 'FLOW' 'FLOW'\r\n"
    strInputB4 += "   USEFOR 'NO3' 'NO3'\r\n"
    strInputB4 += "   USEFOR 'PO4' 'PO4'\r\n"
    strInputB4 += "TIME BLOCK\r\n"
    strInputB4 += "DATA\r\n"
    strInputB4 += " 'FLOW' 'NO3' 'PO4'\r\n"
    # name id num name
    # print strInputB4 % ('Tai',1,1,'Tai')

    # Block-4 col, block data of input points
    strInputD4 = ""
    strInputD4 += "  %s  %.4e  %.4e  %.4e  \n"
    # time FLOW NO3 PO4
    # 2008/01/01-00:00:00  1.0040e+001  3.3000e-001  4.3000e-002
    # print strInputD4 % ('2008/01/01-00:00:00',10.04,0.33,0.043)

    #
    # init variables
    #
    dataInp    = []
    dataBlock  = []
    dataRow    = []
    dataDecVar = []
    with open(blockFname, 'r') as blockFref, open(decvarFname, 'r') as decvarFref, open(inp00Fname, 'r') as inpFref, open(tempFname, 'w') as tempFref:
        [nrowBlock, nrowInsertInp] = [int(elt.strip()) for elt in blockFref.readline().split('\t')]

        dataDecVar = [float(elt.strip()) for elt in decvarFref.readline().split('\t')]
        dataDecVarN = dataDecVar[:nrowBlock]
        dataDecVarP = dataDecVar[nrowBlock:]

        # print nrowBlock, nrowInsertInp
        blockFref.readline().strip()

        # id	num	index	name
        for line in blockFref:
            dataRow = [elt.strip() for elt in re.split('\s+',line.strip())]
            # print dataRow
            dataBlock.append([ int(dataRow[0]), int(dataRow[1]), int(dataRow[2]), dataRow[3] ])

        irowInpFile = 0
        for line in inpFref:
            irowInpFile += 1
            if irowInpFile == nrowInsertInp:
                writeBlockData(tempFref, blockDir, nrowBlock, dataBlock, dataDecVarN, dataDecVarP, strInputH, strInputL, strInputB5, strInputD5, strInputB4, strInputD4)
            else:
                tempFref.write(line)


def writeBlockData(tempFref, blockDir, nrowBlock, dataBlock, dataDecVarN, dataDecVarP, strInputH, strInputL, strInputB5, strInputD5, strInputB4, strInputD4):
    """

    :param tempFref:
    :param blockDir:
    :param nrowBlock:
    :param dataBlock:
    :param dataDecVarN:
    :param dataDecVarP:
    :param strInputH:
    :param strInputL:
    :param strInputB5:
    :param strInputD5:
    :param strInputB4:
    :param strInputD4:
    :return:
    """
    # strInputH:
    tempFref.write(strInputH % nrowBlock);
    # strInputL:
    # index id num name
    for iblock in range(nrowBlock):
        tempFref.write(strInputL % ( dataBlock[iblock][2], dataBlock[iblock][0], dataBlock[iblock][1], dataBlock[iblock][3] ))
    tempFref.write('\r\n')


    for iblock in range(nrowBlock):
        blockDataFname = blockDir+'/'+dataBlock[iblock][3]+'.inp'
        # print '--py:Test:: '+str(iblock)+'\t'+dataBlock[iblock][3]+'.inp'

        # dataBlockData = []
        dataRow = []
        with open(blockDataFname, 'r') as blockDataFref:
            line = blockDataFref.readline()
            dataRow = [elt.strip() for elt in re.split('\s+',line.strip())]
            # print dataRow
            # print len(dataRow)

            if len(dataRow) == 5:
                # strInputB5:
                # name id num name
                tempFref.write(strInputB5 % ( dataBlock[iblock][3], dataBlock[iblock][0], dataBlock[iblock][1], dataBlock[iblock][3] ))

                # dataBlockData.append([dataRow[0], float(dataRow[1]), float(dataRow[2]), float(dataRow[3]), float(dataRow[4])])
                # strInputD5:
                # 2008/01/01-00:00:00  1.0040e+001  3.3000e-001  4.3000e-002  1.0000e+000
                tempFref.write(strInputD5 % ( dataRow[0], float(dataRow[1]), float(dataRow[2])*dataDecVarN[iblock], float(dataRow[3])*dataDecVarP[iblock], float(dataRow[4]) ))
                for line in blockDataFref:
                    dataRow = [elt.strip() for elt in re.split('\s+',line.strip())]
                    # print dataRow

                    # dataBlockData.append([dataRow[0], float(dataRow[1]), float(dataRow[2]), float(dataRow[3]), float(dataRow[4])])
                    # strInputD5:
                    # strInputB5 += " 'FLOW' 'NO3' 'PO4' 'Continuity'\r\n"
                    # 2008/01/01-00:00:00  1.0040e+001  3.3000e-001  4.3000e-002  1.0000e+000
                    tempFref.write(strInputD5 % ( dataRow[0], float(dataRow[1]), float(dataRow[2])*dataDecVarN[iblock], float(dataRow[3])*dataDecVarP[iblock], float(dataRow[4]) ))

            elif len(dataRow) == 4:
                # strInputB4:
                # name id num name
                tempFref.write(strInputB4 % ( dataBlock[iblock][3], dataBlock[iblock][0], dataBlock[iblock][1], dataBlock[iblock][3] ))

                # dataBlockData.append([dataRow[0], float(dataRow[1]), float(dataRow[2]), float(dataRow[3])])
                # strInputD4:
                # 2008/01/01-00:00:00  1.0040e+001  3.3000e-001  4.3000e-002
                tempFref.write(strInputD4 % ( dataRow[0], float(dataRow[1]), float(dataRow[2])*dataDecVarN[iblock], float(dataRow[3])*dataDecVarP[iblock] ))
                for line in blockDataFref:
                    dataRow = [elt.strip() for elt in re.split('\s+',line.strip())]
                    # print dataRow

                    # dataBlockData.append([dataRow[0], float(dataRow[1]), float(dataRow[2]), float(dataRow[3])])
                    # strInputD4:
                    # strInputB4 += " 'FLOW' 'NO3' 'PO4'\r\n"
                    # 2008/01/01-00:00:00  1.0040e+001  3.3000e-001  4.3000e-002
                    tempFref.write(strInputD4 % ( dataRow[0], float(dataRow[1]), float(dataRow[2])*dataDecVarN[iblock], float(dataRow[3])*dataDecVarP[iblock] ))

            tempFref.write('\r\n')


if __name__ == "__main__":
    # icaseStart = 1
    # icaseEnd = 3
    #
    # taihuDir = '.'
    # blockDir = taihuDir+'/delblock'
    # inp00Dir = taihuDir+'/delinput'
    # tempDir  = taihuDir+'/deltemp'
    #
    # blockFname = blockDir+'/block6.inp'
    # inp00Fname = inp00Dir+'/taihu.inp'
    #
    # # --py:[icaseStart = 0, icaseEnd = 2] => [s00000000, s00000001]
    # for icase in range(icaseStart,icaseEnd):
    #     caseName = "t%08d" % icase
    #     decvarFname= tempDir+'/'+caseName+'.txt'
    #     tempFname  = tempDir+'/'+caseName+'.inp'
    #     main(blockDir, blockFname, decvarFname, inp00Fname, tempFname)

    # # --sh:[icaseStart = 1, icaseEnd = 2] => [t00000001, t00000002]
    # # python ./test_delft3d_inp.py -d "$blockDir" -b "$blockFname" -i "$inp00Fname" -t "$tempFname"
    main(sys.argv[1:])
