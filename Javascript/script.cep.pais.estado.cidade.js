var estados = null;

//quando a página estiver carregada
$(document).ready(function () {

    //nesta primeira, quando o usuário clica no campo de CEP e 
    //sai ele vaipegar conteúdo
    //e jogar na API dos Correios para pesquisar o endereço 
    $("#CEP").focusout(function () {

        //pega o que estiver escrito no campo de texto com tag id = CEP
        var cep = $("#CEP").val();
        //checa se o que está escrito no campo é algo no formato 00000-000 (9 caracteres)
        if (cep.length == 9) {
            cep = cep.replace("-", "");

            var urlString = "https://viacep.com.br/ws/" + cep + "/json/";

            $.ajax({
                url: urlString,
                type: "get",
                dataType: "json",
                success: function (data) {
                    //jogando nas caixas de texto que têm tag id correspondentes
                    $("#bairroendereco").val(data.bairro);
                    $("#enderecoendereco").val(data.logradouro);
                    $("#complementoendereco").val(data.complemento);
                    $("#estadoendereco").val(data.uf);

                    //primeiro o estado é colocado e depois é passado para uma função para pesuqisar as cidades daquele estado,
                    //a API dos correios também retorna a cidade,porém elasó colocada no respectivo campo depois
                    //de a função abaixo pesquisar as cidades do estado, 
                    //senão o resultado da função de cidades iria sobrescrever  a cidade achada
                    popularMunicipios("#cidadeendereco", data.uf, data.localidade);

                },
                error: function (erro) {
                    console.log(erro);
                }
            });
        }
    });


    pesquisaEstadosBrasileiros();

    //caso o usuário trocar o estado
    //a lista de municípos será atualizada
    $("#coloque aqui a tag id do campo do estado para que coloque a lista de municípios").on("change", function () {
        popularMunicipios("#tag id do campo cidade que deseja popular", $("#tag id do campo estado que foi mudado").val(), "");
    });
});

//simplesmente pesquisa estados brasileiros
function pesquisaEstadosBrasileiros() {

    $.ajax({
        url: urlString,
        type: "get",
        dataType: "json",
        success: function (data) {

            estados = data;

            //para popular um select de estados
            populaEstados("#coloque aqui a tag id do campo do estado para que coloque a lista de estados");

        },
        error: function (erro) {
            console.log(erro);
        }
    });

}

//esta função prenche os municípios assim que o estado é preenchido  
function popularMunicipios(campopreenchido, siglaEstado, cidadeCEP) {

    if (siglaEstado.length > 0) {

        for (var i = 0; i < estados.length; i++) {

            if (estados[i].sigla == siglaEstado)
                idEstado = estados[i].id;

        }

        if (idEstado != "") {

            var urlString = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/" + idEstado + "/municipios";

            $.ajax({
                url: urlString,
                type: "get",
                dataType: "json",
                beforeSend: function (xhr) {
                    $(campopreenchido).attr('disabled', 'disabled');
                    $(campopreenchido).html('<option value="">Carregando...</option>');
                },
                success: function (data) {
                    console.log(data);
                    console.log(data.length);
                    $(campopreenchido).html('<option value="">Selecione</option>');
                    for (var i = 0; i < data.length; i++) {
                        // Adiciona o retorno no campo, habilita e da foco
                        $(campopreenchido).append('<option value="' + data[i].nome + '">' + data[i].nome + '</option>');
                    }
                    $(campopreenchido).removeAttr('disabled');

                    $(campopreenchido).val(cidadeCEP);
                },
                error: function (erro) {
                    console.log(erro);
                }
            });
        }

    }

}

//mando o campo que será preenchido e os dados foram buscados numa api e guardados numa variável global 
//esta função só recebe como parâmetro o id do campo que será preenchido com estados pesquisados
function populaEstados(campopreenchido) {

    $(campopreenchido).html('<option value="">Selecione</option>');
    for (var i = 0; i < estados.length; i++) {

        // Adiciona o retorno no campo, habilita e da foco
        $(campopreenchido).append('<option value="' + estados[i].sigla + '">' + estados[i].sigla + '</option>');
    }
}
