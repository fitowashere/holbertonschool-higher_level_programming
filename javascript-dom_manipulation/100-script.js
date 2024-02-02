document.addEventListener('DOMContentLoaded', (event) => {
  // Add item
  const addItem = document.querySelector('#add_item');
  addItem.addEventListener('click', () => {
    const ul = document.querySelector('UL.my_list');
    const li = document.createElement('li');
    li.textContent = 'Item';
    ul.appendChild(li);
  });

  // Remove last item
  const removeItem = document.querySelector('#remove_item');
  removeItem.addEventListener('click', () => {
    const ul = document.querySelector('UL.my_list');
    const lastLi = ul.querySelector('li:last-child');
    if (lastLi) ul.removeChild(lastLi);
  });

  // Clear list
  const clearList = document.querySelector('#clear_list');
  clearList.addEventListener('click', () => {
    const ul = document.querySelector('UL.my_list');
    ul.innerHTML = '';
  });
});
