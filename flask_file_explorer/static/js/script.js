/* Add your custom JavaScript code here */
function toggleFolder(element, event) {
    let parent = element.parentElement;
    sublisting = parent.querySelector('ul'); // .directory-listing
    
    if (sublisting.classList.contains('directory-list')) {
        
        if (sublisting.style.display == 'none') {
            sublisting.style.display = 'block';
        } else {
            sublisting.style.display = 'none';
        }
        //sublisting.classList.toggle('d-none');
        //ul = document.createElement('ul');
        //parent.appendChild(ul);
        event.preventDefault();
        element.dispatchEvent(new Event('htmx:abort'));
    }
}