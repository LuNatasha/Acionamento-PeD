document.addEventListener("DOMContentLoaded", function () {

  const SEGMENTOS_FIXOS = [
    "SEGURANÇA HO",
    "CFTV IP",
    "CONTROLE DE ACESSO",
    "COMUNICAÇÃO HO",
    "SPEED DOME",
    "CAPTAÇÃO DE IMAGEM",
    "GERENCIAMENTO DE IMAGEM"
  ];

  const TURNOS_FIXOS = [
    "1° TURNO",
    "2° TURNO",
    "3° TURNO"
  ];

  const graficos = {};

  function criarOuAtualizarGrafico(canvasId, labels, valores) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) {
      console.error("Canvas não encontrado:", canvasId);
      return;
    }

    if (graficos[canvasId]) {
      graficos[canvasId].destroy();
      delete graficos[canvasId];
    }

    graficos[canvasId] = new Chart(canvas, {
      type: "bar",
      data: {
        labels: labels,
        datasets: [{
          data: valores,
          backgroundColor: "#6aa84f",
          borderRadius: 6,
          barThickness: 18
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: false,
        animation: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: ctx => ` ${ctx.raw} chamados`
            }
          }
        },
        scales: {
          x: {
            beginAtZero: true,
            ticks: { precision: 0, stepSize: 1 },
            grid: { color: "#e6e6e6" }
          },
          y: { grid: { display: false } }
        }
      }
    });
  }

  function setText(id, value) {
    const el = document.getElementById(id);
    if (el) {
      el.innerText = value;
    } else {
      console.error("Elemento não encontrado no HTML:", id);
    }
  }

  function carregarDashboard() {
    fetch("http://127.0.0.1:8000/api/dashboard")
      .then(r => r.json())
      .then(data => {
        console.log("Dashboard:", data);

        setText("total",    data.total    ?? 0);
        setText("urgentes", data.urgentes ?? 0);
        setText("normais",  data.normais  ?? 0);

        setText("ultimoSegmento", data.ultimo_chamado?.segmento  || "-");
        setText("ultimoMotivo",   data.ultimo_chamado?.motivo    || "-");
        setText("ultimoHora",     data.ultimo_chamado?.data_hora || "-");

        // Segmento
        const segmentosCompletos = {};
        SEGMENTOS_FIXOS.forEach(seg => {
          segmentosCompletos[seg] = data.segmentos?.[seg] ?? 0;
        });
        criarOuAtualizarGrafico(
          "graficoSegmento",
          Object.keys(segmentosCompletos),
          Object.values(segmentosCompletos)
        );

        // Motivo
        const listaMotivos = Object.entries(data.motivos || {}).sort((a, b) => b[1] - a[1]);
        criarOuAtualizarGrafico(
          "graficoMotivo",
          listaMotivos.length ? listaMotivos.map(i => i[0]) : ["Sem acionamentos"],
          listaMotivos.length ? listaMotivos.map(i => i[1]) : [0]
        );

        // Turno
        const turnosCompletos = {};
        TURNOS_FIXOS.forEach(t => {
          turnosCompletos[t] = data.turnos?.[t] ?? 0;
        });
        criarOuAtualizarGrafico(
          "graficoTurno",
          Object.keys(turnosCompletos),
          Object.values(turnosCompletos)
        );

      })
      .catch(err => console.error("Erro ao carregar dashboard:", err));
  }

  carregarDashboard();
  setInterval(carregarDashboard, 5000);

});