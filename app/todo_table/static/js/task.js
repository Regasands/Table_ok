let isDragging = false;
let draggedElement = null;
let offsetX, offsetY;

function loadPositions() {
    const elements = document.querySelectorAll('.draggable');
    elements.forEach((element) => {
        const left = localStorage.getItem(`${element.id}-left`);
        const top = localStorage.getItem(`${element.id}-top`);
        console.log(left, top)
        if (left !== null && top !== null) {
            element.style.left = left;
            element.style.top = top;

        }
    });
}

function savePosition(element) {
    console.log(element)
    localStorage.setItem(`${element.id}-left`, element.style.left);
    localStorage.setItem(`${element.id}-top`, element.style.top);
}

function startDrag(e) {
    if (e.target.classList.contains('draggable')){
        isDragging = true;
        draggedElement = e.target;

        offsetX = e.clientX - draggedElement.getBoundingClientRect().left;
        offsetY = e.clientY - draggedElement.getBoundingClientRect().top;
    }
}
function drag(e) {
    if (isDragging && draggedElement) {
        const x = e.clientX - offsetX;
        const y = e.clientY - offsetY;
        draggedElement.style.left = `${x}px`;
        draggedElement.style.top = `${y}px`;
    }
}

function stopDrag(){
    if (isDragging && draggedElement) {
        savePosition(draggedElement)
        draggedElement = null;
        isDragging = false;
    }
}

document.addEventListener('mousedown', startDrag)
document.addEventListener('mousemove', drag);
document.addEventListener('mouseup', stopDrag)

window.onload = loadPositions;