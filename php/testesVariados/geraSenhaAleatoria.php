<?php

    $chars = 'abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    $max = strlen($chars)-1;
    $senha = "";
    $tamanhoSenha = 8;
    for($i=0; $i < $tamanhoSenha; $i++)
    {
        $senha .= $chars{mt_rand(0, $max)};
    }

    echo $senha;

?>