<?php
include_once __DIR__ . "/../database/db.php";

class UserController
{
    private $conn;

    public function __construct()
    {
        $objDb = new Database();
        $this->conn = $objDb->connect();
    }

    
    public function Retorno($bool,$mensagem){
        $resposta = ["valor" => $bool, "msg" => $mensagem];
        return $resposta;
    }

    // Retorna todos os usuários
    public function GetAllUser()
    {
        try {
            $sql = "SELECT * FROM usuarios";
            $db = $this->conn->prepare($sql);
            $db->execute();
            return $db->fetchAll(PDO::FETCH_ASSOC);
        } catch (\Exception $th) {
            return $th->getMessage();
        }
    }

    public function GetUsers()
    {
        try {
            $sql = "SELECT id, nome FROM usuarios";
            $db = $this->conn->prepare($sql);
            $db->execute();
            return $db->fetchAll(PDO::FETCH_ASSOC);
        } catch (\Exception $th) {
            return $th->getMessage();
        }
    }

    public function GetAllEspacos()
    {
        try {
            $sql = "SELECT * FROM espacos";
            $db = $this->conn->prepare($sql);
            $db->execute();
            return $db->fetchAll(PDO::FETCH_ASSOC);
        } catch (\Exception $th) {
            return $th->getMessage();
        }
    }

    public function GetEspacos()
    {
        try {
            $sql = "SELECT id, nome FROM espacos";
            $db = $this->conn->prepare($sql);
            $db->execute();
            return $db->fetchAll(PDO::FETCH_ASSOC);
        } catch (\Exception $th) {
            return $th->getMessage();
        }
    }

    public function GetAllReservas()
    {
        try {
            $sql = "SELECT * FROM reservas";
            $db = $this->conn->prepare($sql);
            $db->execute();
            return $db->fetchAll(PDO::FETCH_ASSOC);
        } catch (\Exception $th) {
            return $th->getMessage();
        }
    }


    // Cria um usuário
    public function CreateUser($nome, $email, $telefone)
    {
        try {
            // Verifica se já existe um usuário com o mesmo e-mail
            $sqlCheck = "SELECT COUNT(*) as total FROM usuarios WHERE email = :email";
            $dbCheck = $this->conn->prepare($sqlCheck);
            $dbCheck->bindParam(":email", $email);
            $dbCheck->execute();
            $resultado = $dbCheck->fetch(PDO::FETCH_ASSOC);

            if ($resultado['total'] > 0) {
                return $this->Retorno(false, "Erro: Já existe um usuário cadastrado com este e-mail.");
            }

            // Insere o novo usuário caso o e-mail não esteja cadastrado
            $sql = "INSERT INTO usuarios (nome, email, telefone) VALUES (:nome, :email, :telefone)";
            $db = $this->conn->prepare($sql);
            $db->bindParam(":nome", $nome);
            $db->bindParam(":email", $email);
            $db->bindParam(":telefone", $telefone);

            if ($db->execute()) {
                return $this->Retorno(true, "Usuário cadastrado com sucesso.");
            } else {
                return $this->Retorno(false, "Erro ao cadastrar o usuário.");
            }
        } catch (\Exception $th) {
            return $this->Retorno(false, "Erro: " . $th->getMessage());
        }
    }

    // Atualiza um usuário
    public function UpdateUser($id, $nome, $email, $telefone)
    {
        try {
            $sql = "UPDATE usuarios SET nome = :nome, email = :email, telefone = :telefone WHERE id = :id";
            
            $db = $this->conn->prepare($sql);
            $db->bindParam(":nome", $nome);
            $db->bindParam(":email", $email);
            $db->bindParam(":telefone", $telefone);
            $db->bindParam(":id", $id);
            
            return $db->execute();
        } catch (\Exception $th) {
            return $th->getMessage();
        }
    }

    // Deleta um usuário
    public function DeleteUser($id)
    {
        try {
            $sql = "DELETE FROM usuarios WHERE id = :id";
            $db = $this->conn->prepare($sql);
            $db->bindParam(":id", $id);
            return $db->execute();
        } catch (\Exception $th) {
            return $th->getMessage();
        }
    }

    // Retorna um usuário pelo ID
    public function GetUserById($id)
    {
        try {
            $sql = "SELECT * FROM usuarios WHERE id = :id";
            $db = $this->conn->prepare($sql);
            $db->bindParam(":id", $id);
            $db->execute();
            return $db->fetch(PDO::FETCH_ASSOC);
        } catch (\Exception $th) {
            return $th->getMessage();
        }
    }

    public function CreateEspaco($nome, $tipo, $capacidade, $descricao)
    {
        try {
            $sql = "INSERT INTO espacos (nome, tipo, capacidade, descricao) 
                    VALUES (:nome, :tipo, :capacidade, :descricao)";
            
            $db = $this->conn->prepare($sql);
            $db->bindParam(":nome", $nome);
            $db->bindParam(":tipo", $tipo);
            $db->bindParam(":capacidade", $capacidade, PDO::PARAM_INT);
            $db->bindParam(":descricao", $descricao);

            return $db->execute();
        } catch (\Exception $th) {
            return $th->getMessage();
        }
    }

    public function UpdateEspaco($id, $nome, $tipo, $capacidade, $descricao)
    {
        try {
            $sql = "UPDATE espacos SET nome = :nome, tipo = :tipo, capacidade = :capacidade, descricao = :descricao WHERE id = :id";
            $db = $this->conn->prepare($sql);
            $db->bindParam(":nome", $nome);
            $db->bindParam(":tipo", $tipo);
            $db->bindParam(":capacidade", $capacidade, PDO::PARAM_INT);
            $db->bindParam(":descricao", $descricao);
            $db->bindParam(":id", $id, PDO::PARAM_INT);

            return $db->execute();
        } catch (\Exception $th) {
            return $th->getMessage();
        }
    }


    public function DeleteEspaco($id)
    {
        try {
            $sql = "DELETE FROM espacos WHERE id = :id";
            $db = $this->conn->prepare($sql);
            $db->bindParam(":id", $id);
            return $db->execute();
        } catch (\Exception $th) {
            return $th->getMessage();
        }
    }

    public function GetEspacoById($id)
    {
        try {
            $sql = "SELECT * FROM espacos WHERE id = :id";
            $db = $this->conn->prepare($sql);
            $db->bindParam(":id", $id);
            $db->execute();
            return $db->fetch(PDO::FETCH_ASSOC);
        } catch (\Exception $th) {
            return $th->getMessage();
        }
    }

    public function CreateReserva($usuario_id, $espaco_id, $data_reserva, $horario_inicio, $horario_fim, $quantidade)
    {
        try {
            // Obter a capacidade máxima do espaço
            $capacidadeSql = "SELECT capacidade FROM espacos WHERE id = :espaco_id";
            $capacidadeStmt = $this->conn->prepare($capacidadeSql);
            $capacidadeStmt->bindParam(":espaco_id", $espaco_id, PDO::PARAM_INT);
            $capacidadeStmt->execute();
    
            $espaco = $capacidadeStmt->fetch(PDO::FETCH_ASSOC);
            if (!$espaco) {
                return $this->Retorno(false,"Erro: Espaço não encontrado.");
            }
    
            $capacidadeMaxima = $espaco['capacidade'];
    
            // Verificar se a quantidade de convidados excede a capacidade
            if ($quantidade > $capacidadeMaxima) {
                return $this->Retorno(false,"Erro: A quantidade de convidados excede a capacidade do espaço (máximo: $capacidadeMaxima pessoas).");
            
            }
    
            // Verificar conflitos de horário
            $verificaSql = "SELECT COUNT(*) as total FROM reservas 
                            WHERE espaco_id = :espaco_id 
                            AND data_reserva = :data_reserva
                            AND (
                                (horario_inicio < :horario_fim AND horario_fim > :horario_inicio)
                            )";
    
            $verificaStmt = $this->conn->prepare($verificaSql);
            $verificaStmt->bindParam(":espaco_id", $espaco_id, PDO::PARAM_INT);
            $verificaStmt->bindParam(":data_reserva", $data_reserva);
            $verificaStmt->bindParam(":horario_inicio", $horario_inicio);
            $verificaStmt->bindParam(":horario_fim", $horario_fim);
            $verificaStmt->execute();
    
            $resultado = $verificaStmt->fetch(PDO::FETCH_ASSOC);
    
            if ($resultado['total'] > 0) {
                return $this->Retorno(false,"Erro: Já existe uma reserva para este espaço no horário selecionado.");
            }
    
            // Inserir a reserva
            $sql = "INSERT INTO reservas (usuario_id, espaco_id, data_reserva, horario_inicio, horario_fim, quantidade) 
                    VALUES (:usuario_id, :espaco_id, :data_reserva, :horario_inicio, :horario_fim, :quantidade)";
                
            $db = $this->conn->prepare($sql);
            $db->bindParam(":usuario_id", $usuario_id, PDO::PARAM_INT);
            $db->bindParam(":espaco_id", $espaco_id, PDO::PARAM_INT);
            $db->bindParam(":data_reserva", $data_reserva);
            $db->bindParam(":horario_inicio", $horario_inicio);
            $db->bindParam(":horario_fim", $horario_fim);
            $db->bindParam(":quantidade", $quantidade, PDO::PARAM_INT);
    
            if ($db->execute()) {
                return $this->Retorno(true,"Reserva criada com sucesso");
            } else {
                return $this->Retorno(false,"Erro: Falha ao criar a reserva.");
            }
        } catch (\Exception $th) {

            return "Erro: " . $th->getMessage();
        }
    }



    


    public function cancelarReserva($id)
    {
        try {
            $sql = "DELETE FROM reservas WHERE id = :id";
            $db = $this->conn->prepare($sql);
            $db->bindParam(":id", $id);
            return $db->execute();
        } catch (\Exception $th) {
            return $th->getMessage();
        }
    }


}
?>
