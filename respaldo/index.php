<?php include 'db_config.php';?>
<!DOCTYPE html>
<html>
<head>
<title>Informe COVID</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
</head>
<body>

<h1 style="color:blue">Informe COVID-19</h1>
<form action="form.php" method="POST">
    <div class="form-group">
      <label for="país">País</label>
      <input type="país" class="form-control" name="pais" placeholder="Ingresa tu país" id="país">
    </div>
    <div class="form-group">
      <label for="nro_cont">Número de contagiados:</label>
      <input type="number" class="form-control" name="nro_cont" placeholder="Ingresa el Número de contagiados" id="nro_cont">
    </div>
    <button type="submit" class="btn btn-primary">Enviar</button>
</form> 

</body>
</html> 