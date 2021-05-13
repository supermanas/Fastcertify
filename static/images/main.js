const alertbox = document.getElementById('alert-box')
const imgBox = document.getElementById('img-box')
const form = document.getElementById('p-form')
const names = document.getElementById('id_name')
const description = document.getElementById('id_description')
var contri = document.getElementById('id_types')
const image = document.getElementById('id_image')
console.log(image)
console.log(contri)
const url = ""
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const handleAlerts = (type,text) =>{
    alertbox.innerHTML = `<div class="alert alert-${type}" role="alert">
                                ${text}
                         </div>`
}

image.addEventListener('change',()=>{
    const img_data = image.files[0]
    console.log(img_data)
    console.log(contri)
    const url = URL.createObjectURL(img_data)

    imgBox.innerHTML = `<img src="${url}" width="100%" height="100%">`

})

form.addEventListener('submit',e=>{
    e.preventDefault()
    spp = contri.value
    console.log(spp)
    const fd = new FormData()
    fd.append('csrfmiddlewaretoken',csrf[0].value)
    fd.append('name',names.value)
    fd.append('description',description.value)
    fd.append('image',image.files[0])
    fd.append('types',spp)

    $.ajax({
        type:'POST',
        url:url,
        enctype:'multipart/form-data',
        data:fd,
        success:function(response){
            const sText = `successfully saved ${response.names}`
            console.log(response)
            handleAlerts('success',sText)
            setTimeout(()=>{
                alertbox.innerHTML=""
                imgBox.innerHTML=""
                names.value=""
                description.value=""
                image.value=""
                types.value=""

            },2000)
        },
        error:function(error){
            handleAlerts('danger','something went wrong')
        },
        cache:false,
        contentType:false,
        processData:false,

    })

})