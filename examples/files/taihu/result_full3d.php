<!DOCTYPE html>
<html lang="en">
<head>
    <title>Taihu DSS 3D</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.18.1/vis.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.18.1/vis.min.js"></script>


    <style>
    body, html {
        width: 100%;
        height: 100%;
    }
    </style>

</head>
<body>
<?php
    $resultdir = 'result';
    $casename = '';

    if( count($_GET) == 4 ) {
        if( $_GET['c'] && $_GET['v'] ) {
            // $casename = sprintf('%s%08d', $_GET['pref'], intval($_GET['c']));
            $casename = sprintf($resultdir.'/%s%08d', $_GET['pref'], intval($_GET['c']));
            $varname  = $_GET['v'];

            if( $_GET['t'] >= 0){
                $itime = intval($_GET['t']);
            }
            if( $_GET['t'] == -9999){
                $itime = intval($_GET['t']);
            }

            // http://172.17.17.250/taihu/result_full3d.php?c=2&v=GREENS&t=4
            $jsonFile = '/taihu/'.$casename.'/map_'.$varname.'_t'.$itime.'.json';
        }
    }
?>
<div class="container-fluid" style="height:5%;background-color:#D3D3D3;">
    <div id="d3dmaptitle" class="row text-center">
        d3dmaptitle
    </div>
</div>
<div class="container-fluid" style="height:95%;">
    <div class="row" style="height:100%;">
        <div class="col-sm-12" style="height:100%;">
            <div id="graph" style="height:100%;"></div>
        </div>
    </div>
</div>

<script>
$( document ).ready(function() {
    var jsonFile = "<?php echo $jsonFile; ?>";

    //drawVisualization('df.json','graph');
    drawVisualization(jsonFile, 'graph', 'd3dmaptitle');
});

function drawVisualization(jsonFname,containerId,titleId) {
    var data = null;
    var data = new vis.DataSet();

    var jsonMapContainer = document.getElementById(containerId);
    var jsonMapTitle     = document.getElementById(titleId);

    $.ajax({
        url: jsonFname,
        dataType: "json",
        success: function(jsonData) {
            jsonMapTitle.innerHTML     = '';
            jsonMapContainer.innerHTML = '';

            for (var i = 0; i < jsonData['x'].length; i += 1) {
                data.add({
                    x: jsonData['x'][i],
                    y: jsonData['y'][i],
                    z: jsonData['z'][i],
                    style: jsonData['z'][i]
                });
            }

            var options = {
                width:  '100%',
                height: '100%',
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

            jsonMapTitle.innerHTML +=
                '<div class="col-sm-4">'
                    +'itime = '+jsonData['itime']
                +'</div>'
                +'<div class="col-sm-8">'
                    +'<a href="'+jsonFname+'" target="_blank">'+jsonFname+'</a>'
                +'</div>'
            graph3d = new vis.Graph3d(jsonMapContainer, data, options);
        },
        error: function(xhr,status,error) {
            var icon = '<i class="fa fa-exclamation-circle" aria-hidden="true"></i>';
            jsonMapContainer.innerHtml = icon + status + ", " + error;
        }
    });
}
</script>
</body>
</html>
