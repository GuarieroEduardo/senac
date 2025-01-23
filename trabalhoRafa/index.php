<?php
if(isset($_GET["erro"])){
    $mensagem_erro = "Usuário invalido!";
    
}else{
    $mensagem_erro = null;
}
?>

<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="login.css">
    <link rel="stylesheet" href="index.css">
</head>

<body>
    <form method="POST" action="backend/router/loginRouter.php?acao=validarLogin">
        <div>
            <input type="text" name="email" placeholder="email">
            <input type="text" name="senha" placeholder="senha">
            <button type="submit">Logar</button>
        </div>
    </form>
    <div class="msg-erro">
        <?php echo $mensagem_erro?> 
    </div>


</body>

</html>