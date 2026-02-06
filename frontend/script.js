fetch("http://127.0.0.1:8000/api/dashboard")
  .then(response => response.json())
  .then(data => {
    document.getElementById("total").innerText = data.total;
    document.getElementById("urgentes").innerText = data.urgentes;
    document.getElementById("normais").innerText = data.normais;

    document.getElementById("motivo").innerText = data.ultimo_chamado.motivo ?? "-";
    document.getElementById("descricao").innerText = data.ultimo_chamado.descricao ?? "-";
  })
  .catch(error => {
    console.error("Erro ao carregar dashboard:", error);
  });
