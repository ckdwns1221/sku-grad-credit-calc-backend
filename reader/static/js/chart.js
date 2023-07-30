var i1 = 0;
var width1 = 0;
var id1;
var elem1 = document.getElementById("progress-bar1");
var max1 = elem1.getAttribute('score_did')/parseFloat(elem1.getAttribute('score_need'))*100;
if(max1 > 100) max1 = 100

var i2 = 0;
var width2 = 0;
var id2;
var elem2 = document.getElementById("progress-bar2");
var max2 = elem2.getAttribute('score_did')/parseFloat(elem2.getAttribute('score_need'))*100;
if(max2 > 100) max2 = 100

var i3 = 0;
var width3 = 0;
var id3;
var elem3 = document.getElementById("progress-bar3");
var max3 = elem3.getAttribute('score_did')/parseFloat(elem3.getAttribute('score_need'))*100;
if(max3 > 100) max3 = 100



function frame1() {
    if (width1 >= max1) {
        clearInterval(id1);
        i1 = 0;
    } else {
        width1++;
        elem1.style.width = width1 + "%";
        elem1.innerHTML = width1 + "%";
    }
}

function frame2() {
    if (width2 >= max2) {
        clearInterval(id2);
        i2 = 0;
    } else {
        width2++;
        elem2.style.width = width2 + "%";
        elem2.innerHTML = width2 + "%";
    }
}

function frame3() {

    if (width3 >= max3) {
        clearInterval(id3);
        i3 = 0;
    } else {
        width3++;
        elem3.style.width = width3 + "%";
        elem3.innerHTML = width3 + "%";
    }
}

function start1() {
    if (i1 == 0) {
        i1 = 1;
        id1 = setInterval(frame1, 10);
    }
}

function start2() {
    if (i2 == 0) {
        i2 = 1;
        id2 = setInterval(frame2, 10);
    }
}

function start3() {
    if (i3 == 0) {
        i3 = 1;
        id3 = setInterval(frame3, 10);
    }
}


start1(); // 자동 실행
start2(); // 자동 실행
start3(); // 자동 실행

/*doughnutChar*/
const doughnutChart = document.querySelector("#doughnut-chart");
const doughnutData = {
    labels: ["A+ ~ A0", "B+ ~ B0", "C+ ~ C0", "D+ ~ D0", "F"],
    data: [doughnutChart.getAttribute('A'), doughnutChart.getAttribute('B'), doughnutChart.getAttribute('C'), doughnutChart.getAttribute('D'), doughnutChart.getAttribute('F')],
};

new Chart(doughnutChart, {
    type: "doughnut",
    data: {
        labels: doughnutData.labels,
        datasets: [{
            label: [],
            data: doughnutData.data,
        }, ],
    },
    options: {
        borderWidth: 1,
        borderRadius: 2,
        hoverBorderWidth: 4,
        plugins: {
            legend: {
                display: false,
            },
            tooltip: {
                callbacks: {
                    label: function(context) {
                        const labelIndex = context.dataIndex;
                        const dataValue = doughnutData.data[labelIndex];
                        return dataValue + "%";
                    },
                },
            },
        },
    },
});

/*line chart*/
const linetChart = document.querySelector("#line-chart");
const lineChartData = new Chart(linetChart, {
    type: "line",
    data: {
        labels: [
            "1-1",
            "1-2",
            "2-1",
            "2-2",
            "3-1",
            "3-2",
            "4-1",
            "4-2",
        ],
        datasets: [{
            data: [linetChart.getAttribute('1_1'), linetChart.getAttribute('1_2'), linetChart.getAttribute('2_1'), linetChart.getAttribute('2_2'), linetChart.getAttribute('3_1'), linetChart.getAttribute('3_2'), linetChart.getAttribute('4_1'), linetChart.getAttribute('4_2')],
        }, ],
    },
    options: {
        plugins: {
            legend: {
                display: false,
            },
        },
    },
});