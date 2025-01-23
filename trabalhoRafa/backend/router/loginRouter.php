<?php
require_once __DIR__ . "/../login/loginController.php";
$loginController = new LoginController();

if($_SERVER["REQUEST_METHOD"] == "POST"){
    
    switch ($_GET["acao"]) {
        case 'validarLogin':
            $email = $_POST["email"];
            $senha = $_POST["senha"];

            if(!(empty($email) || empty($senha))){
                $resposta = $loginController->Login($email, $senha);
                if($resposta){
                    header("Location: ../../pages/home/index.php");
                }else{
                    header("location: ../../index.php?erro=true");
                }
            }else{
                header("location: ../../index.php");
            }
            break;
        
        default:
            echo "nao achei nenhuma das opções";
            break;
    }

}
