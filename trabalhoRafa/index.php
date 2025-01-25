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
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <header>

    <h1>Sistema de Agendamentos</h1>

    </header>


    <section id="reservar">
    <form action="/reservar" method="POST">


        <div>
            <a href="./pages/cadastro/cadastroUser.php" id="agendamento"><h3>Cadastrar Usuário</h3></a>
        </div>
        <div>
            <a href="./pages/cadastro/cadastroEspaco.php" id="agendamento"><h3>Cadastrar Espaço</h3></a>
        </div>
        <div>
            <a href="./pages/cadastro/reserva.php" id="agendamento"><h3>Reservar sala</h3></a>
        </div>

</form>
</section>


</body>

</html>