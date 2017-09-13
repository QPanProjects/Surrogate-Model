<!DOCTYPE html>
<html lang="en">
<head>
    <title>Taihu DSS MOEA</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="/assets/css/font-awesome-4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.18.1/vis.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.18.1/vis.min.js"></script>


    <style>
    .noresize {
        resize: none;
    }
    .alert {
        margin: 10px 0px;
    }
    .jumbotron {
        width:100%;
        height:100%;
        height:calc(100% - 1px);
        margin-bottom: 0px;
        background-image:url('/assets/img/taihu-feature-graphic.png');
        background-repeat:no-repeat !important;
        -webkit-background-size:cover !important;
        -moz-background-size:cover !important;
        -o-background-size:cover !important;
        background-size:cover !important;
        background-position:center !important;
    }
    textarea {
        font-family: "Courier New", Courier, monospace;
        margin-top: 15px;
    }
    footer {
        background-color: #f2f2f2;;
        color: #000000;
        margin-top: 15px;
        padding: 15px;
    }
    </style>

    <script>
        var serverTime = new Date();

        function updateTime() {
            serverTime = new Date(serverTime.getTime() + 1000);
            $('#gltimer').html(serverTime.toGMTString());
        }
        updateTime();
        setInterval(updateTime, 1000);
    </script>
</head>
<body>
<nav class="navbar navbar-default navbar-fixed-top">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/">Home</a>
        </div>

        <div class="collapse navbar-collapse" id="myNavbar">
            <ul class="nav navbar-nav">
                <li><a href="/taihu">Taihu</a></li>
                <li><a href="/taihu/index_waq.php">WAQ</a></li>
                <li><a href="/taihu/index_grid.php">GRID</a></li>
                <li class="active"><a href="/taihu/index_moea.php">MOEA</a></li>
                <li><a href="/taihu/index_sm.php">Surrogate</a></li>
            </ul>

            <ul class="nav navbar-nav navbar-right">
                <li><a href="/docs/_build/html/" target="_blank">Document</a></li>
                <li><a href="/index_about.php">About</a></li>
            </ul>
        </div>
    </div>
</nav>

<div class="container-fluid">
    <div class="jumbotron">
        <h1>Taihu Lake MOEA</h1>
        <p>Quan Pan&nbsp;
            <a href="https://nl.linkedin.com/in/quanpan302" target="_blank">
                <i class="fa fa-linkedin-square" aria-hidden="true"></i>
            </a>
        </p>
    </div>

    <div class="row">
        <div class="col-sm-12 text-right">
            <span id="gltimer"><i class="fa fa-clock-o" aria-hidden="true"></i></span>
        </div>
    </div>

    <div class="row">
<?php
    $ready2start = FALSE;

    $_Ngen = 2;
    $_Ndim = 41*2;
    $_Npop = 4;
    $_Nobj = 2;
    $_Ncon = 0;
    $_CXPB = 0.9;

    $rootDir   = '/taihu';
    $resultDir = '/taihu/result/moea';

    if( count($_GET) > 5 ) {
        if( $_GET['ngen'] && $_GET['ndim'] && $_GET['npop'] && $_GET['nobj'] ) {
        //if( isset($_GET['ncon']) && !empty($_GET['ncon']) && $_GET['cxpb'] ) {
            $_Ngen = intval($_GET['ngen']);
            $_Ndim = intval($_GET['ndim']);
            $_Npop = intval($_GET['npop']);
            $_Nobj = intval($_GET['nobj']);
            $_Ncon = intval($_GET['ncon']);
            $_CXPB = floatval($_GET['cxpb']);

            if( $_Npop % 4 > 0.0 ){
                $_Ngen = intval($_GET['ngen']);
                $_Ndim = intval($_GET['ndim']);
                $_Npop = intval($_GET['npop']);
                $_Nobj = intval($_GET['nobj']);
                $_Ncon = intval($_GET['ncon']);
                $_CXPB = floatval($_GET['cxpb']);

                echo '<div class="alert alert-danger alert-dismissable">';
                    echo '<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>';
                    echo '--php:Error:: Remainder of <strong>Npop</strong> divided by 4 is not 0!&nbsp;';
                    print_r($_GET);
                echo '</div>';

            } else {
                $exe_py_cmd = 'python /var/www/html/taihu/run_moea.py'
                               .' -g '.$_Ngen
                               .' -d '.$_Ndim
                               .' -p '.$_Npop
                               .' -o '.$_Nobj
                               .' -c '.$_Ncon
                               .' -x '.$_CXPB
                               .' 2>&1';
                $ready2start = TRUE;
            }

        } else {
            echo '<div class="alert alert-danger alert-dismissable">';
                echo '<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>';
                echo '--php:Error:: Check input!&nbsp;';
                print_r($_GET);
            echo '</div>';
        }

    } else {
        echo '<div class="alert alert-info alert-dismissable"><a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>Welcome !&nbsp;</div>';
    }
?>
    </div>

    <div class="row">
        <div class="col-sm-3">
            <div class="row" style="background-color:#FFEBEE;">
                <div class="col-sm-12 text-center">
                    <h3>Input</h3>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-12">
                    <div class="row">
                        <div class="col-sm-12">
                            <h4>Model</h4>
                        </div>
                    </div>
                    <form action="index_moea.php" method="get" class="row">
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="ngen">Ngen</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control input-sm" name="ngen" id="ngen" value="<?php echo $_Ngen; ?>">
                                <span class="help-block">Total generations</span>
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="ndim">Ndim</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control input-sm" name="ndim" id="ndim" value="<?php echo $_Ndim; ?>" readonly>
                                <span class="help-block">Total decision variables</span>
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="npop">Npop</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control input-sm" name="npop" id="npop" value="<?php echo $_Npop; ?>">
                                <span class="help-block">Total populations</span>
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="nobj">Nobj</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control input-sm" name="nobj" id="nobj" value="<?php echo $_Nobj; ?>">
                                <span class="help-block">Total objectives</span>
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="ncon">Ncon</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control input-sm" name="ncon" id="ncon" value="<?php echo $_Ncon; ?>">
                                <span class="help-block">Total constraints</span>
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="cxpb">CXPB</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control input-sm" name="cxpb" id="cxpb" value="<?php echo $_CXPB; ?>">
                                <span class="help-block">Crossover probability</span>
                            </div>
                        </div>

                        <div class="col-sm-12">
                            <button type="submit" class="btn btn-primary btn-block">Submit</button>
                        </div>
                    </form>
                </div>
            </div>

            <div class="row">
            <?php
            if( $ready2start ){
                echo '<div class="col-sm-12">';
                    echo '<div class="alert alert-info"><i id="loading-indicator" class="fa fa-spinner fa-pulse fa-fw"></i>&nbsp;'.$exe_py_cmd.'</div>';
                echo '</div>';

                echo '<div class="col-sm-12">';
                    echo '<button id="startsm" type="button" class="btn btn-success btn-block">Start</button>';
                echo '</div>';
            }
            ?>
            </div>
        </div>

        <div class="col-sm-6">
            <div class="row" style="background-color:#E8F5E9;">
                <div class="col-sm-12 text-center">
                    <h3>Result</h3>
                </div>
            </div>

            <?php
            if( $ready2start ){
            ?>
            <div class="row">
                <div class="col-sm-6">
                    <div class="row text-center">
                        <div class="col-sm-12">
                            <h4>t01</h4>
                        </div>
                        <div class="col-sm-12">
                            <div class="row">
                                <div class="col-sm-12">
                                    <a id="imgt01his" href="" target="_blank">
                                        <i class="fa fa-picture-o fa-3x fa-fw"></i>
                                    </a>
                                </div>
                                <div class="col-sm-12">
                                    <a id="imgt01map" href="" target="_blank">
                                        <i class="fa fa-picture-o fa-3x fa-fw"></i>
                                    </a>
                                </div>
                                <div class="col-sm-12">
                                    <div id="grapht01" class="center-block">
                                        <i class="fa fa-picture-o fa-3x fa-fw"></i>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-sm-6">
                    <div class="row text-center">
                        <div class="col-sm-12">
                            <h4>t02</h4>
                        </div>

                        <div class="col-sm-12">
                            <div class="row">
                                <div class="col-sm-12">
                                    <a id="imgt02his" href="" target="_blank">
                                        <i class="fa fa-picture-o fa-3x fa-fw"></i>
                                    </a>
                                </div>
                                <div class="col-sm-12">
                                    <a id="imgt02map" href="" target="_blank">
                                        <i class="fa fa-picture-o fa-3x fa-fw"></i>
                                    </a>
                                </div>
                                <div class="col-sm-12">
                                    <div id="grapht02" class="center-block">
                                        <i class="fa fa-picture-o fa-3x fa-fw"></i>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-12">
                    <div class="row text-center">
                        <div class="col-sm-12">
                            <a id="imgjson" href="" target="_blank">
                                <i class="fa fa-picture-o fa-3x fa-fw"></i>
                            </a>
                        </div>
                        <div class="col-sm-12">
                            <h4><a id="filejson" class="btn btn-info btn-block" href="" target="_blank">JSON</a></h4>
                        </div>
                    </div>
                </div>
                <div class="hidden-xs col-sm-12">
                    <table class="table table-hover">
                        <thead>
                            <tr>
                                <th>Gen</th>
                                <th>Obj</th>
                                <th>Var</th>
                            </tr>
                        </thead>
                    </table>
                </div>
            </div>
            <?php
            }
            ?>
        </div>

        <div class="col-sm-3">
            <div class="row" style="background-color:#E3F2FD;">
                <div class="col-sm-12 text-center">
                    <h3>Plot</h3>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-12">
                    <div class="row">
                        <div class="col-sm-12">
                            <h4 class="text-right">t01</h4>
                        </div>
                    </div>
                    <div id="imgt01" class="row">
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="c">Case</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control input-sm" name="c" id="c" value="1">
                                <span class="help-block">Casename</span>
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="v">Vare</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control input-sm" name="v" id="v" value="GREENS" readonly>
                                <span class="help-block">Variable Name</span>
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="p">Point</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control input-sm" name="p" id="p" value="1">
                                <span class="help-block">Point position</span>
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="t">Time</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control input-sm" name="t" id="t" value="0">
                                <span class="help-block">Time</span>
                            </div>
                        </div>
                        <input type="hidden" name="pref" id="pref" value="moea">

                        <div class="col-sm-12">
                            <button id="startimg" type="submit" class="btn btn-primary btn-block <?php if(!$ready2start){ echo 'disabled';} ?>">Plot</button>
                        </div>
                    </div>
                </div>

               <div class="col-sm-12">
                    <div class="row">
                        <div class="col-sm-12">
                            <h4 class="text-right">t02</h4>
                        </div>
                    </div>
                    <div id="imgt02" class="row">
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="c">Case</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control input-sm" name="c" id="c" value="2">
                                <span class="help-block">Casename</span>
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="v">Var</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control input-sm" name="v" id="v" value="GREENS" readonly>
                                <span class="help-block">Variable Name</span>
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="p">Point</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control input-sm" name="p" id="p" value="1">
                                <span class="help-block">Point position</span>
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="t">Time</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control input-sm" name="t" id="t" value="0">
                                <span class="help-block">Time</span>
                            </div>
                        </div>
                        <input type="hidden" name="pref" id="pref" value="moea">

                        <div class="col-sm-12">
                            <button id="startimg" type="submit" class="btn btn-primary btn-block <?php if(!$ready2start){ echo 'disabled';} ?>">Plot</button>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>

    <div class="row">
        <div class="col-sm-12">
            <textarea rows="10" class="form-control noresize"></textarea>
        </div>
    </div>
</div>
<footer class="container-fluid text-center">
    <span>Quan Pan&nbsp;</span>
    <a href="https://nl.linkedin.com/in/quanpan302" target="_blank">
        <i class="fa fa-linkedin-square" aria-hidden="true"></i>
    </a>
</footer>

<script>
$( document ).ready(function() {
    $('#loading-indicator').hide();
    var $textarea = $('textarea');

    var logExe = "Welcome to Taihu DSS Multi-Objective Evolution Algorithm";
    $textarea.text(logExe);

    var resultDir = "<?php echo $resultDir; ?>";

    $('#filejson').attr('href',resultDir+'/taihu.json');
    $('#imgjson').attr('href',resultDir+'/taihu.json.png').html(
        '<img class="img-responsive" src="'+resultDir+'/taihu.json.png?'+serverTime.getTime()+'" alt="Result JSON">'
    );

    $("#imgt01 #startimg").click(function(){
        $.ajax({
            url: "result.php",
            method: "GET",
            async: true,
            timeout: 0,
            data: {
                c: $("#imgt01 #c").val(),
                v: $("#imgt01 #v").val(),
                p: $("#imgt01 #p").val(),
                t: $("#imgt01 #t").val(),
                pref: $("#imgt01 #pref").val()
            },
            beforeSend: function() {
                var icon = '<i class="fa fa-spinner fa-spin fa-3x fa-fw"></i>';
                $('#imgt01his').html( icon );
                $('#imgt01map').html( icon );
                $('#grapht01').html( icon );
            },
            success: function(result,status,xhr){
                var data_array = $.parseJSON(result);

                $('#imgt01his').attr('href',data_array['his']).html(
                    '<img class="img-responsive" src="'+data_array['his']+'" alt="his">'
                );
                $('#imgt01map').attr('href',data_array['map']).html(
                    '<img class="img-responsive" src="'+data_array['map']+'" alt="map">'
                );

                drawVisualization(data_array['json'],'grapht01');

                if ( $("div#grapht01 + a#graphfull3d" ).length ) {
                    $( "div#grapht01 + a#graphfull3d" ).attr( 'href','/taihu/result_full3d.php?'+
                        'c='+$("#imgt01 #c").val()+
                        '&v='+$("#imgt01 #v").val()+
                        '&t='+$("#imgt01 #t").val()+
                        '&pref='+$("#imgt01 #pref").val() );
                } else {
                    $( "div#grapht01" ).after( '<a id="graphfull3d" href="/taihu/result_full3d.php?'+
                        'c='+$("#imgt01 #c").val()+
                        '&v='+$("#imgt01 #v").val()+
                        '&t='+$("#imgt01 #t").val()+
                        '&pref='+$("#imgt01 #pref").val()+
                        '" class="btn btn-info btn-block" target="_blank">Full</a>' );
                }
            },
            error: function(xhr,status,error) {
                var icon = '<i class="fa fa-exclamation-circle" aria-hidden="true"></i>';
                $('#imgt01his').html( icon );
                $('#imgt01map').html( icon );
                $('#grapht01').html( icon );
            }
        });
    });
    $("#imgt02 #startimg").click(function(){
        $.ajax({
            url: "result.php",
            method: "GET",
            async: true,
            timeout: 0,
            data: {
                c: $("#imgt02 #c").val(),
                v: $("#imgt02 #v").val(),
                p: $("#imgt02 #p").val(),
                t: $("#imgt02 #t").val(),
                pref: $("#imgt02 #pref").val()
            },
            beforeSend: function() {
                var icon = '<i class="fa fa-spinner fa-spin fa-3x fa-fw"></i>';
                $('#imgt02his').html( icon );
                $('#imgt02map').html( icon );
                $('#grapht02').html( icon );
            },
            success: function(result,status,xhr){
                var data_array = $.parseJSON(result);

                $('#imgt02his').attr('href',data_array['his']).html(
                    '<img class="img-responsive" src="'+data_array['his']+'" alt="his">'
                );
                $('#imgt02map').attr('href',data_array['map']).html(
                    '<img class="img-responsive" src="'+data_array['map']+'" alt="map">'
                );

                drawVisualization(data_array['json'],'grapht02');

                if ( $("div#grapht02 + a#graphfull3d" ).length ) {
                    $( "div#grapht02 + a#graphfull3d" ).attr( 'href','/taihu/result_full3d.php?'+
                        'c='+$("#imgt02 #c").val()+
                        '&v='+$("#imgt02 #v").val()+
                        '&t='+$("#imgt02 #t").val()+
                        '&pref='+$("#imgt02 #pref").val() );
                } else {
                    $( "div#grapht02" ).after( '<a id="graphfull3d" href="/taihu/result_full3d.php?'+
                        'c='+$("#imgt02 #c").val()+
                        '&v='+$("#imgt02 #v").val()+
                        '&t='+$("#imgt02 #t").val()+
                        '&pref='+$("#imgt02 #pref").val()+
                        '" class="btn btn-info btn-block" target="_blank">Full</a>' );
                }
            },
            error: function(xhr,status,error) {
                var icon = '<i class="fa fa-exclamation-circle" aria-hidden="true"></i>';
                $('#imgt02his').html( icon );
                $('#imgt02map').html( icon );
                $('#grapht02').html( icon );
            }
        });
    });

    $("button#startsm").click(function(){
        $.ajax({
            url: "run_moea.php",
            method: "GET",
            async: false,
            timeout: 0,
            data: {
                ngen: <?php echo $_Ngen; ?>,
                ndim: <?php echo $_Ndim; ?>,
                npop: <?php echo $_Npop; ?>,
                nobj: <?php echo $_Nobj; ?>,
                ncon: <?php echo $_Ncon; ?>,
                cxpb: <?php echo $_CXPB; ?>
            },
            beforeSend: function() {
                logExe  = "--php:Start:: Model\n\n";
                $textarea.text(logExe);

                var icon = '<i class="fa fa-spinner fa-spin fa-3x fa-fw"></i>';
                $('#imgt01his').html( icon );
                $('#imgt01map').html( icon );
                $('#grapht01').html( icon );

                $('#imgt02his').html( icon );
                $('#imgt02map').html( icon );
                $('#grapht02').html( icon );

                $('#imgjson').html( icon );
            },
            success: function(result,status,xhr){
                logExe  = "--php:Success:: Model " + xhr.status + " " + xhr.statusText+"\n\n";
                logExe += result;
                $textarea.text(logExe);

                var icon = '<i class="fa fa-picture-o fa-3x fa-fw"></i>';
                $('#imgt01his').html( icon );
                $('#imgt01map').html( icon );
                $('#grapht01').html( icon );

                $('#imgt02his').html( icon );
                $('#imgt02map').html( icon );
                $('#grapht02').html( icon );

                $('#filejson').attr('href',resultDir+'/taihu.json');
                $('#imgjson').attr('href',resultDir+'/taihu.json.png').html(
                    '<img class="img-responsive" src="'+resultDir+'/taihu.json.png?'+serverTime.getTime()+'" alt="Result JSON">'
                );
            },
            error: function(xhr,status,error) {
                logExe  = "--php:Error:: Model " + xhr.status + " " + xhr.statusText+"\n\n";
                logExe += error;
                $textarea.text(logExe);

                var icon = '<i class="fa fa-exclamation-circle" aria-hidden="true"></i>';
                $('#imgt01his').html( icon );
                $('#imgt01map').html( icon );
                $('#grapht01').html( icon );

                $('#imgt02his').html( icon );
                $('#imgt02map').html( icon );
                $('#grapht02').html( icon );

                $('#imgjson').html( icon );
            }
        });
    });
});

// Called when the Visualization API is loaded.
function drawVisualization(jsonFname,containerId) {
    var data = null;
    var data = new vis.DataSet();

    var jsonMapContainer = document.getElementById(containerId);

    $.getJSON( jsonFname, function( jsonData ) {
        jsonMapContainer.innerHTML = '';

        for (var i = 0; i < jsonData['x'].length; i += 1) {
            data.add({
                x: jsonData['x'][i],
                y: jsonData['y'][i],
                z: jsonData['z'][i],
                style: jsonData['z'][i]
            });
        }

        // specify options
        var options = {
            width:  '100%',
            height: '300px',
            style: 'surface',
            showPerspective: false,
            showGrid: true,
            showShadow: false,
            showLegend: true,
            keepAspectRatio: true,
            verticalRatio: 0.5,
            legendLabel: jsonData['legend'],
            zMin: jsonData['zMin'],
            zMax: jsonData['zMax']
        };
        graph3d = new vis.Graph3d(jsonMapContainer, data, options);
    });

}
</script>
</body>
</html>
