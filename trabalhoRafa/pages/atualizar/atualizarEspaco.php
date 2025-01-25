<?php
require_once __DIR__ . '/../../backend/login/userController.php';

$userController = new UserController();

// Verifica se o ID foi enviado
if (isset($_POST['id'])) {
    $id = $_POST['id'];


    // Busca os dados do espaço pelo ID
    $espaco = $userController->GetEspacoById($id);

    if ($espaco) {
       $id = htmlspecialchars($espaco['id']);
       $nome = htmlspecialchars($espaco['nome']);
       $tipo = htmlspecialchars($espaco['tipo']);
       $capacidade =  htmlspecialchars($espaco['capacidade']);
       $descricao = htmlspecialchars($espaco['descricao']);

    } else {
        die('Espaço não encontrado.');
    }
} else {
    
    die('ID não fornecido.');
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar Espaço</title>
    <link rel="stylesheet" href="../../styles.css">
</head>
<body class="pagina-editar-espaco">
    <section id="editar-espaco">
        <h2>Editar Espaço</h2>
        <form action="../../backend/router/userRouter.php?acao=atualizarEspaco" method="POST">
            <input type="hidden" name="id" value="<?= $id ?>" required>

            <label for="nome">Nome:</label>
            <input type="text" id="nome" name="nome" value="<?= $nome ?>" required>

            <label for="tipo">Tipo:</label>
            <input type="text" id="tipo" name="tipo" value="<?= $tipo ?>" required>

            <label for="capacidade">Capacidade:</label>
            <input type="text" id="capacidade" name="capacidade" value="<?= $capacidade ?>" required>

            <label for="descricao">Descrição:</label>
            <input type="text" id="descricao" name="descricao" value="<?= $descricao ?>" required>

            <button type="submit">Salvar Alterações</button>
        </form>
    </section>
</body>
</html>
