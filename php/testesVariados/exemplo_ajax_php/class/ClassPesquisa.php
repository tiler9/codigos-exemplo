<?php
include("ClassConexao.php");
class ClassPesquisa extends ClassConexao{

    public function pesquisaDb($busca){
        $buscaLike = '%'.$busca.'%';
        $crud = $this->conectaDB()->prepare("SELECT * FROM boletim where nome like :busca");
        $crud->bindValue(':busca', $buscaLike);
        $crud->execute();
        return $f = $crud->fetchAll();
    }

    public function insertRegistro($nome, $nota){
        $sqlInsert = $this->conectaDB()->prepare("INSERT INTO boletim (nome, nota) VALUES ('".$nome."','".$nota."')");

        $sqlInsert->execute();

        if($sqlInsert == true)
            return "Cadastrado com sucesso";
        else
            return "Houve um erro durante o cadastro";
    }
}

?>