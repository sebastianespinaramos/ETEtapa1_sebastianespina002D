$("formulario_contacto").validate({
    rules: {
        nombre:{
            required: true,
            minlength:3,
            maxlength:38
        },
        email:{
            required: true,
            email: true
        },
        mensaje:{
            required: true,
            minlength:5,
            maxlength:200
        }
    }
})

var btnEnviar = document.getElementById("btnEnviar")

btnEnviar.addEventListener("click", function() {
    
    //traer los datos del formulario
    let nombre = document.getElementById("nombre").value
    let email  = document.getElementById("email").value
    let telefono = document.getElementById("telefono").value
    let tipoConsulta = document.getElementById("tipoconsulta").value
    let mensaje = document.getElementById("mensaje").value
    

    
    
   
    

})