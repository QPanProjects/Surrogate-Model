<?php
    echo '--php:Start::['.(new \DateTime())->format('Y-m-d H:i:s')."] run_sm.php\n";
    $_Ngen = 0;
    $_Ndim = 0;
    $_Npop = 0;
    $_Nobj = 0;
    $_Ncon = 0;
    $_CXPB = 0.0;

    $output = '';

    if( $_GET['ngen'] && $_GET['ndim'] && $_GET['npop'] && $_GET['nobj'] ) {
    //if( isset($_GET['ncon']) && !empty($_GET['ncon']) && $_GET['cxpb'] ) {
        $_Ngen = intval($_GET['ngen']);
        $_Ndim = intval($_GET['ndim']);
        $_Npop = intval($_GET['npop']);
        $_Nobj = intval($_GET['nobj']);
        $_Ncon = intval($_GET['ncon']);
        $_CXPB = floatval($_GET['cxpb']);

        if( $_Npop % 4 > 0 ){
            echo "--php:Error:: Remainder of Npop divided by 4 is not 0!\n";
            print_r($_GET);

        } elseif( $_Ndim != 82){
            echo "--php:Error:: Taihu DSS allowed Decision Variable size is 82\n";
            print_r($_GET);

        } else {
            $exe_py_cmd = 'python /var/www/html/taihu/run_sm.py'
                           .' -g '.$_Ngen
                           .' -d '.$_Ndim
                           .' -p '.$_Npop
                           .' -o '.$_Nobj
                           .' -c '.$_Ncon
                           .' -x '.$_CXPB
                           .' 2>&1';
            exec($exe_py_cmd,$output,$returnval);
            foreach( $output as $text ){ echo "$text\n"; }
        }

    } else {
        echo '--php:Error:: check input!\n';
        print_r($_GET);
    }
    echo '--php:End:: ['.(new \DateTime())->format('Y-m-d H:i:s')."]\n";
?>


<?php
//==============================
//==           TEST           ==
//==============================
//phpinfo();

//$exe_py_cmd = 'python /var/www/html/taihu/run_sm.py 2>&1';
//$exe_sh_cmd = '/var/www/html/taihu/run.sh 2>&1';
//$exe_php_cmd = 'php /var/www/html/taihu/run.php 2>&1';
//$exe_cgi_cmd = '/var/www/html/taihu/run.cgi 2>&1';

//========== Test ==========
// $output = shell_exec('php -v');
// $output = exec('echo $PATH');

// $output = shell_exec('/var/www/html/taihu/run.sh');
// $output = exec('/var/www/html/taihu/run.sh');

//========== Python needed! ==========
// echo '<p style="color:red;">py-start: '.(new \DateTime())->format('Y-m-d H:i:s').'</p>';
// exec($exe_py_cmd,$output,$returnval);
// foreach($output as $text){echo "$text<br>";}
// echo '<p style="color:green;">output</p>';print_r($output);
// echo '<p style="color:blue;">returnval</p>'.print_r($returnval);

//========== Shell ==========
// echo '<p style="color:red;">sh: '.(new \DateTime())->format('Y-m-d H:i:s').'</p>';
// exec($exe_sh_cmd,$output,$returnval);
// foreach($output as $text){echo "$text<br>";}
// echo '<p style="color:green;">output</p>';print_r($output);
// echo '<p style="color:blue;">returnval</p>'.print_r($returnval);

//========== PhP shell ==========
// echo '<p style="color:red;">php: '.(new \DateTime())->format('Y-m-d H:i:s').'</p>';
// exec($exe_php_cmd,$output,$returnval);
// foreach($output as $text){echo "$text<br>";}
// echo '<p style="color:green;">output</p>';print_r($output);
// echo '<p style="color:blue;">returnval</p>'.print_r($returnval);

//========== CGI ==========
// echo '<p style="color:red;">cgi: '.(new \DateTime())->format('Y-m-d H:i:s').'</p>';
// exec($exe_cgi_cmd,$output,$returnval);
// foreach($output as $text){echo "$text<br>";}
// echo '<p style="color:green;">output</p>';print_r($output);
// echo '<p style="color:blue;">returnval</p>'.print_r($returnval);
?>
