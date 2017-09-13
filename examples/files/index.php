<!DOCTYPE html>
<html lang="en">
<head>
    <title>Taihu DSS</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="/assets/css/font-awesome-4.7.0/css/font-awesome.min.css">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">

    <style>
    body {
        width: 100%;
        height: 100%;
        font-family: 'Lato',sans-serif;
        font-weight: 300;
        color: #666;
        background-color: #fff;
    }

    html {
        width: 100%;
        height: 100%;
    }

    .navbar {
        margin-bottom: 0;
        border-bottom: 1px solid rgba(227,242,253,.4);
    }
    .navbar-brand {
        font-weight: 700;
    }
    .navbar-brand {
        height: 40px;
        padding: 5px 15px;
        font-size: 18px;
        line-height: 1em;
    }
    .navbar-brand h1{
        color: #0D47A1;
        font-size: 20px;
        line-height: 40px;
    }
    .navbar-brand:focus {
        outline: 0;
    }
    .nav.navbar-nav {
        background-color: rgba(227,242,253,.1);
    }
    .navbar-custom.top-nav-collapse .nav.navbar-nav {
        background-color: rgba(227,242,253,.1);
    }
    .navbar-custom ul.nav li a {
        font-size: 12px;
        letter-spacing: 1px;
        color: #1565C0;
        text-transform: uppercase;
        font-weight: 700;
    }
    .navbar-custom.top-nav-collapse ul.nav li a {
        -webkit-transition: all .2s ease-in-out;
        -moz-transition: all .2s ease-in-out;
        transition: all .2s ease-in-out;
        color: #1976D2;
    }
    .navbar-custom ul.nav ul.dropdown-menu {
        border-radius: 0;
    }
    .navbar-custom ul.nav ul.dropdown-menu li {
        background-color: rgba(227,242,253,.1);
        border-bottom: 1px solid rgba(227,242,253,.1);
    }
    .navbar-custom ul.nav ul.dropdown-menu li:last-child{
        border-bottom: none;
    }
    .navbar-custom ul.nav ul.dropdown-menu li a {
        padding: 10px 20px;
        color: #1976D2;
    }
    .navbar-custom ul.nav ul.dropdown-menu li a:hover {
        background-color: rgba(227,242,253,.4);
    }

    .navbar-custom.top-nav-collapse ul.nav ul.dropdown-menu li {
        background-color: rgba(227,242,253,.1);
        border-bottom: 1px solid rgba(227,242,253,.1);
    }
    .navbar-custom.top-nav-collapse ul.nav ul.dropdown-menu li a {
        color: #1E88E5;
    }
    .navbar-custom.top-nav-collapse ul.nav ul.dropdown-menu li a:hover {
        background-color: rgba(227,242,253,.4);
    }
    .navbar-custom .nav li a {
        -webkit-transition: background .3s ease-in-out;
        -moz-transition: background .3s ease-in-out;
        transition: background .3s ease-in-out;
    }
    .navbar-custom .nav li a:hover,
    .navbar-custom .nav li a:focus,
    .navbar-custom .nav li.active {
        outline: 0;
        background-color: rgba(227,242,253,.4);
    }
    .navbar-custom.top-nav-collapse .nav li a:hover,
    .navbar-custom.top-nav-collapse .nav li a:focus,
    .navbar-custom.top-nav-collapse .nav li.active {
        outline: 0;
        background-color: rgba(227,242,253,.4);
    }
    .navbar-toggle {
        padding: 4px 6px;
        font-size: 14px;
        color: #0D47A1;
        border: 1px solid #0D47A1;
    }
    .navbar-toggle:focus,
    .navbar-toggle:active {
        outline: 0;
    }

    /* ===========================
     * Elements
     */
    .btn {
        border-radius: 0;
        text-transform: uppercase;
        font-family: Montserrat,sans-serif;
        font-weight: 400;
        -webkit-transition: all .3s ease-in-out;
        -moz-transition: all .3s ease-in-out;
        transition: all .3s ease-in-out;
    }
    .btn-circle {
        width: 70px;
        height: 70px;
        margin-top: 15px;
        padding: 7px 16px;
        border: 2px solid #fff;
        border-radius: 50%;
        font-size: 40px;
        color: #fff;
        background: 0 0;
        -webkit-transition: background .3s ease-in-out;
        -moz-transition: background .3s ease-in-out;
        transition: background .3s ease-in-out;
    }
    .btn-circle.btn-dark {
        border: 2px solid #666;
        color: #666;
    }
    .btn-circle:hover,
    .btn-circle:focus {
        outline: 0;
        color: #999;
        background: rgba(255,255,255,.1);
    }
    .btn-circle.btn-dark :hover,
    .btn-circle.btn-dark :focus {
        outline: 0;
        color: #999;
        background: rgba(255,255,255,.1);
    }
    .btn-circle.btn-dark :hover i,
    .btn-circle.btn-dark :focus i{
        color: #999;
        background: rgba(255,255,255,.1);
    }

    .page-scroll .btn-circle i.animated {
        -webkit-transition-property: -webkit-transform;
        -webkit-transition-duration: 1s;
        -moz-transition-property: -moz-transform;
        -moz-transition-duration: 1s;
    }
    .page-scroll .btn-circle:hover i.animated {
        -webkit-animation-name: pulse;
        -moz-animation-name: pulse;
        -webkit-animation-duration: 1.5s;
        -moz-animation-duration: 1.5s;
        -webkit-animation-iteration-count: infinite;
        -moz-animation-iteration-count: infinite;
        -webkit-animation-timing-function: linear;
        -moz-animation-timing-function: linear;
    }
    @-webkit-keyframes pulse {
        0 {
            -webkit-transform: scale(1);
            transform: scale(1);
        }
        50% {
            -webkit-transform: scale(1.2);
            transform: scale(1.2);
        }
        100% {
            -webkit-transform: scale(1);
            transform: scale(1);
        }
    }
    @-moz-keyframes pulse {
        0 {
            -moz-transform: scale(1);
            transform: scale(1);
        }
        50% {
            -moz-transform: scale(1.2);
            transform: scale(1.2);
        }
        100% {
            -moz-transform: scale(1);
            transform: scale(1);
        }
    }

    #preloader {
        background: #ffffff;
        position: fixed;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 999;
    }
    #load {
        background-color: #FF4136;
        opacity: 0.75;
        position: absolute;
        top: 50%;
        right: 0;
        left: 0;
        width: 10px;
        height: 10px;
        margin: -5px auto 0 auto;
        border-radius: 0px;
        border: 5px solid #FF4136;
        box-shadow: 10px 0px #39CCCC, 10px 0px #01FF70;
        animation: shadowSpin 1s ease-in-out infinite;
        z-index: 9999;
    }

    /* ===========================
     * self design
     */
    .noresize {
        resize: none;
    }
    a:hover, a:active, a:focus {
        outline: 0;
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

    .section {
        padding-top:50px;
        width: 100%;
        height:400px;
        color: #000000;
        background-color: #eeeeee;
    }

    /* ===========================
     * Footer
     */
    footer {
        text-align: center;
        background-color: #f2f2f2;;
        margin-top: 0px;
        padding: 15px;
    }
    footer p {
        margin-top: 25px;
        color: #000000;
    }
    </style>

    <script>
    </script>
</head>
<body id="page-top" data-spy="scroll" data-target=".navbar-custom">
<div id="preloader">
    <div id="load"></div>
</div>

<nav class="navbar navbar-custom navbar-fixed-top" role="navigation">
    <div class="container">
        <div class="navbar-header page-scroll">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-main-collapse">
                <span><i class="fa fa-bars" aria-hidden="true"></i></span>
            </button>
            <a class="navbar-brand" href="/">
                <h1>Home</h1>
            </a>
        </div>

        <div class="collapse navbar-collapse navbar-right navbar-main-collapse">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#secdss">DSS</a></li>
                <li><a href="#secwsn">WSN</a></li>
                <li><a href="#sectaihu">Taihu</a></li>

                <li><a href="#secmoea">Optimization</a></li>
                <li><a href="#secdoc">Document</a></li>
                <li><a href="#secabout">About</a></li>
            </ul>
        </div>

    </div>
</nav>


<div class="container">
    <div class="jumbotron text-center">
        <h1>Decision Support System</h1>
        <p>
            <a href="https://nl.linkedin.com/in/quanpan302" target="_blank">
                <i class="fa fa-linkedin-square" aria-hidden="true"></i>&nbsp;Quan Pan
            </a>
        </p>
        <div class="page-scroll">
            <a href="#sectaihu" class="btn btn-circle btn-dark">
                <i class="fa fa-angle-double-down animated"></i>
            </a>
        </div>
    </div>

    <div class="row text-right">
        <div class="col-sm-12">
            <span id="gltimer"><i class="fa fa-clock-o" aria-hidden="true"></i></span>
        </div>
    </div>
</div>

<section id="secdss" class="section text-center">
    <div class="container">
        <div class="row">
            <div class="col-sm-12">
                <h2>Decision Support System</h2>
            </div>
        </div>
    </div>
</section>

<section id="secwsn" class="section text-center">
    <div class="container">
        <div class="row">
            <div class="col-sm-12">
                <h2>Water Supply Network</h2>
                <p>
                    <a href="/wsn">
                        <i class="fa fa-link animated" aria-hidden="true"></i>&nbsp;Water Supply Network DSS
                    </a>
                </p>
            </div>
        </div>
    </div>
</section>

<section id="sectaihu" class="section text-center">
    <div class="container">
        <div class="row">
            <div class="col-sm-12">
                <h2>Taihu Lake</h2>
                <p>
                    <a href="/taihu">
                        <i class="fa fa-link animated" aria-hidden="true"></i>&nbsp;Taihu Lake DSS
                    </a>
                </p>
            </div>
        </div>
    </div>
</section>

<section id="secmoea" class="section text-center">
    <div class="container">
        <div class="row">
            <div class="col-sm-12">
                <h2>Multi-Objective Evolution Algorithm </h2>
                <p>
                    <a href="/moea/test_amga.php" target="_blank">
                        <i class="fa fa-link animated" aria-hidden="true"></i>&nbsp;AMGA2
                    </a>
                </p>
                <p>
                    <a href="/moea/test_nsga.php" target="_blank">
                        <i class="fa fa-link animated" aria-hidden="true"></i>&nbsp;NSGAII
                    </a>
                </p>
            </div>
        </div>
    </div>
</section>

<section id="secdoc" class="section text-center">
    <div class="container">
        <div class="row">
            <div class="col-sm-12">
                <h2>Document</h2>
                <p>
                    <a href="/docs/_build/html/" target="_blank">
                        <i class="fa fa-link animated" aria-hidden="true"></i>&nbsp;Document
                    </a>
                </p>
            </div>
        </div>
    </div>
</section>

<section id="secabout" class="section text-center">
    <div class="container">
        <div class="row">
            <div class="col-sm-12">
                <h2>About</h2>
                <p>
                    <a href="/index_about.php">
                        <i class="fa fa-link animated" aria-hidden="true"></i>&nbsp;About
                    </a>
                </p>
            </div>
        </div>
    </div>
</section>

<footer>
    <div class="container">
        <div class="row">
            <div class="col-sm-12">
                <div class="wow shake" data-wow-delay="0.4s">
                    <div class="page-scroll">
                        <a href="#sectaihu" id="totop" class="btn btn-circle btn-dark">
                            <i class="fa fa-angle-double-up animated"></i>
                        </a>
                    </div>
                </div>
                <p>
                    <i class="fa fa-copyright" aria-hidden="true"></i>&nbsp;All rights reserved.&nbsp;
                    <i class="fa fa-id-card" aria-hidden="true"></i>&nbsp;Quan Pan&nbsp;
                    <a href="https://nl.linkedin.com/in/quanpan302" target="_blank">
                        <i class="fa fa-linkedin-square" aria-hidden="true"></i>
                    </a>
                </p>
            </div>
        </div>
    </div>
</footer>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<script src="http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery-scrollTo/2.1.0/jquery.scrollTo.min.js"></script>
<script src="/assets/js/wow.js"></script>

<script>
(function ($) {
    new WOW().init();

    $(window).load(function() {
        // executes when complete page is fully loaded,
        // including all frames, objects and images

        $("#preloader").delay(100).fadeOut("slow");
        $("#load").delay(100).fadeOut("slow");
    });

    $(window).scroll(function() {
        if ($(".navbar").offset().top > 50) {
            $(".navbar-fixed-top").addClass("top-nav-collapse");
        } else {
            $(".navbar-fixed-top").removeClass("top-nav-collapse");
        }
    });

    $(function(){
        // executes when HTML-Document is loaded and DOM is ready
        // $(document).ready(function(){  });
        // $(function(){  });

        var serverTime = new Date();

        function updateTime() {
            serverTime = new Date(serverTime.getTime() + 1000);
            $('#gltimer').html(serverTime.toGMTString());
        }
        updateTime();
        setInterval(updateTime, 1000);

        $('.navbar-nav li a[href^="#"]').on('click', function(event) {
            // method 1
            if (this.hash !== "") {
                event.preventDefault();
                var hash = this.hash;
                $('html, body').animate({
                    scrollTop: $(hash).offset().top
                }, 1000, function(){
                    window.location.hash = hash;
                });
            }

            // method 2
            //  jquery easing plugin
            //just pass scrollclass in design and start scrolling
			//var $anchor = $(this);
			//$('html, body').stop().animate({
			//	scrollTop: $($anchor.attr('href')).offset().top
			//}, 1000, 'easeInOutExpo');
			//event.preventDefault();
		});
		$('.page-scroll a[href^="#"]').bind('click', function(event) {
			var $anchor = $(this);
			$('html, body').stop().animate({
				scrollTop: $($anchor.attr('href')).offset().top
			}, 1000, 'easeInOutExpo');
			event.preventDefault();
		});
    });
})(jQuery);
</script>
</body>
</html>
