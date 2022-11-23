<?php

    ini_set('max_execution_time', 30000);

    if(isset($_GET["id"])){
        $python = "C:\\ProgramData\\Anaconda3\\python.exe";
        
        if($_GET["id"]==2){
            $file = "C:\\xampp\\htdocs\\try_HBA\\stop.py";
            $output=exec($python . " " . $file);
            echo "stop is called";
            echo "<br>" . $output;
 			echo "<br>" ;

        }elseif($_GET["id"]==1){
            echo 'id=' . $_GET["id"];
            $file = "C:\\xampp\\htdocs\\try_HBA\\launcher.py";
            $output=exec($python . " " . $file);
            echo "started";
            
        }
    }else{
        echo "Invalid request";
    }
    
?>