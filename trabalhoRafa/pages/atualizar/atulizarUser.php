<?php
require_once __DIR__ . '/../../backend/login/userController.php';

$userController = new UserController();

// Verifica se o ID foi enviado
if (isset($_POST['id'])) {
    $id = $_POST['id'];

    // Busca os dados do espaço pelo ID
    $usuario = $userController->GetUserById($id);

    if ($usuario) {
       $id = htmlspecialchars($usuario['id']);
       $nome = htmlspecialchars($usuario['nome']);
       $email = htmlspecialchars($usuario['email']);
       $telefone =  htmlspecialchars($usuario['telefone']);

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
<body class="pagina-editar-usuario">
    <section id="editar-usuario">
        <h2>Editar Espaço</h2>
        <form action="../../backend/router/userRouter.php?acao=update" method="POST">
            <input type="hidden" name="id" value="<?= $id ?>" required>

            <label for="nome">Nome:</label>
            <input type="text" id="nome" name="nome" value="<?= $nome ?>" required>

            <label for="email">Email:</label>
            <input type="text" id="email" name="email" value="<?= $email ?>" required>

            <label for="telefone">Telefone:</label>
            <input type="text" id="telefone" name="telefone" value="<?= $telefone ?>" required>

            <button type="submit">Salvar Alterações</button>
        </form>
    </section>
</body>
</html>



