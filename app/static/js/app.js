const logoutModal = document.getElementById('logoutModal1')
const logoutButton = document.getElementById('logout-btn')

logoutModal.addEventListener('shown.bs.modal', () => {
    logoutButton.focus()
})