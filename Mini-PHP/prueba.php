<?php
require('document.php');
$bariable=7;
$suma;
$booleano = true;
$apellido = false;
$i = 2;
$a = $i + $apellido;
$negro = "vacinga";

function saludar($a, $b){
    if ($a<3){
      $a++;
     // $b++;
    }
    else
      return ($a+$b)/($a-$b);
}


function despedirse($despedida){
    echo "Nos vemos otro día, $despedida";
}

// Función de envoltura
function decirEsto($esto){
    echo $esto;
}

$var = 'saludar';
class ClaseSencilla{
  public $var = 0;
  public $var1 = 0;

  protected function mostrarVar() {
    return 0;
  }
}


echo "Ejemplo de print";
echo $verb;

if($a < 20){
  $v1 = 1;
  echo $v1;
  $suma = $v2 + $v3;
}
function foo() {
    echo "En foo()<br />\n";
}


// Esta es una función de envoltura alrededor de echo
function hacerecho($cadena)
{
    echo $cadena;
}
$func = 'foo';

$func = 'bar';

$func = 'hacerecho';

public function recursividad($a){
  **$d;
  &$d=$a;
  if($a < 20){
    $v1 = 1;
    echo $v1;
    $suma = $v2 + $v3;
    if($a>0 and $b<1 || $s<$d OR $a==2){
    }
  }

  public class prueba{
    protected function abs(){
      return 0;
    }
  }

  echo "esto es un print, se muestra en pantalla";

  switch($suma){
    case 1:
    $v1 = $variable + $v1;
    break;
    case 3:
    $v2 = $variable + $v2;
    break;
    case 4:
    $v3 = $variable;
    break;
    default:
    $v4 = $variable;
    break;
  }

  while($j<=$i){
    $v1 = $variable + $v1;
    echo "*&nbsp&nbsp";
    $j++;
  }

}


prueba $a=new prueba(VOID);



?>


