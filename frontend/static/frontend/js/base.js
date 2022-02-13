const splash = document.getElementById("splash-screen")

document.querySelector("body").onload = (e) => {
    setTimeout(() => {
        splash.style.display = "none"
    }, 1000);
}