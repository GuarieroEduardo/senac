<?php
require_once __DIR__ . '/../../backend/login/userController.php';

$userController = new UserController();

// Obtém todos os usuários
$reservas = $userController->GetAllReservas();
$usuarios = $userController->GetUsers();
$espacos = $userController->GetEspacos();

// Verifica se há uma mensagem de resposta
$erro = isset($_GET['erro']) ? htmlspecialchars($_GET['erro']) : '';

?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reserva de Salas</title>
    <link rel="stylesheet" href="../../styles.css">
</head>
<body>

    <!-- Modal de erro -->
    <div id="modalErro" class="modal" style="display: <?= empty($erro) ? 'none' : 'block' ?>;">
        <div class="modal-content">
            <p id="mensagemErro"><?= $erro ?></p>
            <button id="fecharModalBtn" onclick="fecharModal()">Fechar</button>
        </div>
    </div>

    <section id="reservar">
        <h2>Reserva de Sala</h2>
        <form action="../../backend/router/userRouter.php?acao=cadastrarReserva" method="POST">
            <label for="usuario">Usuário:</label>
            <select id="usuario" name="usuario_id" required>
                <?php foreach ($usuarios as $usuario): ?>
                    <option value="<?= htmlspecialchars($usuario['id']) ?>"><?= htmlspecialchars($usuario['nome']) ?></option>
                <?php endforeach; ?>
            </select>

            <label for="espaco">Espaço:</label>
            <select id="espaco" name="espaco_id" required>
                <?php foreach ($espacos as $espaco): ?>
                    <option value="<?= htmlspecialchars($espaco['id']) ?>"><?= htmlspecialchars($espaco['nome']) ?></option>
                <?php endforeach; ?>
            </select>
            
            <label for="quantidade">Quantidade de Convidados:</label>
            <input type="number" id="quantidade" name="quantidade" required min="1" max="100">

            <label for="data">Data:</label>
            <input type="date" id="data" name="data_reserva" required>

            <label for="hora">Horário de Início:</label>
            <input type="time" id="hora" name="horario_inicio" required>

            <label for="hora_fim">Horário de Término:</label>
            <input type="time" id="hora_fim" name="horario_fim" required>

            <button type="submit">Concluir</button>
        </form>
    </section>

    <section id="agenda">
        <h2>Lista de Reservas</h2>
        <table>
            <thead>
                <tr>
                    <th>Espaço</th>
                    <th>Data</th>
                    <th>Horário (inicio/fim)</th>
                    <th>Usuário</th>
                    <th>Convidados</th>
                    <th>Ações</th>
                </tr>
            </thead>

            <tbody>
                <?php if (!empty($reservas) && is_array($reservas)): ?>
                    <?php foreach ($reservas as $reserva): ?>
                        <tr>
                            <?php 
                                // Encontrando o nome do espaço
                                $espaco_nome = "";
                                foreach ($espacos as $espaco) {
                                    if ($espaco['id'] == $reserva['espaco_id']) {
                                        $espaco_nome = $espaco['nome'];
                                        break;
                                    }
                                }
                                
                                // Encontrando o nome do usuário
                                $usuario_nome = "";
                                foreach ($usuarios as $usuario) {
                                    if ($usuario['id'] == $reserva['usuario_id']) {
                                        $usuario_nome = $usuario['nome'];
                                        break;
                                    }
                                }
                            ?>
                            <td><?= htmlspecialchars($espaco_nome) ?></td>
                            <td><?= htmlspecialchars($reserva['data_reserva']) ?></td>
                            <td><?= htmlspecialchars($reserva['horario_inicio']) ?> - <?= htmlspecialchars($reserva['horario_fim']) ?></td>
                            <td><?= htmlspecialchars($usuario_nome) ?></td>
                            <td><?= htmlspecialchars($reserva['quantidade']) ?></td>
                            <td>
                                <form action="../../backend/router/userRouter.php?acao=cancelarReserva" method="POST">
                                    <input type="hidden" name="id" value="<?= $reserva['id'] ?>">
                                    <button type="submit" class="cancelar" onclick="return confirm('Tem certeza que deseja cancelar esta reserva?')">Cancelar</button>
                                </form>
                            </td>
                        </tr>
                    <?php endforeach; ?>
                <?php else: ?>
                    <tr><td colspan="6">Nenhuma reserva encontrada</td></tr>
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


