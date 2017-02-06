<!DOCTYPE html>
<html lang="en">
<head>
    <title>Taihu DSS WAQ</title>
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
        <div class="col-sm-8">
            <div class="row">
                <div class="col-sm-12">
                    <h3>Result</h3>
                </div>
            </div>


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

                echo '<div class="row">';
                    echo '<div class="col-sm-12">';
                        echo '<div class="alert alert-danger">--php:Error:: <strong>Start</strong> is larger than <strong>End</strong>!&nbsp;';
                        print_r($_GET);
                        echo '</div>';
                    echo '</div>';
                echo '</div>';

            } else {
                $exe_py_cmd = 'python /var/www/html/taihu/run_waq.py'
                               .' -s '.$icaseStart
                               .' -e '.$icaseEnd
                               .' 2>&1';
                $ready2start = TRUE;


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
            $icaseStart = (int)$_GET['iswaq'];
            $icaseEnd = (int)$_GET['iewaq'];

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

    var logExe = "Welcome to Taihu DSS WAQ";
    $textarea.text(logExe);

    var dir1 = "<?php echo $dir1; ?>";
    var dir2 = "<?php echo $dir2; ?>";

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
                logExe  = "--php:Start:: WAQ\n\n";
                $textarea.text(logExe);

                var icon = '<i class="fa fa-spinner fa-spin fa-3x fa-fw"></i>';
                $('#imgt01hisg4011' ).html( icon );
                $('#imgt01mapg1'    ).html( icon );
                $('#imgt02hisg4011' ).html( icon );
                $('#imgt02mapg1'    ).html( icon );
            },
            success: function(result,status,xhr){
                logExe  = "--php:Success:: WAQ " + xhr.status + " " + xhr.statusText+"\n\n";
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
            },
            error(xhr,status,error){
                logExe  = "--php:Error:: WAQ " + xhr.status + " " + xhr.statusText+"\n\n";
                logExe += error;
                $textarea.text(logExe);

                var icon = '<i class="fa fa-exclamation-circle" aria-hidden="true"></i>';
                $('#imgt01hisg4011' ).html( icon );
                $('#imgt01mapg1'    ).html( icon );
                $('#imgt02hisg4011' ).html( icon );
                $('#imgt02mapg1'    ).html( icon );
            }
        });
    });

});
</script>
</body>
</html>
