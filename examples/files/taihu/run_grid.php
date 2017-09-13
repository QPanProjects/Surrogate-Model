<?php
    echo '--php:Start::['.(new \DateTime())->format('Y-m-d H:i:s')."] run_grid.php\n";
    $strCaseStart = 'iswaq';
    $strCaseEnd = 'iewaq';

    if( $_GET[$strCaseStart] && $_GET[$strCaseEnd] ) {
        $icaseStart = (int)$_GET[$strCaseStart];
        $icaseEnd = (int)$_GET[$strCaseEnd];

        if( $icaseStart > $icaseEnd ){
            echo '--php:Error:: <strong>Start</strong> is larger than <strong>End</strong>!';
            print_r($_GET);

        } else {
            $exe_py_cmd = 'python /var/www/html/taihu/run_grid.py'
                           .' -s '.$icaseStart
                           .' -e '.$icaseEnd
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

//$exe_py_cmd = 'python /var/www/html/taihu/run_waq.py 2>&1';
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
