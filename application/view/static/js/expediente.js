var dia1 = new Date();
var hora1 = dia1.getHours();
var minuto1 = dia1.getMinutes();
if (hora == 11)
    document.write("Loja Aberta - Venha e faça agora mesmo o seu pedido.");

if ((hora == 12) && (minuto == 30))
    document.write("A loja aberta - Venha e faça agora mesmo o seu pedido. - promoção do dia: Hambúrguer Artesanal + Coca lata - R$10,99");

if (hora == 19)
    document.write("Quer Pedir seu lanche em casa? Já estamos aceitando pedidos.");

if (hora == 22)
    document.write("Fim do expediente. Te esperamos amanha novamente.");