window.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('sidebarToggle');
    console.log(toggle)
    const overlay = document.getElementById('sidebar-overlay');
    const closeBtn = document.getElementById('sidebarCloseBtn');
    const body = document.body;
    
    if (toggle) {
        const closeSidebar = () => body.classList.remove('sidebar-open');
        
        toggle.addEventListener('click', () => {
            body.classList.toggle('sidebar-open');
            console.log('!!!!!!!!')
        });
        
        // Обработчик для кнопки закрытия
        if (closeBtn) {
            closeBtn.addEventListener('click', closeSidebar);
        }
        
        // Обработчик для клика вне sidebar
        if (overlay) {
            overlay.addEventListener('click', closeSidebar);
        }
        
        // Обработчик клавиши Escape
        document.addEventListener('keydown', (event) => {
            if (event.key === 'Escape' && body.classList.contains('sidebar-open')) {
                closeSidebar();
            }
        });
    }
});