async function buscarDados() {
    try {
        
        const dados = await response.json();
        console.log(dados);
    } catch (error) {
        console.log(error);
    }
}