$("#formEscola").on('submit', function (event) {
    event.preventDefault();
    var dados = $(this).serialize();

    $.ajax({
        url: "controller/controllerEscola.php",
        type: 'post',
        dataType: 'json',
        data: dados,
        success: function (response) {
            $('.resultadoForm table tbody').empty();
            $.each(response, function (key, value) {
                $('.resultadoForm table tbody').append("<tr> <td>" + value.id + "</td> <td>" + value.nome + "</td> <td>" + value.nota + "</td> </tr> ");
            });
        }
    });
});


$("#formInserir").on('submit', function (event) {

    event.preventDefault();

    $.ajax({
        url: 'controller/insert.php',
        type: 'post',
        data: {
            nome: $("#nome_inserir").val(),
            nota: $("#nota_inserir").val(),
        },
        beforeSend: function () {
            $("#mensagens").html("Carregando...");
        },
        success: function (data) {
            $("#mensagens").html(data);
        },
        error: function (data) {
            $("#mensagens").html("Não conseguimos encontrar a página INSERT...");
        }
    });
});