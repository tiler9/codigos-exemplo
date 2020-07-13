<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>Escola</title>
</head>

<body>

    <div class="resultadoForm">
        <table>
            <thead>
                <tr>
                    <td>ID</td>
                    <td>NOME</td>
                    <td>NOTA</td>
                </tr>
            </thead>
            <tbody></tbody>
        </table>
    </div>

    <form name="formEscola" id="formEscola" action="controller/controllerEscola" method="post">

        <input type="text" name="busca" id="busca"><br>
        <input type="submit" value="Pesquisa">

    </form>


    <br><br><br>

    <form name="formInserir" id="formInserir" action="controller/insert" method="post">

        <span>Nome: </span>
        <input type="text" name="nome_inserir" id="nome_inserir">

        <span>Nota: </span>
        <input type="text" name="nota_inserir" id="nota_inserir">
        <br><br>

        <input type="submit" value="Salvar">
    </form>


    <br><br>
    <div id="mensagens">
    </div>


    <script src="lib/zepto.min.js"></script>
    <script src="lib/javascript.js"></script>
</body>

</html>