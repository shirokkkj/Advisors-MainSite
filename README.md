<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home-Advisors</title>
    <!-- Chart.js library -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link href='https://unpkg.com/boxicons@2.0.9/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
    <link rel="stylesheet" href="{{url_for('static', filename='css/home.css')}}">
</head>
<body>
    <div c-container="{{url_for('nav.nav')}}"></div>

    <div class="content">
        <h1> Seja bem vindo(a) <div class="name"> {{cookie_name}} </div></h1>
    </div>
    
    <div class="chart-container">
        <div class="user-dashboard">
            <form action="home" method="POST">
                <input type="text" id="date-picker" name="date" placeholder="Selecione a data" required>
                <button type="submit" class="button-invite-date" method='POST'>Send</button>
            </form>
            <i class='bx bxs-user-check' id="user-icon"></i>
            {{cookie_name}}
            <div class="user-info">
                <span class="user-id"> {%if cookie_password == 'masterloginpassword'%} <strong>master</strong> {%else%} {{user_id}} {%endif%} </span>
                <span class="user-status">0</span>  
                <!-- <div class="calendar-container">
                    <!-- Formulário para enviar a data -->
                <!-- </div> --> 
        </div>
        <hr class="dividor-infos">
        <div class="result-text">
            Resultado
        </div>
        <div class="result-value">
            R${{resultado}}
        </div>
        <hr class="hr-result">
        <canvas id="myLineChart"></canvas>
    </div>


    <script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
    <script>
        // Definindo os dados do gráfico
        const labels = {{ data['labels'] | tojson }};
        const values = {{ data['values']  | tojson }};

        // Função para criar cor baseada no valor
        function getColor(value) {
            return value >= 0 ? 'rgba(39, 245, 86, 1)' : 'rgba(217, 30, 24, 1)';
        }

        // Configuração do gráfico
        const data = {
            labels: labels,
            datasets: [{
                label: 'Ganho',
                data: values,
                borderWidth: 3, // Largura da linha
                tension: 0.0, // Suavizar a linha
                pointRadius: 0, // Remove os pontos
                fill: false, // Não preencher abaixo da linha
                borderColor: 'rgba(39, 245, 86, 1)', // Cor padrão
                segment: {
                    borderColor: ctx => {
                        const { p0, p1 } = ctx;
                        return p1.parsed.y < 0 ? 'rgba(217, 30, 24, 1)' : 'rgba(39, 245, 86, 1)';
                    }
                }
            }]
        };

        const config = {
            type: 'line',
            data: data,
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    x: {
                        grid: {
                            display: false,
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        ticks: {
                            color: 'rgba(255, 255, 255, 0.7)'
                        }
                    },
                    y: {
                        grid: {
                            display: false,
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        ticks: {
                            color: 'rgba(255, 255, 255, 0.7)'
                        }
                    }
                }
            }
        };

        // Renderizando o gráfico
        const myLineChart = new Chart(
            document.getElementById('myLineChart'),
            config
        );


        document.addEventListener('DOMContentLoaded', function() {
            flatpickr("#date-picker", {
                dateFormat: "d/m/Y",
                defaultDate: "01/01/2024",
                mode: "multiple",           // Permite selecionar múltiplas datas
                maxDate: '31/12/2024'                  // Limita a seleção a 5 datas
            });
        });
    </script>
    <script src="{{ url_for('static', filename='js/cru.js') }}"></script>
</body>
</html>