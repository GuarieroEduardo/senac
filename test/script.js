// Selecionando os elementos do popup e formulário
const modalPrimeiro = document.querySelector("#popupEditarProduto");
const modalSegundo = document.querySelector("#popupConcluir");
const modalTerceiro = document.querySelector("#CriacaoDeCampanha");

const buttonOpen = document.querySelector(".buttonOpen");
const buttonClose = document.querySelector(".buttonClose");
const buttonConcluir = document.querySelector(".buttonConcluir");
const buttonClose2 = document.querySelector(".buttonClose2");
const buttonLinkCampanha = document.querySelector(".CriarNovaCampanha");
const buttonClose3 = document.querySelector(".buttonClose3");

const produto = document.getElementById("Produto");
const quantidade = document.getElementById("Quantidade");
const preco = document.getElementById("Preco");
const campanhaCheckbox = document.getElementById("Campanha");

// inputs do segundo pop Up
const checkboxOption = document.getElementById('checkboxOption');
const checkboxlist = document.getElementById('checkboxlist');
// Seleciona todos os checkboxes dentro do segundo popup (popupConcluir)
const checkboxes = modalSegundo.querySelectorAll("input[type='checkbox']");

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

// Abrir o terceiro popup ao clicar em "Criar Campanha"
buttonLinkCampanha.addEventListener("click", function() {
    modalTerceiro.showModal();
});

// Fechar o terceiro popup
buttonClose3.addEventListener("click", function() {
    modalTerceiro.close();
});

// Adiciona um evento que verifica mudanças no campo de texto
checkboxlist.addEventListener('input', function() {
    if (checkboxlist.value !== '') {
        // Marca o checkbox correspondente
        checkboxOption.checked = true;
        // Desmarca todos os outros checkboxes
        for (let i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i] !== checkboxOption) {
                checkboxes[i].checked = false;
            }
        }
    } else {
        checkboxOption.checked = false; // Desmarca o checkbox caso o campo esteja vazio
    }
});

// verifica apenas um checkbox marcado por vez
for (let i = 0; i < checkboxes.length; i++) {
    checkboxes[i].addEventListener("change", function() {
        if (checkboxes[i].checked) {
            // Quando um checkbox é marcado, desmarca todos os outros
            for (let j = 0; j < checkboxes.length; j++) {
                if (j !== i) {
                    checkboxes[j].checked = false;
                }
            }
            // Limpa o campo de texto quando um checkbox que não é o checkboxOption é selecionado
            if (checkboxes[i] !== checkboxOption) {
                checkboxlist.value = '';
            }
        }
    });
}
