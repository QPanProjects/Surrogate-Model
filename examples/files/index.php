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
                <li><a href="/taihu">Taihu</a></li>
                <li><a href="/wsn">WSN</a></li>

                <li class="dropdown">
                    <a class="dropdown-toggle" data-toggle="dropdown" href="#">Test<span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="/moea/test_amga.php" target="_blank">AMGA2</a></li>
                        <li><a href="/moea/test_nsga.php" target="_blank">NSGAII</a></li>
                    </ul>
                </li>
            </ul>

            <ul class="nav navbar-nav navbar-right">
                <li><a href="/docs/_build/html/" target="_blank">Document</a></li>
                <li><a href="https://nl.linkedin.com/in/quanpan302" target="_blank">About</a></li>
                <p id="gltimer" class="navbar-text"><i class="fa fa-clock-o" aria-hidden="true"></i></p>
            </ul>
        </div>
    </div>
</nav>


<div class="container">
    <div class="jumbotron">
        <h1>Decision Support System</h1>
        <p>
            Quan Pan&nbsp;
            <a href="https://nl.linkedin.com/in/quanpan302" target="_blank">
                <i class="fa fa-linkedin-square" aria-hidden="true"></i>
            </a>
        </p>
    </div>

    <div class="row">
        <div class="col-sm-12">
            <h2>Decision Support System</h2>
        </div>
        <div class="col-sm-12">
            <h2>Taihu Lake</h2>
            <p>
                Taihu Lake DSS
                <a href="/taihu">
                    <i class="fa fa-link" aria-hidden="true"></i>
                </a>
            </p>
        </div>
        <div class="col-sm-12">
            <h2>Water Supply Network</h2>
            <p>
                Water Supply Network DSS
                <a href="/wsn">
                    <i class="fa fa-link" aria-hidden="true"></i>
                </a>
            </p>
        </div>
    </div>
</div>


