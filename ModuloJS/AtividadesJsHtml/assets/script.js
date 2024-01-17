let message = "Conexao feita com sucesso!"

let connection = (n) => {
  for (let i = 0; i < 3; i++) {
    document.getElementById('message').innerHTML += n + "<br/>";
  }
};

window.onload = () => {
    connection(message);
}
