<?php
require_once __DIR__ . '/../../backend/login/userController.php';

$userController = new UserController();


// Obtém todos os usuários
$usuarios = $userController->GetAllUser();
$erro = isset($_GET['erro']) ? htmlspecialchars($_GET['erro']) : '';
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro Usuário</title>
    <link rel="stylesheet" href="../../styles.css">
</head>
<body>

    <div id="modalErro" class="modal" style="display: <?= empty($erro) ? 'none' : 'block' ?>;">
        <div class="modal-content">
            <p id="mensagemErro"><?= $erro ?></p>
            <button id="fecharModalBtn" onclick="fecharModal()">Fechar</button>
        </div>
    </div>

    <section id="reservar">
        <h2>Cadastro Usuário</h2> 
        <form action="../../backend/router/userRouter.php?acao=cadastrar" method="POST">
            
            <label for="nome">Nome:</label>
            <input type="text" id="nome" name="nome" required>

            <label for="email">E-mail:</label>
            <input type="email" id="email" name="email" required>

            <label for="telefone">Telefone:</label>
            <input type="text" id="telefone" name="telefone" required>

            <button type="submit">Concluir</button>
        </form>

    </section>

    <section id="cadastro-usuario">
        <h2>Lista de Usuários</h2>
        <table>
            <thead>
                <tr>
                    <th>Nome</th>
                    <th>E-mail</th>
                    <th>Telefone</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                <?php if (!empty($usuarios) && is_array($usuarios)): ?>
                    <?php foreach ($usuarios as $usuario): ?>
                        <tr>
                        
                            <td><?= htmlspecialchars($usuario['nome']) ?></td>
                            <td><?= htmlspecialchars($usuario['email']) ?></td>
                            <td><?= htmlspecialchars($usuario['telefone']) ?></td>
                            <td>
                                <form action="../atualizar/atulizarUser.php" method="POST">
                                    <input type="hidden" name="id" value="<?= $usuario['id'] ?>">
                                    <button type="submit" class="editar">Editar</button>
                                </form>
                                <form action="../../backend/router/userRouter.php?acao=deletar" method="POST">
                                    <input type="hidden" name="id" value="<?= $usuario['id'] ?>">
                                    <button type="submit" class="excluir" onclick="return confirm('Tem certeza que deseja excluir?')">Excluir</button>
                                </form>
                            </td>
                        </tr>
                    <?php endforeach; ?>
                <?php else: ?>
                    <tr><td colspan="4">Nenhum usuário cadastrado</td></tr>
                <?php endif; ?>
            </tbody>
        </table>
    </section>

    <script>
        function fecharModal() {
            document.getElementById('modalErro').style.display = 'none';
        }

        // Ocultar modal caso não haja erro
        window.onload = function() {
            
            var erro = "<?= $erro ?>";
            if (!erro) {
                document.getElementById('modalErro').style.display = 'none';
            }
        };
    </script>
    </script>

</body>
</html>
