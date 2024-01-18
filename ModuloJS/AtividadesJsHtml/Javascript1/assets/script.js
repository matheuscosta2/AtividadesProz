const title = document.getElementById('titulo');
const unorderedList = document.querySelector('ul');
const link = document.querySelector('a');
const ordereList = document.getElementById('lista-ordenada');

title.innerText('lorem ipsum');
link.innerText('dolor sit amet');
unorderedList.innerHTML = ('<li>item1<li/><li>item2<li/><li>item3<li/>');
ordereList.innerHTML = ('<li><a href="www.prozeducacao.com.br">site1<a/><li/><li><a href="www.prozeducacao.com.br">site2<a/><li/><li><a href="www.prozeducacao.com.br">site3<a/><li/>')