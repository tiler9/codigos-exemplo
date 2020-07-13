<?php

include "../class/ClassPesquisa.php";

$nome = filter_input(INPUT_POST, 'nome', FILTER_SANITIZE_SPECIAL_CHARS);
$nota = filter_input(INPUT_POST, 'nota', FILTER_SANITIZE_SPECIAL_CHARS);

$pesquisa = new ClassPesquisa();
$retorno = $pesquisa->insertRegistro($nome, $nota);

echo json_encode($retorno);
?>