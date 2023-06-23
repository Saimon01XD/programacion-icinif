let signUp = document.getElementById("signUp");

let signIn = document.getElementById("signIn");

let inputNombre = document.getElementById("inputNombre");

let titulo = document.getElementById("titulo");


signIn.onclick = function() {
    inputNombre.style.maxHeight = "60px";
    titulo.innerHTML = "Iniciar Sesión";
    signIn.classList.remove("disable");
    signUp.classList.add("disable");
}

signUp.onclick = function() {
    inputNombre.style.maxHeight = "0";
    titulo.innerHTML = "Registrese";
    signIn.classList.add("disable");
    signUp.classList.remove("disable");
}
