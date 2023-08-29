function activateNavItem(event) {
  const navItems = document.querySelectorAll('.custom-nav-link, .dropdown-item');
  navItems.forEach((navItem) => {
    navItem.classList.remove('active');
  });
  event.target.classList.add('active');

  // Check if the clicked item is a dropdown-item
  if (event.target.classList.contains('dropdown-item')) {
    const dropdownToggle = document.querySelector('#navbarDropdownMenuLink');
    dropdownToggle.innerText = event.target.innerText;
    dropdownToggle.classList.add('active'); // Add the 'active' class to the dropdown toggle
  }
}
