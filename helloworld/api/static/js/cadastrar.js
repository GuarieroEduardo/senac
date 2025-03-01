 async function enviarFormulario(evento) {
    evento.preventDefault();

    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;

    const resposta = await fetch('/api/alunos/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            nome: nome,
            email: email
        })  
        
    });
    if (resposta.ok) {
        window.location.href = '/home';
    }else{
        document.getElementById('menagemErro').innerHTML = 'Erro ao cadastrar aluno';
    }
} 

document.getElementById('alunoForm').addEventListener('submit', enviarFormulario)