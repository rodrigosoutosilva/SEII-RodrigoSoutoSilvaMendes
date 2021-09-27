var valor; /*valor digitado*/
var resultado; /*conta realizada*/

function botao(num){/*função que rastreia o botão apertado*/
    valor = document.calc.visor.value += num;
}

function reseta(num){/*função que rastreia o botão C*/
    document.calc.visor.value = '';
}

function calcula(){/*função que rastreia o botão =*/
    resultado = eval(valor);
    document.calc.visor.value = resultado.toLocaleString('pt-br');
}
