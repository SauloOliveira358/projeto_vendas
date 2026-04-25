
   function criarGrafico1(idCanvas, titulo, labels, valores) {
    const ctx = document.getElementById(idCanvas);

    if (!ctx) {
        console.error("Canvas não encontrado:", idCanvas);
        return;
    }

    return new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: titulo,
                data: valores,

                barPercentage: 1,      // Aumenta a largura da barra (padrão é 0.9)
                categoryPercentage: 0.8  // Diminui o espaço entre os grupos
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

function criarGrafico2(idCanvas, titulo, labels, valores) {
    const ctx = document.getElementById(idCanvas);

    if (!ctx) {
        console.error("Canvas não encontrado:", idCanvas);
        return;
    }

    return new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: titulo,
                data: valores
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}



function criarGrafico4(idCanvas, titulo, labels, datasets) {
    const ctx = document.getElementById(idCanvas);

    if (!ctx) {
        console.error("Canvas não encontrado:", idCanvas);
        return;
    }

    return new Chart(ctx, {
        type: 'line', // 🔥 melhor para evolução no tempo
        data: {
            labels: labels,
            datasets: datasets
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: true,
                    position: 'bottom'
                }
            }
}
    });
}


function criarGrafico3(idCanvas, titulo, labels, datasets) {
    const ctx = document.getElementById(idCanvas);

    if (!ctx) {
        console.error("Canvas não encontrado:", idCanvas);
        return;
    }

    return new Chart(ctx, {
        type: 'line', // 🔥 melhor para evolução no tempo
        data: {
            labels: labels,
            datasets: datasets
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: true,
                    position: 'bottom'
                }
            }
}
    });
}