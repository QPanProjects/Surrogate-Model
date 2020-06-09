#!/bin/bash
# echo $# arguments string to $0: $*
# echo $# arguments sequence to $0: $@
#
# ./run.sh 1 2
# ./run.sh 1 2 > ./log.txt 2>&1 &
#
# echo >&2 "$string"
# define STDIN_FILENO    0   /* Standard input.  */
# define STDOUT_FILENO   1   /* Standard output.  */
# define STDERR_FILENO   2   /* Standard error output.  */
#
# return status range: 0-255
#
# integer compare
# -eq == equal
# -ge >= greater than or equal to
# -gt >  greater than
# -le <= less than or equal to
# -lt <  less than
# -ne    not equal to
#
# 0 --sh:Success::[] 0
# 1 --sh:Warning::[] 0
# 2 --sh:Error::  [] 2
#   --sh:Start::  [] 2
#   --sh:End::    [] 4
#   --sh:Test::   [] 3

#clear
createdir(){
    local retval=255
    #
    # input arguments
    #
    local casedir=$1

    if [ -d "$casedir" ]
    then
        rm -rf "$casedir"
        echo "--sh:Warning::[directory $casedir exists, will be removed]"
        retval=1

#    else
#        mkdir "$casedir"
#        retval=$?
#        chmod -R 777 "$casedir"
#        echo "--sh:Success::[create $casedir]"

#        ls -all "$casedir"
    fi

    mkdir "$casedir"
    retval=$?
    chmod -R 777 "$casedir"
    echo "--sh:Success::[create $casedir]"

    return "$retval"
}

createD3Dinp(){
    local retval=255
    #
    # input arguments
    #
    local blockdir=$1
    local blockfname=$2
    local decvarfname=$3
    local inp00fname=$4
    local tempfname=$5

    echo "--sh:Test::   [create Delft3D input $tempfname]"
#    echo "--sh:Test::   [create Delft3D input $blockdir, $blockfname, $inp00fname, $tempfname]"
#    echo "--sh:Test::   [blockdir   : $blockdir]"
#    echo "--sh:Test::   [blockfname : $blockfname]"
#    echo "--sh:Test::   [decvarfname: decvarfname]"
#    echo "--sh:Test::   [inp00fname : $inp00fname]"
#    echo "--sh:Test::   [tempfname  : $tempfname]"

    # --py:Code:: def main(blockDir, blockFname, inp00Fname, tempFname):
    python ./d3d_create_inp.py -d "$blockdir" -b "$blockfname" -v "$decvarfname" -i "$inp00fname" -t "$tempfname"
    retval=$?

#    ls -all "$tempfname"
    return "$retval"
}

copyfile(){
    local retval=255
    #
    # input arguments
    #
    local filefrom=$1
    local fileto=$2

    if [ -f "$filefrom" ]
    then
        cp "$filefrom" "$fileto"
#        mv "$filefrom" "$fileto"
        retval=$?

        chmod 777 "$fileto"
        echo "--sh:Success::[copy to $fileto]"
#        echo "--sh:Success:: copy $filefrom to $fileto."

#        ls -all "$fileto"
    else
        echo "--sh:Error::  [file $filefrom does not exist]"
        retval=1
    fi

    return "$retval"
}
movefile(){
    local retval=255
    #
    # input arguments
    #
    local filefrom=$1
    local fileto=$2

    if [ -f "$filefrom" ]
    then
#        cp "$filefrom" "$fileto"
        mv "$filefrom" "$fileto"
        retval=$?

        chmod 777 "$fileto"
        echo "--sh:Success::[move to $fileto]"
#        echo "--sh:Success:: copy $filefrom to $fileto."

#        ls -all "$fileto"
    else
        echo "--sh:Error::  [file $filefrom does not exist]"
        retval=1
    fi

    return "$retval"
}

readD3Dmap(){
    local retval=255
    #
    # input arguments
    #
    local taihudir=$1
    local casedir=$2

    local varname=GREENS
#    local iseg=0
#    local itime=0

#    local iseg=-9999
#    local itime=-9999
#    local iseg=4011
#    local itime=4
    local iseg=9969
    local itime=4

    echo "--sh:Test::   [read Delft3D-WAQ map $casedir, $varname, $iseg, $itime]"
#    echo "--sh:Test::   [read Delft3D-WAQ map $taihudir, casedir, $varname, $iseg, $itime]"
#    echo "--sh:Test::   [taihudir  : $taihudir]"
#    echo "--sh:Test::   [casedir   : $casedir]"
#    echo "--sh:Test::   [varname   : $varname]"
#    echo "--sh:Test::   [iseg      : $iseg]"
#    echo "--sh:Test::   [itime     : $itime]"

    # --py:Code:: def main(taihuDir, caseName, varName, iseg, itime):
    # --sh:Cmd:: python d3d_read_map.py -d . -c t00000001 -v GREENS -p 4011 -t 1
#    local iseg=4011
#    local itime=0
#    python ./d3d_read_map.py -d "$taihudir" -c "$casedir" -v "$varname" -p "$iseg" -t "$itime"
#    retval=$?

    # --sh:Cmd:: python d3d_read_map.py -d . -c t00000001 -v GREENS -p 13183 -t 1
#    iseg=13183
#    itime=1
    python ./d3d_read_map.py -d "$taihudir" -c "$casedir" -v "$varname" -p "$iseg" -t "$itime"
    retval=$?

#    ls -all "$taihudir/$casedir"
    return "$retval"
}

rundelwaq(){
    local retval=255
    #
    # input arguments
    #
    local exedir=$1
    local casedir=$2
    local inpfname=$3
    local bloomfname=$4
    local procfname=$5

#    echo "--sh:Test:: run Delft3D delwaq"
#    echo "--sh:Test:: exedir    : $exedir"
#    echo "--sh:Test:: inpfname  : $inpfname"
#    echo "--sh:Test:: bloomfname: $bloomfname"
#    echo "--sh:Test:: procfname : $procfname"

    #
    # Run delwaq1
    #
    echo "--sh:Start::  [delwaq1]"

    $exedir/delwaq1 "$inpfname" -eco "$bloomfname" -p "$procfname"
    if [ $? -eq 0 ]
    then
        #
        # Run delwaq2
        #
        echo "--sh:Start::  [delwaq2]"

        $exedir/delwaq2 $inpfname
        retval=$?
        if [ $retval -eq 0 ]
        then
            echo "--sh:Success::[run delwaq2]"

#            ls -all "$casedir"
        else
            echo "--sh:Error::  [delwaq2 did not run correctly, ending calculation]"
        fi
    else
        echo "--sh:Error::  [delwaq1 did not run correctly, ending calculation]"
        retval=1
    fi

    return "$retval"
}


#echo ""
#echo "=================================================="
#echo "==                                              =="
#echo "==   Project:  Surrogate Model                  =="
#echo "==                                              =="
#echo "==   Author:   Quan Pan                         =="
#echo "==   Email:    quanpan302@hotmail.com           =="
#echo "==                                              =="
#echo "==   License:  MIT License                      =="
#echo "==   Create:   2016-12-02                       =="
#echo "==                                              =="
#echo "=================================================="
#echo ""
#echo "--sh:Start:: $0 $# arguments: $*"
if [ $# -eq 4 ]; then
    #
    # input arguments
    #
    if [ $1 -gt $2 ]
    then
        icaseStart=$1
        icaseEnd=$1
    else
        icaseStart=$1
        icaseEnd=$2
    fi
    casedir=$3
#    casepref=$4
    casepref=$4%08g

    #
    # Set runtime directory:
    #
    # install directory: fortran, netcdf, delft3d
    #
    installdir=/home/pan4

    # library: fortran, netcdf
    libfortrandir=$installdir/netcdf-fortran-4.4.4/fortran/.libs/
    libnetcdfdir=$installdir/netcdf-c-4.4.1/liblib/.libs/
    # executable: delft3d
    exedelwaqdir=$installdir/delft3d_repository/bin/lnx64/waq/bin
    # LD_LIBRARY_PATH
    export LD_LIBRARY_PATH=$exedelwaqdir:$libnetcdfdir:$libfortrandir:$LD_LIBRARY_PATH

    # delft3d file: proc_def
    procfname=$installdir/delft3d_repository/bin/lnx64/waq/default/proc_def
    # delft3d file: bloom
    bloomfname=$installdir/delft3d_repository/bin/lnx64/waq/default/bloom.spe

    #
    # Set case directory :
    #
    # s00000001/taihu.inp
    #   1.create directory with name $casename
    #   2.copy deltemp/s00000001.inp in to $casename/taihu.inp
    #
    inpfile=taihu.inp

    taihudir=/var/www/html/taihu

    blockdir=$taihudir/delblock
    blockfname=$taihudir/delblock/block6.inp

    inp00dir=$taihudir/delinput
    inp00fname=$taihudir/delinput/taihu.inp

    tempdir=$taihudir/deltemp

    #
    # set $casename t|s00000000
    #
    for casename in $(seq -f $casepref $icaseStart $icaseEnd)
    do
#        echo ""
        echo "--sh:Start::  [$casename]"

        casedirR=$casedir/$casename
        casedirF=$taihudir/$casedir/$casename

        inpfname=$casedirF/$inpfile

        decvarfname=$tempdir/$casename.txt
        tempfname=$tempdir/$casename.inp


        #
        # test function
        #
#        createD3Dinp "$blockdir" "$blockfname" "$inp00fname" "$tempfname"
#        readD3Dmap "$taihudir" "$casedirR"

        #
        # main flow
        #
        createdir "$casedirF"
        if [ $? -eq 0 ]
        then
            createD3Dinp "$blockdir" "$blockfname" "$decvarfname" "$inp00fname" "$tempfname"
            if [ $? -eq 0 ]
            then
                movefile "$decvarfname" "$casedirF/taihu_decvar.txt"

                movefile "$tempfname" "$inpfname"

#                echo "--sh:Test::   [rundelwaq OFF]"
                if [ $? -eq 0 ]
                then
                    #
                    # Run delwaq1 and delwaq2
                    #
                    rundelwaq "$exedelwaqdir" "$casedirF" "$inpfname" "$bloomfname" "$procfname"
                    if [ $? -eq 0 ]
                    then
                        #
                        # fetch delwaq result taihu.map data
                        #
                        readD3Dmap "$taihudir" "$casedirR"
                    else
                        echo "--sh:Error:: run delwaq."
                    fi
                fi

            fi
        fi
        echo "--sh:End::    [$casename]"
    done
else
    echo "--sh:Error::  [Your command line contains no arguments]"
fi



