function criarGrafico(idCanvas, titulo) {
    const ctx = document.getElementById(idCanvas);

    if (!ctx) {
        console.error("Canvas não encontrado:", idCanvas);
        return;
    }

    return new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: titulo,
                data: []
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}
