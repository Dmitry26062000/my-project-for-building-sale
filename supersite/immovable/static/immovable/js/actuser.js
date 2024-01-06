function showTab(tabId) {
    var tabs = document.querySelectorAll('.hidden-tab');
    tabs.forEach(function (tab) {
        tab.style.display = 'none';
        5
    });
    var selectedTab = document.getElementById(tabId);
    selectedTab.style.display = 'block';
};

function toggleTable(myTable) {
    var table = document.getElementById(myTable);
    if (table.style.display === 'none') {
        table.style.display = 'table';
    } else {
        table.style.display = 'none';
    }
};

function mainmenu() {
    window.location.href = "/"
};

function printDiv(divName) {
    const s = 'Дата подписания:_______________', logot = 'ЖК Орион ', Sign = 'Подпись:', Empty = '     ';
    var printContents = document.getElementById(divName).innerHTML;
    var datesign = s.innerHTML;
    w = window.open();
    w.document.write(logot.toUpperCase(), printContents, s, Empty, Sign);
    w.print();
    w.close();
};

