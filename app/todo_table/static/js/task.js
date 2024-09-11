let isDragging = false;
let isResizing = false;
let draggedElement = null;
let resizerElement = null;
let offsetX, offsetY;
let maxZIndex;

function loadPositions() {
    const elements = document.querySelectorAll('.draggable');
    elements.forEach((element) => {
        const left = localStorage.getItem(`${element.id}-left`);
        const top = localStorage.getItem(`${element.id}-top`);
        const width = localStorage.getItem(`${element.id}-width`);
        const height = localStorage.getItem(`${element.id}-height`);
        const zindex = localStorage.getItem(`${element.id}-zindex`);

        console.log(left, top)
        if (left !== null && top !== null) {
            element.style.left = left;
            element.style.top = top;
        }
        if (width !== null) {
            element.style.width = width;
        }
        if (height !== null){
            element.style.height = height;
        }
        if (zindex !== null){
            element.style.zIndex = zindex;
        }
    });
}

function savePosition(element) {
    console.log(element)
    localStorage.setItem(`${element.id}-left`, element.style.left);
    localStorage.setItem(`${element.id}-top`, element.style.top);
    localStorage.setItem(`${element.id}-width`, element.style.width);
    localStorage.setItem(`${element.id}-height`, element.style.height);
    localStorage.setItem(`${element.id}-zindex`, element.style.zIndex + 1);
}

function startDragorResizer(e) {
     if (e.target.classList.contains('resizer')) {
        isResizing = true;
        resizerElement = e.target
        draggedElement = resizerElement.parentElement.parentElement;
        let maxZIndex = Math.max(...[...document.querySelectorAll('*')].map(el => +getComputedStyle(el).zIndex || 0));
        if (draggedElement.style.zIndex == maxZIndex){
            draggedElement.style.zIndex = maxZIndex;
            } else{
                draggedElement.style.zIndex = maxZIndex + 1;  
            }

    }
    else if (e.target.classList.contains('draggable')  || e.target.closest('.draggable')){
        isDragging = true;
        draggedElement = e.target.closest('.draggable');
        let maxZIndex = Math.max(...[...document.querySelectorAll('*')].map(el => +getComputedStyle(el).zIndex || 0));
        if (draggedElement.style.zIndex == maxZIndex){
        draggedElement.style.zIndex = maxZIndex;
        } else{
            draggedElement.style.zIndex = maxZIndex + 1;  
        }


        offsetX = e.clientX - draggedElement.getBoundingClientRect().left;
        offsetY = e.clientY - draggedElement.getBoundingClientRect().top;

    }
}
function resizer(e){
    if (isResizing && draggedElement) {
        const newWidth = e.clientX - draggedElement.getBoundingClientRect().left;
        const newHeight = e.clientY - draggedElement.getBoundingClientRect().top;
        if (newHeight >= 150) {
            draggedElement.style.height = `${newHeight}px`
        }
        if (newWidth >= 150) {
            draggedElement.style.width = `${newWidth}px`
        }

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

function stopDragorResize(){
    if ((isDragging || isResizing) && draggedElement) {
        savePosition(draggedElement)
        draggedElement = null;
        resizerElement = null;
        isDragging = false;
        isResizing = false;
        maxZIndex = null;

    }
}


document.addEventListener('mousedown', startDragorResizer);
document.addEventListener('mousemove', (e) => {
    if (isResizing) {
        resizer(e);
    } else if (isDragging) {
        drag(e);
    }
});
document.addEventListener('mouseup', stopDragorResize);

window.onload = loadPositions;