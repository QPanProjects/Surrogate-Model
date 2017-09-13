<!DOCTYPE html>
<html lang="en">
<head>
    <title>Taihu DSS</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/assets/css/font-awesome-4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
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
                <li><a href="/taihu/index_grid.php">GRID</a></li>
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
        <a class="btn btn-primary" href="/taihu/index_grid.php">GRID</a>
        <a class="btn btn-primary" href="/taihu/index_moea.php?ngen=2&ndim=82&npop=4&nobj=2&ncon=0&cxpb=0.9">MOEA</a>
        <a class="btn btn-primary" href="/taihu/index_sm.php?ngen=2&ndim=82&npop=4&nobj=2&ncon=0&cxpb=0.9">Surrogate</a>
    </div>

    <div class="row">
        <div class="col-sm-12 text-center">
            <h3>Input</h3>
        </div>
        <div class="col-sm-12">
            <div id="d3dInputList">
                d3dInputList
            </div>
        </div>
    </div>

<?php
    $rootDir = '/taihu';
    $resultDirM = '/taihu/result/moea';
    $resultDirS = '/taihu/result/sm';
    $dirS1 = $rootDir.'/sm00000001';
    $dirS2 = $rootDir.'/sm00000002';
    $dirM1 = $rootDir.'/moea00000001';
    $dirM2 = $rootDir.'/moea00000002';


    echo '<div class="row text-center">';
        echo '<div class="col-sm-6">';
            echo '<div class="row">';
                echo '<div class="col-sm-12">';
                    echo '<h3>MOEA</h3>';
                echo '</div>';
            echo '</div>';

            echo '<div class="row">';
                echo '<div class="col-sm-12">';
                    echo '<a id="imgjsonM" href="'.$resultDirM.'/taihu.json.png" target="_blank">';
                        echo '<i class="fa fa-picture-o fa-3x fa-fw"></i>';
                    echo '</a>';
                echo '</div>';
                echo '<div class="col-sm-12">';
                    echo '<a class="btn btn-info btn-block" href="'.$resultDirM.'/taihu.json" target="_blank">JSON</a>';
                echo '</div>';
            echo '</div>';
        echo '</div>';

        echo '<div class="col-sm-6">';
            echo '<div class="row">';
                echo '<div class="col-sm-12">';
                    echo '<h3>Surrogate</h3>';
                echo '</div>';
            echo '</div>';

            echo '<div class="row">';
                echo '<div class="col-sm-12">';
                    echo '<a id="imgjsonS" href="'.$resultDirS.'/taihu.json.png" target="_blank">';
                        echo '<i class="fa fa-picture-o fa-3x fa-fw"></i>';
                    echo '</a>';
                echo '</div>';
                echo '<div class="col-sm-12">';
                    echo '<a class="btn btn-info btn-block" href="'.$resultDirS.'/taihu.json" target="_blank">JSON</a>';
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
    console.log( 'start' );
    var resultDirM = "<?php echo $resultDirM; ?>";
    var resultDirS = "<?php echo $resultDirS; ?>";

    $.ajax({
        url: "/taihu/delblock/block_list.json",
        method: "GET",
        async: true,
        timeout: 0,
        dataType: "json",
        beforeSend: function() {
            $('div#d3dInputList').html(
                '<i class="fa fa-spinner fa-spin fa-2x fa-fw"></i>'
            );
        },
        success: function(result){
            var htmlstring = '';
            htmlstring +=
                '<div class="dropdown">'
                    +'<button class="btn btn-info btn-block dropdown-toggle" type="button" id="d3dstation" data-toggle="dropdown">'
                        +result['station'][0]
                    +'</button>'
                    +'<ul class="dropdown-menu" style="max-height: 300px;overflow-y:scroll; " role="menu" aria-labelledby="d3dstation">';

            $.each( result['station'], function( key,value ) {
                // htmlstring += '<li role="presentation"><a role="menuitem" tabindex="'+key+'" href="#">'+value+'</a></li>';
                htmlstring +=
                    '<li role="presentation">'
                        +'<a role="menuitem" tabindex="-1">'
                            +'<img style="width:50px; height:50px;" src="/taihu/delblock/'+value+'_Discharge.png?'+serverTime.getTime()+'" alt="Input">'
                            +'<img style="width:50px; height:50px;" src="/taihu/delblock/'+value+'_NO3.png?'+serverTime.getTime()+'" alt="Input">'
                            +'<img style="width:50px; height:50px;" src="/taihu/delblock/'+value+'_PO4.png?'+serverTime.getTime()+'" alt="Input">'
                            +value
                        +'</a>'
                    +'</li>';
            });
            htmlstring +=
                    '</ul>'
                +'</div>';

            htmlstring +=
                '<div class="col-sm-4">'
                    +'<a id="imgStationDischarge" href="/taihu/delblock/'+result['station'][0]+'_Discharge.png" target="_blank">'
                    +'<img class="img-responsive" src="/taihu/delblock/'+result['station'][0]+'_Discharge.png?'+serverTime.getTime()+'" alt="Input">'
                    +'</a>'
                +'</div>'
                +'<div class="col-sm-4">'
                    +'<a id="imgStationNO3" href="/taihu/delblock/'+result['station'][0]+'_NO3.png" target="_blank">'
                    +'<img class="img-responsive" src="/taihu/delblock/'+result['station'][0]+'_NO3.png?'+serverTime.getTime()+'" alt="Input">'
                    +'</a>'
                +'</div>'
                +'<div class="col-sm-4">'
                    +'<a id="imgStationPO4" href="/taihu/delblock/'+result['station'][0]+'_PO4.png" target="_blank">'
                    +'<img class="img-responsive" src="/taihu/delblock/'+result['station'][0]+'_PO4.png?'+serverTime.getTime()+'" alt="Input">'
                    +'</a>'
                +'</div>';

            $('div#d3dInputList').html( htmlstring );

            $('ul.dropdown-menu li a').on('click', function(event) {
                event.preventDefault();

                var text = $(this).text();
                $(this).parents('.dropdown').find('.dropdown-toggle').val(text).text(text);

                $('#imgStationDischarge').attr('href','/taihu/delblock/'+text+'_Discharge.png');
                $('#imgStationDischarge img').attr('src','/taihu/delblock/'+text+'_Discharge.png?'+serverTime.getTime());

                $('#imgStationNO3').attr('href','/taihu/delblock/'+text+'_NO3.png');
                $('#imgStationNO3 img').attr('src','/taihu/delblock/'+text+'_NO3.png?'+serverTime.getTime());

                $('#imgStationPO4').attr('href','/taihu/delblock/'+text+'_PO4.png');
                $('#imgStationPO4 img').attr('src','/taihu/delblock/'+text+'_PO4.png?'+serverTime.getTime());
            });
        }
    });


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
