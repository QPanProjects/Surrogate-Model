<!DOCTYPE html>
<html lang="en">
<head>
    <title>Taihu DSS SM</title>
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
                <li class="active"><a href="/taihu/index_waq.php">WAQ</a></li>
                <li><a href="/taihu/index_moea.php">MOEA</a></li>
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
        <h1>Taihu Lake WAQ Loop</h1>
        <p>Quan Pan&nbsp;
            <a href="https://nl.linkedin.com/in/quanpan302" target="_blank">
                <i class="fa fa-linkedin-square" aria-hidden="true"></i>
            </a>
        </p>
    </div>

    <div class="row">
        <div class="col-sm-12">
            <p id="gltimer" class="text-right"><i class="fa fa-clock-o" aria-hidden="true"></i></p>
        </div>
    </div>

    <div class="row">
<?php
    $ready2start = FALSE;

    $icaseStart = 99999999;
    $icaseEnd   = 99999999;

    $rootDir   = '/taihu';
    $dir1 = $rootDir.'/t00000001';
    $dir2 = $rootDir.'/t00000002';

    if( count($_GET) > 0 ) {
        if( $_GET['iswaq'] && $_GET['iewaq'] ) {
            $icaseStart = (int)$_GET['iswaq'];
            $icaseEnd = (int)$_GET['iewaq'];

            if( $icaseStart > $icaseEnd ){
                $icaseStart = (int)$_GET['iswaq'];
                $icaseEnd = (int)$_GET['iewaq'];

                echo '<div class="alert alert-danger alert-dismissable">';
                    echo '<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>';
                    echo '--php:Error:: <strong>Start</strong> is larger than <strong>End</strong>!&nbsp;';
                    print_r($_GET);
                echo '</div>';

            } else {
                $exe_py_cmd = 'python /var/www/html/taihu/run_waq.py'
                               .' -s '.$icaseStart
                               .' -e '.$icaseEnd
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
                    <form action="index_waq.php" method="get" class="row">
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="iswaq">Start</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control input-sm" name="iswaq" id="iswaq" value="<?php echo $icaseStart; ?>">
                                <span class="help-block">Case start</span>
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="control-label col-sm-2" for="iewaq">End</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control input-sm" name="iewaq" id="iewaq" value="<?php echo $icaseEnd; ?>">
                                <span class="help-block">Case End</span>
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
            <div class="row text-center">
                <div class="col-sm-12">
                    <h3>t01</h3>
                </div>
                <div class="col-sm-12">
                    <div class="row">
                        <div class="col-sm-6">
                            <a id="imgt01his" href="" target="_blank">
                                <i class="fa fa-picture-o fa-3x fa-fw"></i>
                            </a>
                        </div>
                        <div class="col-sm-6">
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

                <div class="col-sm-12">
                    <h3>t02</h3>
                </div>

                <div class="col-sm-12">
                    <div class="row">
                        <div class="col-sm-6">
                            <a id="imgt02his" href="" target="_blank">
                                <i class="fa fa-picture-o fa-3x fa-fw"></i>
                            </a>
                        </div>
                        <div class="col-sm-6">
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

    var logExe = "Welcome to Taihu DSS WAQ Loop";
    $textarea.text(logExe);

    var dir1 = "<?php echo $dir1; ?>";
    var dir2 = "<?php echo $dir2; ?>";

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
                t: $("#imgt01 #t").val()
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
            },
            error(xhr,status,error){
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
                t: $("#imgt02 #t").val()
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
            },
            error(xhr,status,error){
                var icon = '<i class="fa fa-exclamation-circle" aria-hidden="true"></i>';
                $('#imgt02his').html( icon );
                $('#imgt02map').html( icon );
                $('#grapht02').html( icon );
            }
        });
    });

    $("button#startsm").click(function(){
        $.ajax({
            url: "run_waq.php",
            method: "GET",
            async: false,
            timeout: 0,
            data: {
                iswaq: <?php echo $icaseStart; ?>,
                iewaq: <?php echo $icaseEnd; ?>
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
            },
            error(xhr,status,error){
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
            }
        });
    });
});

// Called when the Visualization API is loaded.
function drawVisualization(jsonFname,containerId) {
    var data = null;

    // Create and populate a data table.
    var data = new vis.DataSet();

    $.getJSON( jsonFname, function( jsonData ) {
        var jsonMapContainer = document.getElementById(containerId);

        for (var i = 0; i < jsonData['x'].length; i += 1) {
        //for (var i = 0; i < 100; i += 1) {
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
            height: '500px',
            style: 'surface',
            showPerspective: false,
            showGrid: true,
            showShadow: false,
            keepAspectRatio: true,
            verticalRatio: 0.5
        };

        // create a graph3d
        graph3d = new vis.Graph3d(jsonMapContainer, data, options);
    });

}
</script>
</body>
</html>
