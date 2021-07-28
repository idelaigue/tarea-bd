<?php include '../include/header.html'; ?>
<body>
    <div class='container-fluid'>
        <div class='row justify-content-center mt-5'>
            <div class='container-6 shadow-lg rounded m-auto p-5'>
                <h1>Bienvenido</h1>
                <p>Ingrese sus datos para iniciar sesión.</p>
                <form action="/sesion/valida_login.php" method="POST">
                    <div class="form-group">
                        <label for="email">Correo Electrónico</label>
                        <input type="email" class="form-control" placeholder="correo@electronico.com" id="email" name = "email">
                    </div>
                    <div class="form-group">
                        <label for="pwd">Contraseña</label>
                        <input type="password" class="form-control" placeholder="Contraseña" id="pwd" name = "pwd">
                    </div>
                    <div class='d-flex justify-content-end'>
                        <button type="submit" class="btn btn-primary">Enviar <i class="fas fa-sign-in-alt"></i></button>
                    </div>
                </form>
            </div>
        </div>
    </div>


</body>

</html>