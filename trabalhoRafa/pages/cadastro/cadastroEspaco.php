<?php
require_once __DIR__ . '/../../backend/login/userController.php';

$userController = new UserController();

$espacos = $userController->GetAllEspacos();
$erro = isset($_GET['erro']) ? htmlspecialchars($_GET['erro']) : '';

?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Espaços</title>
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
        <h2>Cadastro Espaços</h2>
        <form action="../../backend/router/userRouter.php?acao=cadastrarEspaco"  method="POST">
            <label for="nome">Nome:</label>
            <input type="text" id="nome" name="nome" required>
            
            <label for="espaco">Tipo:</label>
            <input type="text" id="tipo" name="tipo" required>
            
            
            <label for="capacidade">Capacidade:</label>
            <input type="number" id="capacidade" name="capacidade" min="1" max="100" required>
            
            
            <label for="descricao">Descrição:</label>
            <input type="text" id="descrição" name="descricao" required>


            <button type="submit">Concluir</button>
        </form>
    </section>

    <section id="cadastro-espacos">
        <h2>Lista de Espaços</h2>
        <table>
            <thead>
                <tr>
                    <th>Nome</th>
                    <th>Tipo</th>
                    <th>Capacidade</th>
                    <th>Descrição</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                <?php if (!empty($espacos) && is_array($espacos)): ?>
                    <?php foreach ($espacos as $espaco): ?>
                        <tr>
                            <td><?= htmlspecialchars($espaco['nome']) ?></td>
                            <td><?= htmlspecialchars($espaco['tipo']) ?></td>
                            <td><?= htmlspecialchars($espaco['capacidade']) ?></td>
                            <td><?= htmlspecialchars($espaco['descricao']) ?></td>
                            <td>
                            <!-- Formulário para editar -->
                                <form action="../atualizar/atualizarEspaco.php" method="POST" >
                                    <input type="hidden" name="id" value="<?= $espaco['id'] ?>">
                                    <button type="submit" class="editar">Editar</button>
                                </form>
                            <!-- Formulário para excluir -->
                                <form action="../../backend/router/userRouter.php?acao=deletarEspaco" method="POST">
                                    <input type="hidden" name="id" value="<?= $espaco['id'] ?>">
                                    <button type="submit" class="excluir" onclick="return confirm('Tem certeza que deseja excluir?')">Excluir</button>
                                </form>
                            </td>
                        </tr>
                    <?php endforeach; ?>
                <?php else: ?>
                    <tr><td colspan="5">Nenhum espaço cadastrado</td></tr>
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