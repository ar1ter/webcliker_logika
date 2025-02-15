document.getElementById('click-button').addEventListener('click', () => {
	fetch('/click')
		.then(response => response.json())
		.then(data => {
			document.getElementById('score').textContent = data.score;
			document.getElementById('balance').textContent = data.balance;
		});
});

document.getElementById('shop-button').addEventListener('click', () => {
	let shopMenu = document.getElementById('shop-menu');
	if (shopMenu.style.display === "none" || shopMenu.style.display === "") {
		shopMenu.style.display = "block";
	} else {
		shopMenu.style.display = "none";
	}
});

document.getElementById('close-shop').addEventListener('click', () => {
	document.getElementById('shop-menu').style.display = "none";
});

document.getElementById('buy-autoclicker').addEventListener('click', () => {
	fetch('/buy_autoclicker')
		.then(response => response.json())
		.then(data => {
			if (data.success) {
				document.getElementById('balance').textContent = data.balance;
			} else {
				alert("Not enough coins!");
			}
		});
});

document.getElementById('buy-multiplier').addEventListener('click', () => {
	fetch('/buy_multiplier')
		.then(response => response.json())
		.then(data => {
			if (data.success) {
				document.getElementById('balance').textContent = data.balance;
			} else {
				alert("Not enough coins!");
			}
		});
});

document.getElementById('buy-booster').addEventListener('click', () => {
	fetch('/buy_booster')
		.then(response => response.json())
		.then(data => {
			if (data.success) {
				document.getElementById('balance').textContent = data.balance;
			} else {
				alert("Not enough coins or booster already active!");
			}
		});
});

// Оновлення гри кожну секунду
setInterval(() => {
	fetch('/get_data')
		.then(response => response.json())
		.then(data => {
			document.getElementById('score').textContent = data.score;
			document.getElementById('balance').textContent = data.balance;
		});
}, 1000);
