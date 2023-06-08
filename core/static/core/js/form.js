//validaciones formulario (por implementar)
$(document).ready(function () {
    $("#form1").submit(function (e) {
        var nombre = $("#nombre1").val();
        var clave1 = $("#pass1").val();
        var clave2 = $("#pass2").val();
        var correo = $("#correo1").val();
        var num = $("#numero1").val();
        var mensaje = "";

        let entrar = false;
        let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/
        let regexContraseña = /[QWERTYUIOPASDFGHJKLÑZXCVBNM]/
        let regexPass = /[1234567890]/
        let regexNmbr = /^[0-9]*$/

        if (nombre.trim().length < 4 || nombre.trim().length > 12) {
            mensaje += 'El nombre no es valido <br>';
            entrar = true;
        }
        if (regexPass.test(nombre)) {
            mensaje += 'El nombre solo pueden ser caracteres alfabeticos <br>'
            entrar = true;
        }
        if (!regexEmail.test(correo)) {
            mensaje += 'El email no es valido <br>'
            entrar = true
        }
        if (!regexNmbr.test(num)) {
            mensaje += 'Deben ser caracteres numericos <br>'
            entrar = true;
        }
        if (num.length < 9 || num.length > 9 && num.length > 1) {
            mensaje += 'Numero de Telefono invalido <br>'
            entrar = true;
        }
        if (clave1 != clave2) {
            mensaje += 'Las contraseñas no coinciden <br>'
            entrar = true;
        }
        if (clave1.length < 5) {
            mensaje += 'La contraseña debe tener al menos 5 caracteres <br>'
            entrar = true;
        }
        if (!regexContraseña.test(clave1)) {
            mensaje += 'La contraseña debe tener al menos una mayuscula <br>'
            entrar = true;
        }
        if (!regexPass.test(clave1)) {
            mensaje += 'La contraseña debe tener al menos un caracter numerico <br>'
            entrar = true;
        }
        if (entrar) {
            $("#warnings").html(mensaje);
            e.preventDefault();
        } else {
            $("#warnings").html("<button type='submit' href=''> :3 </button>");
        }
    });
    function esMayuscula(letra) {
        return letra === letra.toUpperCase();
    }
})
$(document).ready(function () {
    $("#form2").submit(function (a) {
        a.preventDefault();
        var clave3 = $("#pass3").val();
        var correo2 = $("#correo2").val();
        var mensaje = "";
        let entrar = false;
        let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/

        if (clave3 != "El7profeporfa") {
            mensaje += 'Contraseña Equivocada <br>'
            entrar = true;
        }
        if (!regexEmail.test(correo2)) {
            mensaje += 'El email no es valido <br>'
            entrar = true
        }
        if (entrar) {
            $("#warnings").html(mensaje);
        }
        else {
            $("#warnings").html("<button type='submit' href='indexmenu.html'> Entrar al sistema </button>");
        }
    });
})