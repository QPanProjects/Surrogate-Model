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
        <div class="col-sm-12">
            <p id="gltimer" class="text-right"><i class="fa fa-clock-o" aria-hidden="true"></i></p>
        </div>
    </div>

    <div class="row">
        <div class="col-sm-8">
            <div class="row">
                <div class="col-sm-12">
                    <h3>Result</h3>
                </div>
            </div>


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
    $dir1 = $rootDir.'/t00000001';
    $dir2 = $rootDir.'/t00000002';

    if( count($_GET) > 0 ) {
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

                echo '<div class="row">';
                    echo '<div class="col-sm-12">';
                        echo '<div class="alert alert-danger">--php:Error:: Remainder of <strong>Npop</strong> divided by 4 is not 0!&nbsp;';
                        print_r($_GET);
                        echo '</div>';
                    echo '</div>';
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


                echo '<div class="row">';
                    echo '<div class="col-sm-6">';
                        echo '<table class="table table-hover">';
                            echo '<thead>';
                                echo '<tr>';
                                    echo '<th>Gen</th>';
                                    echo '<th>Obj</th>';
                                    echo '<th>Var</th>';
                                echo '</tr>';
                            echo '</thead>';
                        echo '</table>';
                    echo '</div>';
                    echo '<div class="col-sm-6">';
                        echo '<div class="row">';
                            echo '<div class="col-sm-12">';
                                echo '<h4>'.$resultDir.'&nbsp;<a href="'.$resultDir.'/taihu.json" target="_blank">JSON</a></h4>';
                            echo '</div>';
                            echo '<div class="col-sm-12">';
                                echo '<a id="imgjson" href="'.$resultDir.'/taihu.json.png" target="_blank">';
                                    echo '<i class="fa fa-picture-o fa-3x fa-fw"></i>';
                                echo '</a>';
                            echo '</div>';
                        echo '</div>';
                    echo '</div>';
                echo '</div>';

                echo '<div class="row">';
                    echo '<div class="col-sm-6">';
                        echo '<h4>'.$dir1.'</h4>';
                        echo '<div class="row">';
                            echo '<div class="col-sm-6">';
                                echo '<a id="imgt01hisg4011" href="'.$dir1.'/his_GREENS_s4011.png" target="_blank">';
                                    echo '<i class="fa fa-picture-o fa-3x fa-fw"></i>';
                                echo '</a>';
                            echo '</div>';
                            echo '<div class="col-sm-6">';
                                echo '<a id="imgt01mapg1" href="'.$dir1.'/map_GREENS_t4.png" target="_blank">';
                                    echo '<i class="fa fa-picture-o fa-3x fa-fw"></i>';
                                echo '</a>';
                            echo '</div>';
                        echo '</div>';
                    echo '</div>';

                    echo '<div class="col-sm-6">';
                        echo '<h4>'.$dir2.'</h4>';
                        echo '<div class="row">';
                            echo '<div class="col-sm-6">';
                                echo '<a id="imgt02hisg4011" href="'.$dir2.'/his_GREENS_s4011.png" target="_blank">';
                                    echo '<i class="fa fa-picture-o fa-3x fa-fw"></i>';
                                echo '</a>';
                            echo '</div>';
                            echo '<div class="col-sm-6">';
                                echo '<a id="imgt02mapg1" href="'.$dir2.'/map_GREENS_t4.png" target="_blank">';
                                    echo '<i class="fa fa-picture-o fa-3x fa-fw"></i>';
                                echo '</a>';
                            echo '</div>';
                        echo '</div>';
                    echo '</div>';
                echo '</div>';
            }

        } else {
            $_Ngen = intval($_GET['ngen']);
            $_Ndim = intval($_GET['ndim']);
            $_Npop = intval($_GET['npop']);
            $_Nobj = intval($_GET['nobj']);
            $_Ncon = intval($_GET['ncon']);
            $_CXPB = floatval($_GET['cxpb']);

            echo '<div class="row">';
                echo '<div class="col-sm-12">';
                    echo '<div class="alert alert-danger">--php:Error:: check input!&nbsp;';
                    print_r($_GET);
                    echo '</div>';
                echo '</div>';
            echo '</div>';
        }

    } else {
        echo '<div class="row">';
            echo '<div class="col-sm-12">';
                echo '<div class="alert alert-info">Welcome !&nbsp;';
                echo '</div>';
            echo '</div>';
        echo '</div>';
    }
?>
        </div>
        <div class="col-sm-4">
            <div class="row">
                <div class="col-sm-12">
                    <h3 class="text-right">Input</h3>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-12">
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
                    echo '<button id="startsm" type="button" class="btn btn-success btn-block">Start Surrogate Model</button>';
                echo '</div>';
            }
            ?>
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

    var logExe = "Welcome to Taihu DSS MOEA";
    $textarea.text(logExe);

    var dir1 = "<?php echo $dir1; ?>";
    var dir2 = "<?php echo $dir2; ?>";
    var resultDir = "<?php echo $resultDir; ?>";

    $('#imgt01hisg4011').html(
        '<img class="img-responsive" src="'+dir1+'/his_GREENS_s4011.png?'+serverTime.getTime()+'" alt="'+dir1+' his">'
    );
    $('#imgt01mapg1').html(
        '<img class="img-responsive" src="'+dir1+'/map_GREENS_t4.png?'+serverTime.getTime()+'" alt="'+dir1+' map">'
    );

    $('#imgt02hisg4011').html(
        '<img class="img-responsive" src="'+dir2+'/his_GREENS_s4011.png?'+serverTime.getTime()+'" alt="'+dir2+' his">'
    );
    $('#imgt02mapg1').html(
        '<img class="img-responsive" src="'+dir2+'/map_GREENS_t4.png?'+serverTime.getTime()+'" alt="'+dir2+' map">'
    );

    $('#imgjson').html(
        '<img class="img-responsive" src="'+resultDir+'/taihu.json.png?'+serverTime.getTime()+'" alt="Result JSON">'
    );

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
                logExe  = "--php:Start:: MOEA\n\n";
                $textarea.text(logExe);

                var icon = '<i class="fa fa-spinner fa-spin fa-3x fa-fw"></i>';
                $('#imgt01hisg4011' ).html( icon );
                $('#imgt01mapg1'    ).html( icon );
                $('#imgt02hisg4011' ).html( icon );
                $('#imgt02mapg1'    ).html( icon );
                $('#imgt02mapg1'    ).html( icon );

                $('#imgjson').html( icon );
            },
            success: function(result,status,xhr){
                logExe  = "--php:Success:: MOEA " + xhr.status + " " + xhr.statusText+"\n\n";
                logExe += result;
                $textarea.text(logExe);

                $('#imgt01hisg4011').html(
                    '<img class="img-responsive" src="'+dir1+'/his_GREENS_s4011.png?'+serverTime.getTime()+'" alt="'+dir1+' his">'
                );
                $('#imgt01mapg1').html(
                    '<img class="img-responsive" src="'+dir1+'/map_GREENS_t4.png?'+serverTime.getTime()+'" alt="'+dir1+' map">'
                );

                $('#imgt02hisg4011').html(
                    '<img class="img-responsive" src="'+dir2+'/his_GREENS_s4011.png?'+serverTime.getTime()+'" alt="'+dir2+' his">'
                );
                $('#imgt02mapg1').html(
                    '<img class="img-responsive" src="'+dir2+'/map_GREENS_t4.png?'+serverTime.getTime()+'" alt="'+dir2+' map">'
                );

                $('#imgjson').html(
                    '<img class="img-responsive" src="'+resultDir+'/taihu.json.png?'+serverTime.getTime()+'" alt="Result JSON">'
                );
            },
            error(xhr,status,error){
                logExe  = "--php:Error:: MOEA " + xhr.status + " " + xhr.statusText+"\n\n";
                logExe += error;
                $textarea.text(logExe);

                var icon = '<i class="fa fa-exclamation-circle" aria-hidden="true"></i>';
                $('#imgt01hisg4011' ).html( icon );
                $('#imgt01mapg1'    ).html( icon );
                $('#imgt02hisg4011' ).html( icon );
                $('#imgt02mapg1'    ).html( icon );

                $('#imgjson').html( icon );
            }
        });
    });

});
</script>
</body>
</html>
