// Selecionando os elementos do popup
const modalPrimeiro = document.querySelector("#popupEditarProduto");
const modalSegundo = document.querySelector("#popupConcluir");

const buttonOpen = document.querySelector(".buttonOpen");
const buttonClose = document.querySelector(".buttonClose");

const buttonConcluir = document.querySelector(".buttonConcluir");
const buttonClose2 = document.querySelector(".buttonClose2");

// Abrir o primeiro popup
buttonOpen.addEventListener("click", function() {
    modalPrimeiro.showModal();
});

// Fechar o primeiro popup
buttonClose.addEventListener("click", function() {
    modalPrimeiro.close();
});

// Abrir o segundo popup ao clicar em "Concluir"
buttonConcluir.addEventListener("click", function() {
    const botaoCampanha = document.getElementById("Campanha")

    if (botaoCampanha.checked) {
        modalSegundo.showModal(); // Abre o segundo popup
    } else {
       
    }
});

// Fechar o segundo popup
buttonClose2.addEventListener("click", function() {
    modalSegundo.close();
});
