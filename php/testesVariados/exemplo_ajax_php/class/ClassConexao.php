<?php

class ClassConexao{
    public function conectaDB(){
        try{
            $con = new PDO('mysql:host=localhost:3308;dbname=escola','root','');
            return $con;
        }catch(PDOException $ex){
            echo $ex->getMessage();
        }
    } 
}


?>