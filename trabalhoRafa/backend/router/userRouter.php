<?php

require_once __DIR__ . "/../login/userController.php";
$userController = new UserController();

if($_SERVER["REQUEST_METHOD"] == "POST"){
    
    switch ($_GET["acao"]) {
        case 'cadastrar':
            $nome = $_POST["nome"];
            $email = $_POST["email"];
            $telefone = $_POST["telefone"];

            if(!(empty($nome) || empty($email) || empty($telefone))){
                $resposta = $userController->CreateUser($nome, $email, $telefone);

                if($resposta["valor"]){
                    header("Location: ../../index.php"); // Redireciona para a página inicial
                    exit;
                }else {
                    header("Location: ../../pages/cadastro/cadastroUser.php?erro={$resposta['msg']}");
                    exit;
                    
                }
    
            }
            break;

        case "update":
            if (isset($_POST["id"])){
                $nome = $_POST["nome"];
                $email = $_POST["email"];
                $telefone = $_POST["telefone"];
                if(!(empty($nome) || empty($email)) || empty($telefone)){
                    $resposta = $userController->UpdateUser($_POST["id"],$nome,$email, $telefone);
                    if($resposta){
                        header("Location: ../../index.php");
                    }
                }
            }
            break;

        case "deletar":
            if (isset($_POST["id"])) {
                $id = $_POST["id"];
                echo "ID a ser deletado: " . htmlspecialchars($id) . "<br>";
            
                $resultado = $userController->DeleteUser($id);
        
                if ($resultado) {
                    echo "Usuário deletado com sucesso!<br>";
                    header("Location: ../../index.php");
                    exit;
                } else {
                    echo "Erro ao deletar o usuário.<br>";
                }
            } else {
                echo "ID não fornecido para exclusão.<br>";
            }
            break;
        
        
        case 'cadastrarEspaco':
            $nome = $_POST["nome"];
            $tipo = $_POST["tipo"];
            $capacidade = $_POST["capacidade"];
            $descricao = $_POST["descricao"];
            
            if (!(empty($nome) || empty($tipo) || empty($capacidade) || empty($descricao))) {
                $resposta = $userController->CreateEspaco($nome, $tipo, $capacidade, $descricao);
                echo $resposta;
                if ($resposta) {
                    header("Location: ../../index.php"); // Redireciona para a página inicial
                    exit;
                }
            } else {
                echo "Todos os campos devem ser preenchidos.";
            }
            break;

        case "atualizarEspaco":
            echo "tentei";
            if (isset($_POST["id"])){
                $id = $_POST['id'];
                $nome = $_POST['nome'];
                $tipo = $_POST['tipo'];
                $capacidade = $_POST['capacidade'];
                $descricao = $_POST['descricao'];
            
                $resultado = $userController->UpdateEspaco($id, $nome, $tipo, $capacidade, $descricao);
                echo $resultado;
            }
        
            if ($resultado) {
                echo "Espaço atualizado com sucesso!";
                header("Location: ../../index.php");
            } else {
                echo "Erro ao atualizar espaço.";
            }
            break;
        
            

        case "deletarEspaco":
            if (isset($_POST["id"])) {
                $id = $_POST["id"];
                echo "ID a ser deletado: " . htmlspecialchars($id) . "<br>";
            
                $resultado = $userController->DeleteEspaco($id);
            
                if ($resultado) {
                    echo "Usuário deletado com sucesso!<br>";
                    header("Location: ../../index.php");
                    exit;
                } else {
                    echo "Erro ao deletar o usuário.<br>";
                }
            } else {
                echo "ID não fornecido para exclusão.<br>";
            }
            break;

            case 'cadastrarReserva':
                $usuario_id = $_POST["usuario_id"];
                $espaco_id = $_POST["espaco_id"];
                $data_reserva = $_POST["data_reserva"];
                $horario_inicio = $_POST["horario_inicio"];
                $horario_fim = $_POST["horario_fim"];
                $quantidade = $_POST["quantidade"]; // Novo campo para quantidade de convidados
            
                // Verificar se todos os campos foram preenchidos
                if (!(empty($usuario_id) || empty($espaco_id) || empty($data_reserva) || empty($horario_inicio) || empty($horario_fim) || empty($quantidade))) {
                    // Chamar o método para criar a reserva
                    $resposta = $userController->CreateReserva($usuario_id, $espaco_id, $data_reserva, $horario_inicio, $horario_fim, $quantidade);
                    
                    // Verificar a resposta do método

                    if($resposta["valor"]){
                        header("Location: ../../index.php"); // Redireciona para a página inicial
                        exit;
                    }else {
                        header("Location: ../../pages/cadastro/reserva.php?erro={$resposta['msg']}");
                        exit;
                        
                    }
                    
                } else {
                    echo "Todos os campos devem ser preenchidos.";
                }
                break;
            

        
        case "cancelarReserva":
            if (isset($_POST["id"])) {
                $id = $_POST["id"];
                echo "ID da reserva a ser cancelada: " . htmlspecialchars($id) . "<br>";
            
                $resultado = $userController->cancelarReserva($id);
            
                if ($resultado) {
                    echo "Reserva cancelada com sucesso!<br>";
                    header("Location: ../../index.php"); // Substitua pelo caminho correto do seu frontend
                    exit;
                } else {
                    echo "Erro ao cancelar a reserva.<br>";
                }
            } else {
                echo "ID da reserva não fornecido para cancelamento.<br>";
            }
            break;
            


        default:
            echo "nao achei nenhuma das opções";
            break;
    }

}
