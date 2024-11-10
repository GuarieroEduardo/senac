// Selecionando os elementos do popup e formulário
const modalPrimeiro = document.querySelector("#popupEditarProduto");
const modalSegundo = document.querySelector("#popupConcluir");

const buttonOpen = document.querySelector(".buttonOpen");
const buttonClose = document.querySelector(".buttonClose");
const buttonConcluir = document.querySelector(".buttonConcluir");
const buttonClose2 = document.querySelector(".buttonClose2");

const produto = document.getElementById("Produto");
const quantidade = document.getElementById("Quantidade");
const preco = document.getElementById("Preco");
const campanhaCheckbox = document.getElementById("Campanha");

// Função para exibir erros
function ShowError(input, mensagem) {
    const formControl = input.parentElement;
    const small = formControl.querySelector("small");
    small.textContent = mensagem;
    small.classList.add("error"); 
}

// Função para remover erros
function ShowSucesso(input) {
    const formControl = input.parentElement;
    const small = formControl.querySelector("small");
    small.classList.remove("error");
}

// Função de validação dos campos obrigatórios
function checkRequired(inputs) {
    let isValid = true;
    inputs.forEach(function(input) {
        if (input.value.trim() === "") {
            ShowError(input, "Campo obrigatório");
            isValid = false;
        } else {
            ShowSucesso(input);
        }
    });
    return isValid;
}

// Função para validar o checkbox de Campanha
function checkCampanhaRequired() {
    if (!campanhaCheckbox.checked) {
        ShowError(campanhaCheckbox, "*"); // Exibe o asterisco como erro no campo Campanha
        return false;
    } else {
        ShowSucesso(campanhaCheckbox);
        return true;
    }
}

// Função para abrir o primeiro popup
buttonOpen.addEventListener("click", function() {
    modalPrimeiro.showModal();
});

// Função para fechar o primeiro popup
buttonClose.addEventListener("click", function() {
    modalPrimeiro.close();
});

// Abrir o segundo popup ao clicar em "Concluir"
// Se todos os campos e o checkbox de campanha estiverem marcado mudara de popUp
buttonConcluir.addEventListener("click", function() {
    let isFormValid = checkRequired([produto, quantidade, preco]);
    let isCampanhaValid = checkCampanhaRequired();

    if (isFormValid && isCampanhaValid) {
        modalSegundo.showModal();
    }
});

// Fechar o segundo popup
buttonClose2.addEventListener("click", function() {
    modalSegundo.close();
});
