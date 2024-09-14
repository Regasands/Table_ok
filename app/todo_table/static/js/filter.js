function filterTasks (){
    const teamSelect = document.getElementById('team-select').value;
    const teamGroup = document.getElementById('group-select').value;
    const taskElement = document.querySelectorAll('.draggable');
    if (teamSelect === 'all') {
        taskElement.forEach(element => {
            if (element.getAttribute('data-group') === teamGroup){
                element.style.display = 'flex';
            }
            else {
                element.style.display = 'none';
            }
        })
    } else {
        taskElement.forEach(element => {
            if (element.getAttribute('data-item') === teamSelect){
                element.style.display = 'flex';
            }
            else {
                element.style.display = 'none';
            }
        })
    };
};

function filterTeams (){
    const selectedGroup = document.getElementById('group-select');
    const teamSelect = document.getElementById('team-select');
    const teams = teamSelect.querySelectorAll('option[data-group]');
        // Скрыть/показать опции на основе выбранной группы
        teams.forEach(option => {
            if (option.getAttribute('data-group') === selectedGroup.value) {
                option.style.display = 'block';
            } else {
                option.style.display = 'none';
        }
        teamSelect.value = 'all';
        filterTasks();
    });
};

document.getElementById('group-select').addEventListener('change', filterTeams);
document.getElementById('team-select').addEventListener('change', filterTasks);

// Выполняем фильтрацию один раз при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    filterTeams();
    filterTasks();
});