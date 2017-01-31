<html lang="en">
<head>
    <title>Taihu DSS</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="./assets/css/font-awesome-4.7.0/css/font-awesome.min.css">
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
        background-image:url('./assets/img/taihu-feature-graphic.png');
        background-repeat:no-repeat !important;
        -webkit-background-size:cover !important;
        -moz-background-size:cover !important;
        -o-background-size:cover !important;
        background-size:cover !important;
        background-position:center !important;
    }
    footer {
        background-color: #f2f2f2;;
        color: #000000;
        margin-top: 25px;
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
            <a class="navbar-brand" href="/">DSS</a>
        </div>

        <div class="collapse navbar-collapse" id="myNavbar">
            <ul class="nav navbar-nav">
                <li class="active"><a href="/taihu">Taihu</a></li>

                <li class="dropdown">
                    <a class="dropdown-toggle" data-toggle="dropdown" href="#">Test<span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="./moea/test_amga.php" target="_blank">AMGA2</a></li>
                        <li><a href="./moea/test_nsga.php" target="_blank">NSGAII</a></li>
                    </ul>
                </li>
            </ul>

            <ul class="nav navbar-nav navbar-right">
                <li><a href="./docs/_build/html/" target="_blank">Document</a></li>
                <li><a href="https://nl.linkedin.com/in/quanpan302" target="_blank">About</a></li>
                <p id="gltimer" class="navbar-text"><i class="fa fa-clock-o" aria-hidden="true"></i></p>
            </ul>
        </div>
    </div>
</nav>

<div class="container">
    <div class="jumbotron">
        <h1>Taihu Lake DSS</h1>
        <p>WAQ, MOEA, SM</p>
    </div>


<?php
    echo '<div class="row">';
        echo '<div class="col-sm-12">';
            echo '<div class="alert alert-info">Input</div>';
        echo '</div>';
    echo '</div>';

    echo '<div class="row">';
        echo '<div class="col-sm-4">';
            echo '<form action="./taihu/index_waq.php" method="get">';
                echo '<h4>delwaq loop</h4>';
                echo '<div class="form-group">';
                    echo '<label class="control-label col-sm-2" for="iswaq">Start</label>';
                    echo '<div class="col-sm-10">';
                        echo '<input type="text" class="form-control input-sm" name="iswaq" id="iswaq" value="1">';
                        echo '<span class="help-block">Case start</span>';
                    echo '</div>';
                echo '</div>';
                echo '<div class="form-group">';
                    echo '<label class="control-label col-sm-2" for="iewaq">End</label>';
                    echo '<div class="col-sm-10">';
                        echo '<input type="text" class="form-control input-sm" name="iewaq" id="iewaq" value="2">';
                        echo '<span class="help-block">Case End</span>';
                    echo '</div>';
                echo '</div>';

                echo '<div class="col-sm-12">';
                    echo '<button type="submit" class="btn btn-primary btn-block">Submit</button>';
                echo '</div>';
            echo '</form>';
        echo '</div>';

        echo '<div class="col-sm-4">';
            echo '<form action="./taihu/index_moea.php" method="get">';
                echo '<h4>delwaq moea</h4>';
                echo '<div class="form-group">';
                    echo '<label class="control-label col-sm-2" for="ngen">Ngen</label>';
                    echo '<div class="col-sm-10">';
                        echo '<input type="text" class="form-control input-sm" name="ngen" id="ngen" value="2">';
                        echo '<span class="help-block">Total generations</span>';
                    echo '</div>';
                echo '</div>';
                echo '<div class="form-group">';
                    echo '<label class="control-label col-sm-2" for="ndim">Ndim</label>';
                    echo '<div class="col-sm-10">';
                        echo '<input type="text" class="form-control input-sm" name="ndim" id="ndim" value="10">';
                        echo '<span class="help-block">Total decision variables</span>';
                    echo '</div>';
                echo '</div>';
                echo '<div class="form-group">';
                    echo '<label class="control-label col-sm-2" for="npop">Npop</label>';
                    echo '<div class="col-sm-10">';
                        echo '<input type="text" class="form-control input-sm" name="npop" id="npop" value="4">';
                        echo '<span class="help-block">Total populations</span>';
                    echo '</div>';
                echo '</div>';
                echo '<div class="form-group">';
                    echo '<label class="control-label col-sm-2" for="nobj">Nobj</label>';
                    echo '<div class="col-sm-10">';
                        echo '<input type="text" class="form-control input-sm" name="nobj" id="nobj" value="2">';
                        echo '<span class="help-block">Total objectives</span>';
                    echo '</div>';
                echo '</div>';
                echo '<div class="form-group">';
                    echo '<label class="control-label col-sm-2" for="ncon">Ncon</label>';
                    echo '<div class="col-sm-10">';
                        echo '<input type="text" class="form-control input-sm" name="ncon" id="ncon" value="0">';
                        echo '<span class="help-block">Total constraints</span>';
                    echo '</div>';
                echo '</div>';
                echo '<div class="form-group">';
                    echo '<label class="control-label col-sm-2" for="cxpb">CXPB</label>';
                    echo '<div class="col-sm-10">';
                        echo '<input type="text" class="form-control input-sm" name="cxpb" id="cxpb" value="0.9">';
                        echo '<span class="help-block">Crossover probability</span>';
                    echo '</div>';
                echo '</div>';

                echo '<div class="col-sm-12">';
                    echo '<button type="submit" class="btn btn-primary btn-block">Submit</button>';
                echo '</div>';
            echo '</form>';
        echo '</div>';

        echo '<div class="col-sm-4">';
            echo '<form action="./taihu/index_sm.php" method="get">';
                echo '<h4>delwaq sm</h4>';
                echo '<div class="form-group">';
                    echo '<label class="control-label col-sm-2" for="ngen">Ngen</label>';
                    echo '<div class="col-sm-10">';
                        echo '<input type="text" class="form-control input-sm" name="ngen" id="ngen" value="2">';
                        echo '<span class="help-block">Total generations</span>';
                    echo '</div>';
                echo '</div>';
                echo '<div class="form-group">';
                    echo '<label class="control-label col-sm-2" for="ndim">Ndim</label>';
                    echo '<div class="col-sm-10">';
                        echo '<input type="text" class="form-control input-sm" name="ndim" id="ndim" value="10">';
                        echo '<span class="help-block">Total decision variables</span>';
                    echo '</div>';
                echo '</div>';
                echo '<div class="form-group">';
                    echo '<label class="control-label col-sm-2" for="npop">Npop</label>';
                    echo '<div class="col-sm-10">';
                        echo '<input type="text" class="form-control input-sm" name="npop" id="npop" value="4">';
                        echo '<span class="help-block">Total populations</span>';
                    echo '</div>';
                echo '</div>';
                echo '<div class="form-group">';
                    echo '<label class="control-label col-sm-2" for="nobj">Nobj</label>';
                    echo '<div class="col-sm-10">';
                        echo '<input type="text" class="form-control input-sm" name="nobj" id="nobj" value="2">';
                        echo '<span class="help-block">Total objectives</span>';
                    echo '</div>';
                echo '</div>';
                echo '<div class="form-group">';
                    echo '<label class="control-label col-sm-2" for="ncon">Ncon</label>';
                    echo '<div class="col-sm-10">';
                        echo '<input type="text" class="form-control input-sm" name="ncon" id="ncon" value="0">';
                        echo '<span class="help-block">Total constraints</span>';
                    echo '</div>';
                echo '</div>';
                echo '<div class="form-group">';
                    echo '<label class="control-label col-sm-2" for="cxpb">CXPB</label>';
                    echo '<div class="col-sm-10">';
                        echo '<input type="text" class="form-control input-sm" name="cxpb" id="cxpb" value="0.9">';
                        echo '<span class="help-block">Crossover probability</span>';
                    echo '</div>';
                echo '</div>';

                echo '<div class="col-sm-12">';
                    echo '<button type="submit" class="btn btn-primary btn-block">Submit</button>';
                echo '</div>';
            echo '</form>';
        echo '</div>';
    echo '</div>';

    $rootDir = 'taihu';
    echo '<div class="row">';
        echo '<div class="col-sm-12">';
            echo '<div class="alert alert-info">Log</div>';
        echo '</div>';

        $dir1 = $rootDir.'/t00000001';
        echo '<div class="col-sm-12">';
            echo '<h4>'.$dir1.'</h4>';
            echo '<div class="row">';
                echo '<div class="col-sm-3">';
                    echo '<a href="'.$dir1.'/his_GREENS_s4011.png" target="_blank">';
                        echo '<img class="img-responsive" src="'.$dir1.'/his_GREENS_s4011.png" alt="'.$dir1.' his">';
                    echo '</a>';
                echo '</div>';
                echo '<div class="col-sm-3">';
                    echo '<a href="'.$dir1.'/his_GREENS_s13183.png" target="_blank">';
                        echo '<img class="img-responsive" src="'.$dir1.'/his_GREENS_s13183.png" alt="'.$dir1.' his">';
                    echo '</a>';
                echo '</div>';
                echo '<div class="col-sm-3">';
                    echo '<a href="'.$dir1.'/map_GREENS_t0.png" target="_blank">';
                        echo '<img class="img-responsive" src="'.$dir1.'/map_GREENS_t0.png" alt="'.$dir1.' map">';
                    echo '</a>';
                echo '</div>';
                echo '<div class="col-sm-3">';
                    echo '<a href="'.$dir1.'/map_GREENS_t1.png" target="_blank">';
                        echo '<img class="img-responsive" src="'.$dir1.'/map_GREENS_t1.png" alt="'.$dir1.' map">';
                    echo '</a>';
                echo '</div>';
            echo '</div>';
        echo '</div>';

        $dir2 = $rootDir.'/t00000002';
        echo '<div class="col-sm-12">';
            echo '<h4>'.$dir2.'</h4>';
            echo '<div class="row">';
                echo '<div class="col-sm-3">';
                    echo '<a href="'.$dir2.'/his_GREENS_s4011.png" target="_blank">';
                        echo '<img class="img-responsive" src="'.$dir2.'/his_GREENS_s4011.png" alt="'.$dir2.' his">';
                    echo '</a>';
                echo '</div>';
                echo '<div class="col-sm-3">';
                    echo '<a href="'.$dir2.'/his_GREENS_s13183.png" target="_blank">';
                        echo '<img class="img-responsive" src="'.$dir2.'/his_GREENS_s13183.png" alt="'.$dir2.' his">';
                    echo '</a>';
                echo '</div>';
                echo '<div class="col-sm-3">';
                    echo '<a href="'.$dir2.'/map_GREENS_t0.png" target="_blank">';
                        echo '<img class="img-responsive" src="'.$dir2.'/map_GREENS_t0.png" alt="'.$dir2.' map">';
                    echo '</a>';
                echo '</div>';
                echo '<div class="col-sm-3">';
                    echo '<a href="'.$dir2.'/map_GREENS_t1.png" target="_blank">';
                        echo '<img class="img-responsive" src="'.$dir2.'/map_GREENS_t1.png" alt="'.$dir2.' map">';
                    echo '</a>';
                echo '</div>';
            echo '</div>';
        echo '</div>';
    echo '</div>';

    echo '<div class="row">';
        echo '<div class="col-sm-12">';
            echo '<textarea rows="10" class="form-control noresize">';
                echo file_get_contents($rootDir.'/log.txt');
            echo '</textarea>';
        echo '</div>';
    echo '</div>';
?>


</div>
<footer class="container-fluid text-center">
    <span>Quan Pan&nbsp;</span>
    <a href="https://nl.linkedin.com/in/quanpan302" target="_blank">
        <i class="fa fa-linkedin-square" aria-hidden="true"></i>
    </a>
</footer>

<script>

</script>
</body>
</html>


<?php
//==============================
//==           TEST           ==
//==============================
//phpinfo();

//$exe_py_cmd = 'python /var/www/html/taihu/run.py 2>&1';
//$exe_sh_cmd = '/var/www/html/taihu/run.sh 2>&1';
//$exe_php_cmd = 'php /var/www/html/taihu/run.php 2>&1';
//$exe_cgi_cmd = '/var/www/html/taihu/run.cgi 2>&1';

//========== Test ==========
//$output = shell_exec('php -v');
//$output = exec('echo $PATH');

//$output = shell_exec('/var/www/html/taihu/run.sh');
//$output = exec('/var/www/html/taihu/run.sh');

//========== Python needed! ==========
//echo '<p style="color:red;">py: '.(new \DateTime())->format('Y-m-d H:i:s').'</p>';
//exec($exe_py_cmd,$output,$returnval);
//foreach($output as $text){echo "$text<br>";}
//echo '<p style="color:green;">output</p>';print_r($output);
//echo '<p style="color:blue;">returnval</p>'.print_r($returnval);

//========== Shell ==========
//echo '<p style="color:red;">sh: '.(new \DateTime())->format('Y-m-d H:i:s').'</p>';
//exec($exe_sh_cmd,$output,$returnval);
//foreach($output as $text){echo "$text<br>";}
//echo '<p style="color:green;">output</p>';print_r($output);
//echo '<p style="color:blue;">returnval</p>'.print_r($returnval);

//========== PhP shell ==========
//echo '<p style="color:red;">php: '.(new \DateTime())->format('Y-m-d H:i:s').'</p>';
//exec($exe_php_cmd,$output,$returnval);
//foreach($output as $text){echo "$text<br>";}
//echo '<p style="color:green;">output</p>';print_r($output);
//echo '<p style="color:blue;">returnval</p>'.print_r($returnval);

//========== CGI ==========
//echo '<p style="color:red;">cgi: '.(new \DateTime())->format('Y-m-d H:i:s').'</p>';
//exec($exe_cgi_cmd,$output,$returnval);
//foreach($output as $text){echo "$text<br>";}
//echo '<p style="color:green;">output</p>';print_r($output);
//echo '<p style="color:blue;">returnval</p>'.print_r($returnval);
?>
