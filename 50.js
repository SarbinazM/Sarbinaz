document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Navbar fonini scroll qilinganda o'zgartirish
    const nav = document.querySelector('nav');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            nav.style.background = '#ffffff';
            nav.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
        } else {
            nav.style.background = '#f8f8f8';
            nav.style.boxShadow = 'none';
        }
    });

    // 2. Statistika raqamlarini animatsiya bilan chiqarish (Counter)
    const stats = document.querySelectorAll('.stat-item h2');
    
    const animateStats = () => {
        stats.forEach(stat => {
            const target = parseInt(stat.innerText);
            let count = 0;
            const speed = target / 100; // Tezlikni sozlash

            const updateCount = () => {
                if (count < target) {
                    count += speed;
                    stat.innerText = Math.ceil(count) + "+";
                    setTimeout(updateCount, 20);
                } else {
                    stat.innerText = target + "+";
                }
            };
            updateCount();
        });
    };

    // Sahifa yuklanganda statistika animatsiyasini ishga tushirish
    animateStats();

    // 3. "Batafsil" tugmalari uchun oddiy bosish effekti
    const buttons = document.querySelectorAll('.btn-main, .btn-card');
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            alert("Tez kunda batafsil ma'lumot qo'shiladi!");
        });
    });

    // 4. Konsolga salom xabari (Tekshirish uchun)
    console.log("Veb-sahifa JavaScript bilan muvaffaqiyatli bog'landi!");
});