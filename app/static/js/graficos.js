const GRID_COLOR  = 'rgba(120,120,120,0.12)';
const TEXT_COLOR  = '#888888';

function formatBRL(value) {
  return 'R$ ' + Number(value).toLocaleString('pt-BR', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2
  });
}

function formatBRLCompact(value) {
  const n = Number(value);
  if (n >= 1_000_000) return 'R$ ' + (n / 1_000_000).toFixed(1).replace('.', ',') + 'M';
  if (n >= 1_000)     return 'R$ ' + (n / 1_000).toFixed(0) + 'k';
  return 'R$ ' + n.toFixed(0);
}

// ============================================================
//  Gráfico 1 — Receita Líquida Mensal  (linha com área)
//  KPI: receita_liquida  |  Temporal
// ============================================================
function criarGrafico1(idCanvas, titulo, labels, valores) {
  const el = document.getElementById(idCanvas);
  if (!el) { console.error('Canvas não encontrado:', idCanvas); return; }

  return new Chart(el, {
    type: 'line',
    data: {
      labels,
      datasets: [{
        label: 'Receita Líquida (R$)',
        data: valores,
        borderColor:          '#185FA5',
        backgroundColor:      'rgba(24,95,165,0.08)',
        borderWidth:          2.5,
        pointBackgroundColor: '#185FA5',
        pointBorderColor:     '#ffffff',
        pointBorderWidth:     2,
        pointRadius:          4,
        pointHoverRadius:     6,
        fill:                 true,
        tension:              0.4,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      interaction: { mode: 'index', intersect: false },
      plugins: {
        title: {
          display: true,
          text: titulo,
          font: { size: 13, weight: '500' },
          color: TEXT_COLOR,
          padding: { bottom: 10 }
        },
        legend: { display: false },
        tooltip: {
          callbacks: { label: ctx => formatBRL(ctx.parsed.y) }
        }
      },
      scales: {
        x: {
          title: { display: true, text: 'Mês', color: TEXT_COLOR, font: { size: 11 } },
          grid: { display: false },
          ticks: { color: TEXT_COLOR, font: { size: 11 } }
        },
        y: {
          beginAtZero: true,
          title: { display: true, text: 'Receita (R$)', color: TEXT_COLOR, font: { size: 11 } },
          grid: { color: GRID_COLOR, borderDash: [4, 4] },
          ticks: {
            color: TEXT_COLOR,
            font: { size: 11 },
            callback: v => formatBRLCompact(v)
          }
        }
      }
    }
  });
}

// ============================================================
//  Gráfico 2 — Receita Total por Filial  (barras horizontais)
//  KPI: receita_liquida por filial  |  Comparativo
//  Rótulos de valor desenhados DENTRO de cada barra
// ============================================================
function criarGrafico2(idCanvas, titulo, labels, valores) {
  const el = document.getElementById(idCanvas);
  if (!el) { console.error('Canvas não encontrado:', idCanvas); return; }

  // Ordena decrescente (maior receita no topo)
  const pares = labels.map((l, i) => ({ label: l, valor: valores[i] }));
  pares.sort((a, b) => b.valor - a.valor); // decrescente: maior no topo
  const labelsOrd  = pares.map(p => p.label);
  const valoresOrd = pares.map(p => p.valor);

  // Intensidade de azul proporcional ao valor
  const max = valoresOrd[0]; // após ordenação decrescente, maior está no índice 0
  const bgColors = valoresOrd.map(v => {
    const alpha = 0.35 + 0.65 * (v / max);
    return 'rgba(24, 95, 165, ' + alpha.toFixed(2) + ')';
  });

  return new Chart(el, {
    type: 'bar',
    data: {
      labels: labelsOrd,
      datasets: [{
        label: 'Receita Total (R$)',
        data: valoresOrd,
        backgroundColor: bgColors,
        borderRadius: 5,
        borderSkipped: false,
        maxBarThickness: 36,
      }]
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      layout: { padding: { right: 80 } },   // espaço para rótulos fora das barras curtas
      iinteraction: {
  mode: 'nearest',
  intersect: true
},
      plugins: {
        title: {
          display: true,
          text: titulo,
          font: { size: 13, weight: '500' },
          color: TEXT_COLOR,
          padding: { bottom: 10 }
        },
        legend: { display: false },
        tooltip: {
              callbacks: {
                title: (ctx) => ctx[0].label, // nome da filial
                label: (ctx) => 'Receita: ' + formatBRL(ctx.parsed.x)
              }
}
      },
      scales: {
        x: {
          display: false,
          grid: { display: false }
        },
        y: {
          grid: { display: false },
          ticks: { color: TEXT_COLOR, font: { size: 11 } }
        }
      },
      animation: {
        onComplete(evt) {
          const ch   = evt.chart;
          const ctx  = ch.ctx;
          const meta = ch.getDatasetMeta(0);

          ctx.save();
          ctx.font         = '500 11px sans-serif';
          ctx.textBaseline = 'middle';

          meta.data.forEach((bar, i) => {
            const val      = valoresOrd[i];
            const txt      = formatBRLCompact(val);
            const barWidth = bar.x - bar.base;
            const txtWidth = ctx.measureText(txt).width;
            const MARGIN   = 10;

            if (barWidth > txtWidth + MARGIN * 2) {
              // Cabe dentro → alinha à direita, com margem interna
              ctx.textAlign = 'right';
              ctx.fillStyle = '#ffffff';
              ctx.fillText(txt, bar.x - MARGIN, bar.y);
            } else {
              // Barra pequena → coloca fora à direita
              ctx.textAlign = 'left';
              ctx.fillStyle = TEXT_COLOR;
              ctx.fillText(txt, bar.x + 6, bar.y);
            }
          });

          ctx.restore();
        }
      }
    }
  });
}

// ============================================================
//  Gráfico 3 — Crescimento Médio por Canal  (barras verticais)
//  KPI: crescimento_receita_pct  |  Comparativo
//  Verde = positivo | Vermelho = negativo
// ============================================================
function criarGrafico3(idCanvas, titulo, labels, valores) {
  const el = document.getElementById(idCanvas);
  if (!el) { console.error('Canvas não encontrado:', idCanvas); return; }

  const bgColors = valores.map(v =>
    v >= 0 ? 'rgba(15,110,86,0.85)' : 'rgba(163,45,45,0.85)'
  );

  return new Chart(el, {
    type: 'bar',
    data: {
      labels,
      datasets: [{
        label: 'Crescimento (%)',
        data: valores,
        backgroundColor: bgColors,
        borderRadius: 5,
        borderSkipped: false,
        maxBarThickness: 52,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      interaction: { mode: 'index', intersect: false },
      plugins: {
        title: {
          display: true,
          text: titulo,
          font: { size: 13, weight: '500' },
          color: TEXT_COLOR,
          padding: { bottom: 10 }
        },
        legend: { display: false },
        tooltip: {
          callbacks: { label: ctx => ctx.parsed.y.toFixed(2).replace('.', ',') + '%' }
        }
      },
      scales: {
        x: {
          title: { display: true, text: 'Canal de venda', color: TEXT_COLOR, font: { size: 11 } },
          grid: { display: false },
          ticks: { color: TEXT_COLOR, font: { size: 11 } }
        },
        y: {
          beginAtZero: true,
          title: { display: true, text: 'Crescimento (%)', color: TEXT_COLOR, font: { size: 11 } },
          grid: { color: GRID_COLOR, borderDash: [4, 4] },
          ticks: {
            color: TEXT_COLOR,
            font: { size: 11 },
            callback: v => v.toFixed(1) + '%'
          }
        }
      }
    }
  });
}

// ============================================================
//  Gráfico 4 — Ticket Médio ao Longo do Tempo  (linha)
//  KPI: ticket_medio  |  Temporal
// ============================================================
function criarGrafico4(idCanvas, titulo, labels, valores) {
  const el = document.getElementById(idCanvas);
  if (!el) { console.error('Canvas não encontrado:', idCanvas); return; }

  return new Chart(el, {
    type: 'line',
    data: {
      labels,
      datasets: [{
        label: 'Ticket Médio (R$)',
        data: valores,
        borderColor:          '#BA7517',
        backgroundColor:      'rgba(186,117,23,0.08)',
        borderWidth:          2.5,
        pointBackgroundColor: '#BA7517',
        pointBorderColor:     '#ffffff',
        pointBorderWidth:     2,
        pointRadius:          4,
        pointHoverRadius:     6,
        fill:                 true,
        tension:              0.4,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      interaction: { mode: 'index', intersect: false },
      plugins: {
        title: {
          display: true,
          text: titulo,
          font: { size: 13, weight: '500' },
          color: TEXT_COLOR,
          padding: { bottom: 10 }
        },
        legend: { display: false },
        tooltip: {
          callbacks: { label: ctx => formatBRL(ctx.parsed.y) }
        }
      },
      scales: {
        x: {
          title: { display: true, text: 'Período', color: TEXT_COLOR, font: { size: 11 } },
          grid: { display: false },
          ticks: { color: TEXT_COLOR, font: { size: 11 } }
        },
        y: {
          beginAtZero: true,
          title: { display: true, text: 'Ticket Médio (R$)', color: TEXT_COLOR, font: { size: 11 } },
          grid: { color: GRID_COLOR, borderDash: [4, 4] },
          ticks: {
            color: TEXT_COLOR,
            font: { size: 11 },
            callback: v => formatBRL(v)
          }
        }
      }
    }
  });
}