<!DOCTYPE html>
<html lang="en">
<head>
    <title>Taihu DSS</title>
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
        margin: 15px 0px;
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
            <a class="navbar-brand" href="/">Home</a>
        </div>

        <div class="collapse navbar-collapse" id="myNavbar">
            <ul class="nav navbar-nav">
                <li class="active"><a href="/taihu">Taihu</a></li>
                <li><a href="/taihu/index_waq.php">WAQ</a></li>
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
        <h1>Taihu Lake DSS</h1>
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

    <div class="btn-group btn-group-justified">
        <a class="btn btn-primary" href="/taihu/index_waq.php?iswaq=1&iewaq=2">WAQ</a>
        <a class="btn btn-primary" href="/taihu/index_moea.php?ngen=2&ndim=10&npop=4&nobj=2&ncon=0&cxpb=0.9">MOEA</a>
        <a class="btn btn-primary" href="/taihu/index_sm.php?ngen=2&ndim=10&npop=4&nobj=2&ncon=0&cxpb=0.9">Surrogate Model</a>
    </div>

    <div class="row">
        <div class="col-sm-12">
            <h2 class="text-right">Log</h2>
        </div>
    </div>


<?php
    $rootDir = '/taihu';
    $resultDirM = '/taihu/result/moea';
    $resultDirS = '/taihu/result/surrogate';
    $dir1 = $rootDir.'/t00000001';
    $dir2 = $rootDir.'/t00000002';


    echo '<div class="row">';
        echo '<div class="col-sm-6">';
            echo '<h3>MOEA</h3>';
            echo '<div class="row">';
                echo '<div class="col-sm-12">';
                    echo '<h4>'.$resultDirM.'&nbsp;<a href="'.$resultDirM.'/taihu.json" target="_blank">JSON</a></h4>';
                echo '</div>';
                echo '<div class="col-sm-12">';
                    echo '<a id="imgjsonM" href="'.$resultDirM.'/taihu.json.png" target="_blank">';
                        echo '<i class="fa fa-picture-o fa-3x fa-fw"></i>';
                    echo '</a>';
                echo '</div>';
            echo '</div>';
        echo '</div>';

        echo '<div class="col-sm-6">';
            echo '<h3>Surrogate</h3>';
            echo '<div class="row">';
                echo '<div class="col-sm-12">';
                    echo '<h4>'.$resultDirS.'&nbsp;<a href="'.$resultDirS.'/taihu.json" target="_blank">JSON</a></h4>';
                echo '</div>';
                echo '<div class="col-sm-12">';
                    echo '<a id="imgjsonS" href="'.$resultDirS.'/taihu.json.png" target="_blank">';
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
                    echo '<a id="imgt01hisg13183" href="'.$dir1.'/his_GREENS_s4011.png" target="_blank">';
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
                    echo '<a id="imgt02hisg13183" href="'.$dir2.'/his_GREENS_s4011.png" target="_blank">';
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

    echo '<div class="row">';
        echo '<div class="col-sm-12">';
            echo '<textarea rows="10" class="form-control noresize">';
                echo file_get_contents('log.txt');
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
$( document ).ready(function() {
    var dir1 = "<?php echo $dir1; ?>";
    var dir2 = "<?php echo $dir2; ?>";
    var resultDirM = "<?php echo $resultDirM; ?>";
    var resultDirS = "<?php echo $resultDirS; ?>";

    $('#imgt01hisg13183').html(
        '<img class="img-responsive" src="'+dir1+'/his_GREENS_s4011.png?'+serverTime.getTime()+'" alt="'+dir1+' his">'
    );
    $('#imgt01mapg1').html(
        '<img class="img-responsive" src="'+dir1+'/map_GREENS_t4.png?'+serverTime.getTime()+'" alt="'+dir1+' map">'
    );

    $('#imgt02hisg13183').html(
        '<img class="img-responsive" src="'+dir2+'/his_GREENS_s4011.png?'+serverTime.getTime()+'" alt="'+dir2+' his">'
    );
    $('#imgt02mapg1').html(
        '<img class="img-responsive" src="'+dir2+'/map_GREENS_t4.png?'+serverTime.getTime()+'" alt="'+dir2+' map">'
    );

    $('#imgjsonM').html(
        '<img class="img-responsive" src="'+resultDirM+'/taihu.json.png?'+serverTime.getTime()+'" alt="MOEA Result JSON">'
    );
    $('#imgjsonS').html(
        '<img class="img-responsive" src="'+resultDirS+'/taihu.json.png?'+serverTime.getTime()+'" alt="Surrogate Model Result JSON">'
    );

});
</script>
</body>
</html>
