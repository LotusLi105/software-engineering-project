(function () {
    'use strict';
    var myChart = echarts.init(document.getElementById('left-mid-nong'));

    // 指定图表的配置项和数据
    var option = {
        tooltip: {},
        legend: [{
                // 设置布局方向
                orient: 'vertical',
                // 文字和图形对齐方式
                align: 'left',
                right: '25%',
                top: '10%',
                // 图形形状
                icon: 'circle',
                padding: [20, 0, 0, 0],
                itemGap: 20,
                textStyle: {
                    borderRadius: 100,
                    color:'#fff'
                },
                data: ["Bream", "Roach", "Whitefish", "Parkki", "Perch","Pike","Smelt"]
            },
            {
                orient: 'vertical',
                right: '6%',
                top: '10%',
                padding: [20, 0, 0, 0],
                itemGap: 20,
                // 文字和图形对齐方式
                align: 'left',
                // 图形形状
                icon: 'circle',
                textStyle: {
                    borderRadius: 100,
                    color:'#fff'
                },
                data: []
            }
        ],
        series: [{
            name: '数量',
            type: 'pie',
            radius: '50%',
            right: '40%',
            bottom:'10%',
            data: [{
                    value: 35,
                    name: 'Bream'
                },
                {
                    value: 20,
                    name: 'Roach'
                },
                {
                    value: 6,
                    name: 'Whitefish'
                },
                {
                    value: 11,
                    name: 'Parkki'
                },
                {
                    value: 56,
                    name: 'Perch'
                },
                {
                    value: 17,
                    name: 'Pike'
                },
                 {
                    value: 14,
                    name: 'Smelt'
                }
            ]
        }]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener('resize',function(){
        myChart.resize();
    })

    
})()